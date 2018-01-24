from fabric.api import * 

# @task(alias="showVersion")
def showVersion():
    """
    This will save the current running configuration as the startup 
    configuration.
    """
    run("show version")
