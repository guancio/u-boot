#!/usr/bin/python

# FIXME: Get (list of?) board type(s) from cmdline, or file
import boardtypes.sandbox

# FIXME: Convert this to iterate over testcases then steps within them
def run_tests(b, module):
    i = 0
    while True:
        f = getattr(module, 'testcase_' + str(i), None)
        if not f:
            break
        f(b)
        i += 1

# FIXME: Build U-Boot
# FIXME: Before running any tests, run any preparation steps
#        e.g. to generate test data
b = boardtypes.sandbox.Board()
b.boot()
# FIXME: Get list of tests from cmdline, or file
import test_boot
run_tests(b, test_boot)
import test_env
run_tests(b, test_env)
b.shutdown()
# FIXME: Clean up var dir (or just builds, or just test data, ...)
