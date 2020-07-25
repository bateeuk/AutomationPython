from behave import *
from selenium.webdriver import Chrome
import time


@given(u'User open browser, enter URL and navigate to Free Car Check page')
def step_impl(context):
    path = 'D:\Selenium\chromedriver.exe'
    context.driver = Chrome(executable_path = path)
    context.driver.set_page_load_timeout(6)
    context.driver.maximize_window()
    context.driver.delete_all_cookies()
    context.driver.get("https://cartaxcheck.co.uk/")
    context.driver.refresh()
    context.driver.find_element_by_xpath('//h1[contains(text(),"Free Car Check")]')
    time.sleep(4)

@when(u'User clicks vehicle enquiry text field and enters "<REG Number>"')
def step_impl(context):
    context.driver.find_element_by_id("vrm-input").click()
    context.driver.find_element_by_id("vrm-input").clear()
    context.driver.find_element_by_css_selector("#vrm-input").send_keys("T29TEE")
    time.sleep(4)

@when(u'User selects the Free Car Check button')
def step_impl(context):
    context.driver.find_element_by_css_selector('[class="jsx-3655351943 "]').click()


@then(u'User is directed to the Vehicle Identity screen')
def step_impl(context):
    context.driver.get_screenshot_as_file("Vehicle Identity_1.png")
@then(u'User checks and logs down the vehicle details')
def step_impl(context):
    elementRs = "T29TEE"
    elementMs = "Mercedes-Benz"
    elementMos = "E 220 D Amg Line Auto"
    elementCs = "Silver"
    print(elementRs, elementMs, elementMos, elementCs)
    time.sleep(4)
    elementR = context.driver.find_element_by_xpath('//dd[contains(text(),"T29TEE")]')
    context.driver.find_element_by_xpath("//dd[contains(text(),'Mercedes-Benz')]")
    context.driver.find_element_by_xpath("//dd[contains(text(),'E 220 D Amg Line Auto')]")
    context.driver.find_element_by_xpath("//dd[contains(text(),'Silver')]")
    context.driver.find_element_by_xpath(
        '//div[contains(@class,"jsx-79705764")]//div[1]//div[1]//span[1]//div[2]//dl[5]//dd[1]')
    print("Plate number" + str(elementR))
    time.sleep(30)

@then(u'User navigates back to the Free Car Check page')
def step_impl(context):
    context.driver.back()
    time.sleep(4)
    context.driver.get_screenshot_as_file("Vehicle Identity_2.png")
    context.driver.close()











