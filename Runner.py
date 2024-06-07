# This file is the Runner For Parallel Execution Report generation automatically
r"""
----Use subprocess to run commands below
----Run ParallelExecutor
----Run HTML-Combine
----Rename all generated combined reports
----Run send_message method for all combined reports
"""
import os
import shutil
import subprocess
import time


def start_execution():
    subprocess.run('python Test/Runner/ParallelExecutor.py', shell=True)
    time.sleep(2)


def run_allure_combine():
    root = os.getcwd()
    if wait_for_file(f"{root}\\Allure\\chrome\\chrome_report"):
        subprocess.run(
            f'allure-combine Allure\\chrome\\chrome_report --dest {root}\\HTML\\chrome --auto-create-folders',
            shell=True)
        subprocess.run(
            f'allure-combine Allure\\firefox\\firefox_report --dest {root}\\HTML\\firefox --auto-create-folders',
            shell=True)
        subprocess.run(f'allure-combine Allure\\edge\\edge_report --dest {root}\\HTML\\edge --auto-create-folders',
                       shell=True)


def run_allure_rename():
    root = os.getcwd()
    if wait_for_file(f"{root}\\HTML\\chrome\\complete.html"):
        os.rename(f"{root}\\HTML\\chrome\\complete.html",
                  f"{root}\\HTML\\chrome\\Chrome.html")
        os.rename(f"{root}\\HTML\\firefox\\complete.html",
                  f"{root}\\HTML\\firefox\\Firefox.html")
        os.rename(f"{root}\\HTML\\edge\\complete.html",
                  f"{root}\\HTML\\edge\\Edge.html")


def wait_for_file(file_path, timeout=120):
    start_time = time.time()
    while time.time() - start_time < timeout:
        if os.path.exists(file_path):
            return True
        time.sleep(1)
    return False


def run_send_message():
    pass


def delete_folders():
    time.sleep(2)
    root = os.getcwd()
    if wait_for_file(f"{root}\\Allure"):
        shutil.rmtree(f"{root}\\Allure")
        shutil.rmtree(f"{root}\\Reports")


start_execution()
run_allure_combine()
run_allure_rename()
run_send_message()
delete_folders()
