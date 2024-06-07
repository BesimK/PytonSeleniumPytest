import os
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor


def run_tests(browser):
    env = os.environ.copy()
    env['BROWSER'] = browser
    allure_dir = f"Reports/{browser}/{browser}_report"
    subprocess.run(
        ["behave", f"-D Browser = {browser}", "-f allure_behave.formatter:AllureFormatter", "-o",
         allure_dir],
        env=env)


if os.name == 'nt':  # Windows
    browsers = ["chrome", "firefox", "edge"]
else:  # Non-Windows (e.g., macOS, Linux)
    browsers = ["chrome", "firefox", "safari"]

with ThreadPoolExecutor(max_workers=len(browsers)) as executor:
    executor.map(run_tests, browsers)
    time.sleep(2)
