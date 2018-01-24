from fabric.api import * 

# @task(alias="reboot")
def reboot():
    """
    This will save the current running configuration as the startup 
    configuration.
    """
    run("reboot")
