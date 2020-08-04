from appium import webdriver
import os


class Device(object):
    def __init__(self):
        ANDROID_BASE_CAPS = {
            # 'app': os.path.abspath('../app/wework_3_0_27.apk'),
            'automationName': 'UIAutomator2',
            'platformName': 'Android',
            'platformVersion': '11.0',
            'deviceName': '9A241FFBA00003',
            'appPackage': 'com.tencent.wework',
            'appActivity': '.launch.LaunchSplashActivity',
            'noReset': True,
            'skipServerInstallation': True,
            'skipDeviceInitialization': True
        }

        EXECUTOR = 'http://127.0.0.1:4723/wd/hub'

        self.driver = webdriver.Remote(command_executor=EXECUTOR, desired_capabilities=ANDROID_BASE_CAPS)
