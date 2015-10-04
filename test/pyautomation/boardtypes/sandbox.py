import boardtypes.base
import pexpect
import pexpect.replwrap
import sys
import uboot_utils

class Board(boardtypes.base.BoardBase):
    def __init__(self):
        pass

    def boot(self):
        p = pexpect.spawn(uboot_utils.uboot_bin('sandbox'))
        p.logfile_read = sys.stdout
        return self.baseboot(p)

    def shutdown(self):
        try:
            self.r.run_command("reset")
            self.r.close()
        except pexpect.EOF:
            pass
