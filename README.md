# WxHookPythonSDK
为DeanWxHook提供python调用模块，兼容千寻框架

## 安装
pip install https://github.com/sqkkyzx/WxHookPythonSDK/raw/main/dist/deanwxhook-1.1.tar.gz

## 使用
```
import deanwxhook

# 新建一个wxbot实例
# ip – ip
# port – 端口，非千寻http端口，需要使用微信启动端口
# debuggingwxid – 调试用wxid，使用任一方法时，如果不对towxid传参，则默认发消息到此wxid

wxbot = deanwxhook.HttpClient(
  ip="127.0.0.1", 
  port="8056", 
  debuggingwxid="wxid_00000000000000"
)

# 发送图片消息
wxbot.sendImage(towxid="00000000000@chatroom", path="c:/0000/00000/00000.png")

# 发送文本消息
wxbot.sendText(towxid="00000000000@chatroom", msg="000000000")

# 其他方法请自行调用查看
```
