from starcluster import clustersetup
from starcluster.logger import log


class WhoamiPlugin(clustersetup.DefaultClusterSetup):
    """
    Runs the whoami command.
    """

    def __init__(self):
        pass

    def run(self, nodes, master, user, user_shell, volumes):
        log.info("Running whoami plugin")

        res = master.ssh.execute('whoami')
        log.info("whoami?: " + res[0])
