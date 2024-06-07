# This file is the Runner For Parallel Execution, Report Generation and Report Sending Automatically
from Main.Utilities import Helpers

Helpers.start_execution()
Helpers.run_allure_combine()
Helpers.run_allure_rename()
Helpers.send_reports()
Helpers.delete_folders()
