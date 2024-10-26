from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_config
from nornir_utils.plugins.functions import print_result

def configure_ospf(task):

    if str(task.host) == "R1-13":
        ospf_config = [
            "router ospf 1 vrf control-data",
            "network 192.168.2.0 0.0.0.255 area 0",
            "network 192.168.1.0 0.0.0.255 area 0",
        ]
    elif str(task.host) == "R2-13":
        ospf_config = [
            "router ospf 1 vrf control-data",
            "network 192.168.1.0 0.0.0.255 area 0",
            "default-information originate",
        ]
    else:
        ospf_config = []

    if ospf_config:  # Ensure there's a config to send
        task.run(task=netmiko_send_config, config_commands=ospf_config)


nr = InitNornir(config_file="config.yaml")
results = nr.run(task=configure_ospf)
print_result(results)
