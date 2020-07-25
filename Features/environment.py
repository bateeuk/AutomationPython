from behave import *
from selenium.webdriver import Chrome


def before_all(context):
    path = 'D:\\Selenium\\chromedriver.exe'
    context.driver = Chrome(executable_path = path)

def after_all(context):
    context.driver.close()
