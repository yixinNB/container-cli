# introduction
When we initialize a container, if we accidentally make a port mapping mistake, we need to rebuild the container or modify the docker configuration file manually.  
This tool is designed to automate the process of modifying docker configuration files.
# demo
This demo shows how container-cli can modify the port mapping of a container named python
```
admin@ubuntuyyy:~$ cc  #short of container-cli
current user is not root
? confirm close docker? Yes
INFO     | container_cli:__close_docker:17 - closing docker
0 Warning: Stopping docker.service, but it can still be activated by:
  docker.socket
? Please input container name: python
Please enter ALL host ports and their corresponding ports in the container one by one
? Please input host port, empty to exit 23
? Please input container port, empty to exit 22
? Please input host port, empty to exit
? confirm? Yes
INFO     | container_cli.change_ports:change_ports:59 - finished
docker restarted, please restart your container
```

# installation
## step1 install pipx
By default, ubuntu doesn't have a way to install pipx using pip, so we have to:
```
sudo apt-get update && sudo apt-get install pipx && pipx ensurepath
```
After that we need to shut down the terminal and reenter it (or just reboot)
## step2 install container-cli
```
pipx install container-cli
```

# usage
Type `cc` or `container_cli` on the command line to start, and follow the prompts.

## Star History

![Star History Chart](https://api.star-history.com/svg?repos=yixinnb/container-cli&type=Date)
