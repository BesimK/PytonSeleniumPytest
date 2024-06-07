# import asyncio
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
#
#     # Read the HTML content from the file
#     try:
#         with open(report_path, 'r', encoding='utf-8') as file:
#             html_content = str(file.read())
#     except Exception as e:
#         print(f"Error reading HTML file: {e}")
#         return
#     html_content = "<html><body>Wololo</body></html>"
#     await asyncio.wait_for(bot.send_message(chat_id=recipient, text=html_content), timeout=120)
#
#     # # Send the HTML content as a message
#     # try:
#     #     await asyncio.wait_for(
#     #         bot.send_message(chat_id=recipient, text=html_content),
#     #         timeout=120
#     #     )
#     #     print('HTML report sent successfully as a message.')
#     # except (TelegramError, asyncio.TimeoutError) as e:
#     #     print(f'Failed to send message. Error: {e}')
#
#
# def get_user_id(token):
#     url = f"https://api.telegram.org/bot{token}/getUpdates"
#     response = requests.get(url)
#     print(response.json())
#
#
# # Your bot token and chat ID
# bot_token = '7438234940:AAHllO2wm56vUpuw14RrXXpwTMbP_FTLP_I'
# chat_id = '6397942332'
# path = "C:\\Users\\Dell\\Python Workspace\\PytonSeleniumPytest\\allure-report\\complete.html"
#
# # Run the async function
# asyncio.run(send_telegram_message(bot_token, chat_id, path))
