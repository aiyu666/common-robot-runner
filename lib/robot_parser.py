import json
import os
import sys
from robot.api import ExecutionResult, ResultVisitor, SuiteVisitor


class RobotReportParser(SuiteVisitor):
    def __init__(self, is_allpass=True):
        self.pass_list = []
        self.fail_list = []
        self.include_tags = ""
        self.total = 0
        self.pass_rate = 0
        self.pass_cases = 0
        self.fail_cases = 0
        self.total_cases = 0
        self.is_allpass = is_allpass

    def visit_suite(self, suite):
        if suite.status == "PASS":
            if suite.source:
                if suite.name == "Test":
                    self.include_tags = suite.source
                else:
                    self.suite_name = suite.source.split("/")[-1]
        if suite.status == "FAIL":
            if suite.source:
                if suite.name == "Test":
                    self.include_tags = suite.source
                else:
                    self.suite_name = suite.source.split("/")[-1]

        suite.suites.visit(self)
        suite.tests.visit(self)

    def visit_test(self, test):
        if test.passed == False:
            self.is_allpass = False
        if test.status == "PASS":
            test_list = lambda: None
            test_list.id = test.id
            test_list.suite = self.suite_name
            test_list.case_name = test.name
            self.pass_list.append(test_list)
        if test.status == "FAIL":
            test_list = lambda: None
            test_list.id = test.id
            test_list.suite = self.suite_name
            test_list.case_name = test.name
            self.fail_list.append(test_list)

    def parser(self, file_dir):
        if not os.path.exists(file_dir):
            raise AssertionError('No Output file found.')

        result = ExecutionResult(file_dir)
        result.suite.visit(self)
        self.pass_cases = result.statistics.total.all.passed
        self.fail_cases = result.statistics.total.all.failed
        self.total_cases = float(result.statistics.total.all.failed + result.statistics.total.all.passed)
        self.fail_case_total = len(self.fail_list)
        self.pass_case_total = len(self.pass_list)
        self.pass_rate = int(self.pass_cases / self.total_cases * 100)