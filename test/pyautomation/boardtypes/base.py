import pexpect.replwrap

class BoardBase(object):
    def __init__(self):
        pass

    def baseboot(self, p):
        self.r = pexpect.replwrap.REPLWrapper(p, "=>", None)
        return self.r

    def run_command(self, cmd):
        self.r.run_command(cmd)

