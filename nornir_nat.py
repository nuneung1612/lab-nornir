from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_config
from nornir_utils.plugins.functions import print_result

def configure_nat(task):

    if str(task.host) == "R2-13":
        nat_config = [
            "access-list 1 permit 192.168.1.0 0.0.0.255",
            "access-list 1 permit 192.168.2.0 0.0.0.255",
            "ip nat inside source list 1 interface GigabitEthernet0/2 vrf control-data overload",
            "int g0/1",
            "ip nat inside",
            "exit",
            "int gi0/2",
            "ip nat outside",
        ]
    else:
        nat_config = []

    if nat_config:
        task.run(task=netmiko_send_config, config_commands=configure_nat)


nr = InitNornir(config_file="config.yaml")
results = nr.run(task=configure_nat)
print_result(results)
