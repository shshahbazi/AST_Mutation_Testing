import os
import re

import pytest

from run import PYTHON_FILE


class Plugin:
    def __init__(self):
        self.killed = False

    def pytest_runtest_logreport(self, report):
        if (not report.passed) and (not self.killed):
            self.killed = True


def run_tests(code, mutation_number):
    with open(PYTHON_FILE, 'r') as f:
        split_text = re.split(r'#\s?Test', f.read(), flags=re.IGNORECASE)
    new_content = code + '# Test' + split_text[1]

    filename = os.getcwd() + '/mutation/mutation_file' + str(mutation_number) + '.py'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as f:
        f.write(new_content)

    plugin = Plugin()
    pytest.main(['-p', 'no:terminal', filename], plugins=[plugin])
    return plugin.killed
