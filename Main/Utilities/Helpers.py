# Here will be auto Allure report generator method and Telegram message sender
import os
import shutil
import subprocess
import time
import telebot


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
        sys_browser = "Edge" if os.name == 'nt' else "Safari"
        subprocess.run(
            f'allure-combine Allure\\{sys_browser}\\{sys_browser}_report --dest {root}\\HTML\\{sys_browser} '
            f'--auto-create-folders',
            shell=True)


def run_allure_rename():
    root = os.getcwd()
    if wait_for_file(f"{root}\\HTML\\chrome\\complete.html"):
        os.rename(f"{root}\\HTML\\chrome\\complete.html",
                  f"{root}\\HTML\\chrome\\Chrome.html")
        os.rename(f"{root}\\HTML\\firefox\\complete.html",
                  f"{root}\\HTML\\firefox\\Firefox.html")
        sys_browser = "Edge" if os.name == 'nt' else "Safari"
        os.rename(f"{root}\\HTML\\{sys_browser.lower()}\\complete.html",
                  f"{root}\\HTML\\{sys_browser.lower()}\\{sys_browser}.html")

def wait_for_file(file_path, timeout=120):
    start_time = time.time()
    while time.time() - start_time < timeout:
        if os.path.exists(file_path):
            return True
        time.sleep(1)
    return False


def send_reports():
    butler = '7438234940:AAHllO2wm56vUpuw14RrXXpwTMbP_FTLP_I'
    chat_id = '6397942332'
    tb = telebot.TeleBot(butler)
    root = os.getcwd()
    with open(f"{root}\\HTML\\Chrome\\Chrome.html", "rb") as file:
        tb.send_document(chat_id, file)
    with open(f"{root}\\HTML\\Firefox\\Firefox.html", "rb") as file:
        tb.send_document(chat_id, file)
    if os.name == 'nt':
        with open(f"{root}\\HTML\\Edge\\Edge.html", "rb") as file:
            tb.send_document(chat_id, file)
    else:
        with open(f"{root}\\HTML\\Safari\\Safari.html", "rb") as file:
            tb.send_document(chat_id, file)


def delete_folders():
    time.sleep(2)
    root = os.getcwd()
    if wait_for_file(f"{root}\\Allure"):
        shutil.rmtree(f"{root}\\Allure")
        shutil.rmtree(f"{root}\\Reports")


def generate_report(driver):
    run_allure_generate(driver)


def run_allure_generate(browser):
    results_path = f"Reports/{browser}/{browser}_report/"
    report_path = f"Allure/{browser}/{browser}_report"
    command = f"allure generate {results_path} -o {report_path} --clean"
    subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
