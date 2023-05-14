from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
import time

def run_automation(input_value):
    # set up appium
    caps = {}
    caps["platformName"] = "Android"
    caps["appium:platformVersion"] = "13"
    caps["appium:deviceName"] = "sdk_gphone64_arm64"
    caps["appium:automation"] = "UiAutomator2"
    caps["appium:appPackage"] = "bot.touchkin"
    caps["appium:appActivity"] = "bot.touchkin.ui.InstantSplash"
    caps["appium:ensureWebviewsHavePages"] = True
    caps["appium:nativeWebScreenshot"] = True
    caps["appium:newCommandTimeout"] = 3600
    caps["appium:connectHardwareKeyboard"] = True

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

    # set up explicit wait
    wait = WebDriverWait(driver, 20)

    # find elements and perform actions
    try:
        # wait for element to be clickable
        el1 = wait.until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Next")))
        el1.click()

        # wait for element to be visible
        el2 = wait.until(EC.visibility_of_element_located((MobileBy.ID, "bot.touchkin:id/anEditText")))
        el2.send_keys("Tester")

        # wait for element to be clickable
        el3 = wait.until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Submit nickname")))
        el3.click()

        # wait for element to be visible
        el4 = wait.until(EC.visibility_of_element_located((MobileBy.ID, "bot.touchkin:id/textView")))
        el4.click()

        # wait for element to be clickable
        el5 = wait.until(EC.element_to_be_clickable((MobileBy.ID, "bot.touchkin:id/spaceButton")))
        el5.click()

        # wait for element to be clickable
        el6 = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, "//android.widget.FrameLayout[@content-desc=\"I would work with a coach if it was affordable\"]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ImageView[1]")))
        el6.click()

        # wait for element to be clickable
        el7 = wait.until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Close")))
        el7.click()

        # wait for element to be clickable
        el8 = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, "//android.widget.LinearLayout[@content-desc=\"Talk\"]/android.widget.ImageView")))
        el8.click()

        time.sleep(5)
        # perform action with ActionChains
        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(534, 1437)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(522, 1534)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        time.sleep(5)

        # wait for element to be clickable
        el9 = wait.until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Kinda like this👆")))
        el9.click()

        # wait for element to be visible
        el10 = wait.until(EC.visibility_of_element_located((MobileBy.ACCESSIBILITY_ID, "Reply or say help…")))
        el10.send_keys(input_value)

        # wait for element to be clickable
        el11 = wait.until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Send")))
        el11.click()
        
        time.sleep(15)

        elements = driver.find_elements(by=MobileBy.ANDROID_UIAUTOMATOR, 
                                        value='new UiSelector().resourceId("bot.touchkin:id/message")')
        
        output = []
        flag=True
        for element in elements:
            if(element.get_attribute('text')==input_value and flag==True):
                flag=False
            elif(flag==False):
                output.append(element.get_attribute('text'))
        
    finally:
        # close the app session
        driver.quit()

    return output