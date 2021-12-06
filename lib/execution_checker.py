from robot.api import ExecutionResult, ResultVisitor

class ExecutionChecker(ResultVisitor):

    def __init__(self, is_allpass=True):
        self.is_allpass = is_allpass

    def visit_test(self, test):
        if test.passed is False:
            self.is_allpass = False