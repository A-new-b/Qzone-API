import requests

import qzone

import config

from urllib.parse import urlencode


class Qzone_send(qzone.Qzone):

    def __init__(self):
        super(Qzone_send, self).__init__(**qzone.get_cookie_from_curl(config.cookie_curl))

    def emotion_send(self, context):
        url = "https://user.qzone.qq.com/proxy/domain/taotao.qzone.qq.com/cgi-bin/emotion_cgi_publish_v6"
        headers = config.publish_headers
        g_tk = self.gtk
        cookie = qzone.qzone_cookie

        params = {
            'g_tk': str(g_tk),
        }
        msg_dict = {
            "qzreferrer": "https://user.qzone.qq.com/" + config.account,
            "syn_tweet_verson": 1,
            "paramstr": 1,
            "pic_template": None,
            "richtype": None,
            "richval": None,
            "special_url": None,
            "who": 1,
            "con": context,
            "feedversion": 1,
            "ver": 1,
            "ugc_right": 1,
            "to_sign": 0,
            "hostuin": config.account,
            "code_version": 1,
            "format": "fs"
        }
        data = urlencode(msg_dict)
        data=data.replace("None","")

        response = requests.post(url=url, params=params, cookies=cookie, headers=headers, data=data, verify=False)

        print(response.text)


if __name__ == "__main__":
    mySend = Qzone_send()
    mySend.emotion_send("hello，各位朋友好，这里是白猫三号机，这是一条从python上发出的消息")
