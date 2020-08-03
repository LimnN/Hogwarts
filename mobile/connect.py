from appium import webdriver
import os

ANDROID_BASE_CAPS = {
    'app': os.path.abspath('../app/wework_v3.0.24.apk'),
    'automationName': 'UIAutomator2',
    'platformName': 'Android',
    'platformVersion': os.getenv('ANDROID_PLATFORM_VERSION') or '11.0',
        'deviceName': os.getenv('ANDROID_DEVICE_VERSION') or '192.168.0.103:5555',
    'noReset': True
}

EXECUTOR = 'http://127.0.0.1:4723/wd/hub'

driver = webdriver.Remote(command_executor=EXECUTOR, desired_capabilities=ANDROID_BASE_CAPS)
