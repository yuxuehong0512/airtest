# author_='Yuxuehong';
# date: 2023/9/10 22:11
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco()
auto_setup(__file__)

app = "com.zhao.myreader"
start_app(app)
v = Template(r"img/tpl1650378187363.png", record_pos=(0.006, 0.094), resolution=(1080, 2340))
wait(v=v)
touch(Template(r"img/tpl1650378306243.png", record_pos=(0.126, -0.926), resolution=(1080, 2340)))
exists(Template(r"img/tpl1650378336382.png", record_pos=(0.15, -0.742), resolution=(1080, 2340)))
touch(Template(r"img/tpl1650378359838.png", threshold=0.5, record_pos=(0.144, -0.459), resolution=(1080, 2340)))
snapshot(filename="img/截图.png", msg="请填写测试点.")
assert_exists(Template(r"img/tpl1650378433234.png", threshold=0.5, record_pos=(0.258, 1.021), resolution=(1080, 2340)),
              "请填写测试点")
touch(Template(r"img/tpl1650378501376.png", record_pos=(-0.428, -0.927), resolution=(1080, 2340)))
swipe(Template(r"img/tpl1650378521739.png", record_pos=(-0.332, -0.006), resolution=(1080, 2340)),
      vector=[0.6875, 0.0063])
sleep(1)
assert_not_exists(Template(r"img/tpl1650378604254.png", record_pos=(-0.085, -0.45), resolution=(1080, 2340)), "请填写测试点")
touch(Template(r"img/tpl1650378645761.png", threshold=0.7, rgb=False, record_pos=(0.425, -0.923),
               resolution=(1080, 2340)))
touch(Template(r"img/tpl1650378666127.png", record_pos=(-0.318, -0.805), resolution=(1080, 2340)))
text("大佬")
touch(Template(r"img/tpl1650378717035.png", record_pos=(0.369, -0.809), resolution=(1080, 2340)))
assert_exists(Template(r"img/tpl1650378822541.png", record_pos=(0.008, -0.343), resolution=(1080, 2340)), "请填写测试点")
#
stop_app(app)