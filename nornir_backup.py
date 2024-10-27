import os
from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command

BACKUP_DIR = "backups/"

nr = InitNornir(config_file="config.yaml")

def create_backups_dir():
    if not os.path.exists(BACKUP_DIR):
        os.mkdir(BACKUP_DIR)


def save_config_to_file(method, hostname, config):
    filename =  f"{hostname}-{method}.cfg"
    with open(os.path.join(BACKUP_DIR, hostname), "w") as f:
        f.write(config)


def get_netmiko_backups():
    backup_results = nr.run(
        task=netmiko_send_command, 
        command_string="show run"
        )

    for hostname in backup_results:
        save_config_to_file(
            method="netmiko",
            hostname=hostname,
            config=backup_results[hostname][0].result
        )


def main():
    create_backups_dir()
    get_netmiko_backups()

if __name__ == "__main__":
    main()