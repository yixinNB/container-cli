import json
import sys

import questionary
from loguru import logger


def __ask_ports():
    print("Please enter ALL host ports and their corresponding ports in the container one by one")
    target_ports = {}  # {host_port: container_port}
    while 1:
        h = questionary.text("Please input host port, empty to exit").ask()
        if h == "":
            break
        c = questionary.text("Please input corresponding container port, empty to exit").ask()
        target_ports[h] = c

    for host_port in target_ports:
        container_port=target_ports[host_port]
        print(f"host port {host_port} <-> container port {container_port}")
    if not questionary.confirm("Is these correct?").ask():
        sys.exit(-1)
    return target_ports


def __update_ports(id, ports: dict):
    '''

    :param id: container id
    :param ports: {host_port: container_port}
    '''
    hostconfig_path = f"/var/lib/docker/containers/{id}/hostconfig.json"
    config_path = f"/var/lib/docker/containers/{id}/config.v2.json"

    hostconfig = json.load(open(hostconfig_path, 'r'))
    config = json.load(open(config_path, 'r'))

    new_PortBindings = {}
    new_ExposedPorts = {}
    new_Ports = {}
    for item_key in ports:
        host_port = item_key
        container_port = str(ports[item_key]) + "/tcp"
        new_PortBindings[container_port] = [{"HostIp": '', "HostPort": str(host_port)}]

        new_ExposedPorts[container_port] = {}

        new_Ports[container_port] = [
            {"HostIp": "0.0.0.0", "HostPort": host_port},
            {"HostIp": "::", "HostPort": host_port},
        ]

    hostconfig["PortBindings"] = new_PortBindings
    config["Config"]["ExposedPorts"] = new_ExposedPorts
    config["NetworkSettings"]["Ports"] = new_Ports

    json.dump(hostconfig, open(hostconfig_path, 'w'))
    json.dump(config, open(config_path, 'w'))


def change_ports(container_id):
    target_ports = __ask_ports()
    __update_ports(container_id, target_ports)
    logger.info("finished")
