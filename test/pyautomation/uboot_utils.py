import os.path

module_dir = os.path.dirname(__file__)
module_dir = os.path.abspath(module_dir)
uboot_dir = module_dir + "/../.."
uboot_dir = os.path.abspath(uboot_dir)

def build_board(board):
    pass

def uboot_bin(board):
    return module_dir + "/var/build-" + board + "/u-boot"
