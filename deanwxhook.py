import requests
import json
import time

headers = {"Content-Type": "application/json"}


class HttpClient:

    def __init__(self, ip, port, debuggingwxid):
        """
        :param ip: ip
        :param port: 端口
        :param debuggingwxid: 调试用wxid，使用方法时，如果不对towxid传参，则默认发消息到此wxid
        """
        self.host = ip
        self.port = port
        self.debuggingwxid = debuggingwxid
        self.url = f"http://{ip}:{port}/DaenWxHook/client/"

    def sendText(self, msg: str, towxid: str = None, ):
        """
        发送文本消息
        :param towxid: 消息接收人的wxid，为空时使用debuggingwxid
        :param msg: 文本
        :return:
        """
        if towxid is None:
            towxid = self.debuggingwxid
        data = {
            "type": "Q0001",
            "data": {
                "wxid": towxid,
                "msg":  msg.replace("\n", "\r")
            }
        }
        res = requests.post(url=self.url, data=json.dumps(data, ensure_ascii=False).encode('utf-8'), headers=headers)
        return res.text

    def sendImage(self, path: str, towxid: str = None):
        """
        发送图片消息
        :param towxid: 消息接收人的wxid，为空时使用debuggingwxid
        :param path: 图片链接，可为本地地址或url
        :return:
        """
        if towxid is None:
            towxid = self.debuggingwxid
        data = {
            "type": "Q0010",
            "data": {
                "wxid": towxid,
                "path": path
            }
        }
        res = requests.post(url=self.url, data=json.dumps(data, ensure_ascii=False).encode('utf-8'), headers=headers)
        return res.text

    def sendFile(self, path: str, towxid: str = None):
        """
        发送文件消息
        :param towxid: 消息接收人的wxid，为空时使用debuggingwxid
        :param path: 文件链接，可为本地地址或url
        :return:
        """
        if towxid is None:
            towxid = self.debuggingwxid
        data = {
            "type": "Q0011",
            "data": {
                "wxid": towxid,
                "path": path
            }
        }
        res = requests.post(url=self.url, data=json.dumps(data, ensure_ascii=False).encode('utf-8'), headers=headers)
        return res.text

    def sendSong(self, name: str, author: str = None, jumpUrl: str = None, musicUrl: str = None, imageUrl: str = None,
                 app: str = "wx8dd6ecd81906fd84", towxid: str = None):
        """
        发送音乐分享
        :param name: 歌曲名
        :param author: 作者名
        :param jumpUrl: 点击时跳转页面
        :param musicUrl: 直接播放使用的媒体流链接
        :param imageUrl: 缩略图链接
        :param app: 应用id，默认为网易云音乐
        :param towxid: 消息接收人的wxid，为空时使用debuggingwxid
        :return:
        """
        if towxid is None:
            towxid = self.debuggingwxid
        data = {
            "type": "Q0014",
            "data": {
                "wxid":     towxid,
                "name":     name,
                "author":   author,
                "app":      app,
                "jumpUrl":  jumpUrl,
                "musicUrl": musicUrl,
                "imageUrl": imageUrl

            }
        }
        res = requests.post(url=self.url, data=json.dumps(data, ensure_ascii=False).encode('utf-8'), headers=headers)
        return res.text

    def sendXml(
            self,
            xml: str,
            towxid: str = None,
    ):
        """
        发送XML代码
        :param xml: XML代码
        :param towxid: 消息接收人的wxid，为空时使用debuggingwxid
        :return:
        """
        if towxid is None:
            towxid = self.debuggingwxid
        data = {
            "type": "Q0015",
            "data": {
                "wxid": towxid,
                "xml":  xml
            }
        }
        res = requests.post(url=self.url, data=json.dumps(data, ensure_ascii=False).encode('utf-8'), headers=headers)
        return res.text

    def sendList(
            self,
            title: str,
            contents: list,
            timestamp=time.time(),
            towxid: str = None,
    ):
        """
        利用聊天记录样式，发送一个列表
        :param title: 标题，仅部分情况生效
        :param contents: 列表内容，每行均为字符串。
        :param timestamp: 所有项目统一显示的时间戳。
        :param towxid: 消息接收人的wxid，为空时使用debuggingwxid
        :return:
        """
        if towxid is None:
            towxid = self.debuggingwxid
        datalist = []
        for key in contents:
            row = {
                "wxid":      "",
                "nickName":  "",
                "timestamp": int(timestamp),
                "msg":       str(key)
            }
            datalist.append(row)

        data = {
            "type": "Q0009",
            "data": {
                "wxid":     towxid,
                "title":    title,
                "dataList": datalist
            }
        }
        res = requests.post(url=self.url, data=json.dumps(data, ensure_ascii=False).encode('utf-8'), headers=headers)
        return res.text

    # 发送链接
    def sendUrl(
            self,
            title: str,
            content: str,
            jumpurl: str = None,
            app: str = None,
            path: str = None,
            towxid=None

    ):
        """
        发送分享链接卡片
        :param title: 标题，最多显示两行
        :param content: 链接的内容，最多显示三行
        :param jumpurl: 跳转链接
        :param app: 应用ID
        :param path: 缩略图
        :param towxid: 消息接收人的wxid，为空时使用debuggingwxid
        :return:
        """
        if towxid is None:
            towxid = self.debuggingwxid
        data = {
            "type": "Q0012",
            "data": {
                "wxid":    towxid,
                "title":   title,
                "content": content,
                "jumpUrl": jumpurl,
                "app":     app,
                "path":    path
            }
        }
        res = requests.post(url=self.url, data=json.dumps(data, ensure_ascii=False).encode('utf-8'), headers=headers)
        return res.text
