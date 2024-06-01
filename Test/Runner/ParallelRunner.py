# import os
# import subprocess
# from concurrent.futures import ThreadPoolExecutor
#
#
# def run_tests(browser):
#     env = os.environ.copy()
#     env['BROWSER'] = browser
#     allure_dir = f"reports/allure/{browser}"
#     subprocess.run(["behave", "--tags=@your_tag", "-f", "allure_behave.formatter:AllureFormatter", "-o", allure_dir],
#                    env=env)
#
#
# browsers = ["chrome", "firefox", "edge"]
#
# with ThreadPoolExecutor(max_workers=len(browsers)) as executor:
#     executor.map(run_tests, browsers)
