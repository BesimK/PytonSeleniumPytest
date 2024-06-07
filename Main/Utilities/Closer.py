# import asyncio
import subprocess
import time
from allure_combine import combine_allure


# import time
#
# import requests
#
#
# async def send_telegram_message(token, recipient, report_path):
#     """
#     Send a message to a Telegram user using a bot.
#
#     :param token: The token of the Telegram bot.
#     :param recipient: The chat ID of the recipient.
#     :param report_path: The path to report to send.
#     """
#     # bot = Bot(token=token)
#     url = f"https://api.telegram.org/bot{token}/sendMessage"
#     with open(report_path, 'r', encoding='utf-8') as file:
#         html_content = file.read()
#
#     await bot.send_message(chat_id=recipient, text=html_content, parse_mode='HTML')
#     await asyncio.sleep(5)
#
#
# bot_token = '7438234940:AAHllO2wm56vUpuw14RrXXpwTMbP_FTLP_I'
# chat_id = '6397942332'
# path = "C:\\Users\\Dell\\Python Workspace\\PytonSeleniumPytest\\allure-report\\complete.html"
#
#
# asyncio.run(send_telegram_message(bot_token, chat_id, path))
#
#
# def get_user_id(token):
#     url = f"https://api.telegram.org/bot{token}/getUpdates"
#     response = requests.get(url)
#     print(response.json())
#

def generate_report(driver):
    run_allure_generate(driver)


def run_allure_generate(browser):
    results_path = f"Reports/{browser}/{browser}_report/"
    report_path = f"Allure/{browser}/{browser}_report"
    command = f"allure generate {results_path} -o {report_path} --clean"
    subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


# def run_allure_combine(browser):
#     results_path = f"Allure/{browser}/{browser}_report/"
#     report_path = f"HTML/{browser}/{browser}_report"
#     deleted = " --dest {report_path} --auto-create-folders"
#     command = f"allure-combine {results_path}"
#     subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def send_report():
    pass
