from fabric.api import run, env, roles, task, hide, open_shell, runs_once, local, settings
from fabric.colors import red, cyan, yellow, green
from fabric.contrib.console import confirm
from getpass import getpass

from envdefs import *

@task(alias="reboot")
def reboot():
    """
    This will save the current running configuration as the startup 
    configuration.
    """
    run("reboot")
