from nornir import InitNornir
from nornir_utils.plugins.functions import print_result

def say_hello(task):
    return f"Hello, {task.host} - {task.host.groups} - {task.host.hostname}"

nr = InitNornir(config_file="config.yaml")
result = nr.run(task=say_hello)
print_result(result)