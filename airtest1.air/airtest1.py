# -*- encoding=utf8 -*-
__author__ = "yuxuehong"

from airtest.core.api import *

from poco.drivers.android.uiautomation import AndroidUiautomationPoco

auto_setup(__file__)

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

app = "com.zhao.myreader"

start_app(app) #启动app

poco(text="书城").click()
