class TestCase0(object):
    """Simple environment variable tests"""

    def step0(self):
        """Print a variable that exists"""
        # FIXME: Implement this
        pass

    def step1(self):
        """Print a variable that doesn't exist"""
        # FIXME: Implement this
        pass

# FIXME: Convert all these to steps:
def testcase_0(b):
    """Print a variable that exists"""
    b.run_command("printenv baudrate")
    # FIXME: Validate result

def testcase_1(b):
    """Print a variable that doesn't exist"""
    b.run_command("printenv test_env")
    # FIXME: Validate result

def testcase_2(b):
    """Unset a nonexistent variable"""
    b.run_command("setenv test_env")
    # FIXME: Validate result

def testcase_3(b):
    """Set a new variable"""
    b.run_command("setenv test_env foo")
    # FIXME: Validate result

def testcase_4(b):
    """Unset a variable"""
    b.run_command("setenv test_env")
    # FIXME: Validate result

def testcase_5(b):
    """Set an existing variable"""
    b.run_command("setenv test_env foo")
    b.run_command("setenv test_env bar")
    # FIXME: Validate result

def testcase_6(b):
    """Clean up"""
    b.run_command("setenv test_env")
    # FIXME: Validate result
