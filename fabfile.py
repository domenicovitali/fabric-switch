from fabric.api import * 
from fabric.api import run, env, roles, task, hide, open_shell, runs_once, local, settings, parallel

from fabric.contrib.console import confirm

from fabric.colors import red, cyan, yellow, green

env.user = "admin"
user.password = "*****"
env.no_keys = True
env.use_ssh_config = True
env.use_shell = False

# @task(alias="showVersion")
def showVersion():
    """
    This will save the current running configuration as the startup 
    configuration.
    """
    
    with open("/tmp/debug","w") as ofile:
        ofile.write(cyan("Test session %s @ %s" %
          (env.user , env.host) ) )

    try:
        #open_shell("terminal lenght 0" )
        #open_shell("show version" )
        # todo: insert password
        open_shell("enable\n\nterminal lenght 0\nshow version\n \nexit\n" )
        # open_shell("exit\n" )
        # open_shell("enable\nP1ngazz0\nterminal lenght 0\nshow version\n exit\n" )
        # open_shell("show version", shell=False)
    except Exception as e:
        print( red( "%s exception: %s" % (env.host, e) ) )
    return
