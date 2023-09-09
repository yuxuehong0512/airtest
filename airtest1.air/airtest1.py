# -*- encoding=utf8 -*-
__author__ = "yuxuehong"

from airtest.core.api import *

from poco.drivers.android.uiautomation import AndroidUiautomationPoco

auto_setup(__file__)

poco = AndroidUiautomationPoco()

app = "com.zhao.myreader"

start_app(app) #启动app

poco(text="书城").click()
poco("com.zhao.myreader:id/iv_search").click()
poco("com.zhao.myreader:id/et_search_key").click()
text("大佬")
poco("com.zhao.myreader:id/tv_search_conform").click()
poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("android:id/content").child("android.widget.RelativeLayout").offspring("android.widget.ImageView").click()
stop_app(app)