import re
import subprocess
import sys
import time
import os

from loguru import logger
import questionary

from .change_ports import change_ports


def __close_docker():
    while 1:
        logger.info("closing docker")
        status, output = subprocess.getstatusoutput("systemctl stop docker")
        print(status, output)
        if status == 0:
            break
        else:
            logger.error("can NOT close docker")
            time.sleep(5)
    subprocess.getstatusoutput("service docker stop")


def __start_docker():
    subprocess.getstatusoutput("systemctl start docker")
    subprocess.getstatusoutput("service docker restart")
    print("docker restarted, please restart your container")


def __get_container_id():
    while 1:
        container_name = questionary.text("Please input container name").ask()
        status, output = subprocess.getstatusoutput(f"docker inspect {container_name} | grep Id")
        if status != 0:
            logger.error("container name error")
            continue
        pattern = '"Id": "([a-zA-Z0-9]{64}?)",'

        # 使用正则表达式匹配并提取中间的内容
        match = re.search(pattern, output)
        if not match:
            logger.error("can't use re to match id")
            continue
        return match.groups()[0]


def check_root():
    if os.geteuid() != 0:
        print("current user is not root")
        current_path = os.path.abspath(__file__)
        venv_python_path = os.path.abspath(sys.executable)
        # command = ['sudo', venv_python_path, current_path] + sys.argv[1:]
        command = ["sudo", venv_python_path, "-m", "container_cli"] + sys.argv[1:]
        subprocess.call(' '.join(command), shell=True)
        sys.exit()


def main():
    check_root()

    # opts,args=checkopt.checkopt("debug=")# --debug [path]
    # if "debug" in opts:
    #     logger.level("debug")

    if not questionary.confirm("confirm close docker?").ask():
        sys.exit(-1)
    __close_docker()
    id = __get_container_id()
    change_ports(id)

    __start_docker()
