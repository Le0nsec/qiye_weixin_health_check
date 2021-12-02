# coding=UTF-8
# Python2
# Author: Leon
# Github: https://github.com/Le0nsec/qiye_weixin_health_check

import json
import time
import hackhttp

hh = hackhttp.hackhttp()

cookie_dict = {
    "xxx":"wedrive_uin=xxx; wedrive_sid=xxxxx; etc.",
    "ccc":"",

    }

def get_health_form_list(name, cookie):
    raw = '''
GET /form/healthformlist HTTP/1.1
Host: doc.weixin.qq.com
Connection: close
Pragma: no-cache
Cache-Control: no-cache
sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "macOS"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7
Cookie: %s
'''
    try:
        code, head, html, redirect, log = hh.http('https://doc.weixin.qq.com/form/healthformlist', raw = raw % (cookie))
        if code != 200:
            raise Exception("/form/healthformlist status_code not 200")
        json_result = json.loads(html)
        if json_result["head"]["ret"] == -20002:
            raise Exception(name + ": login state expire")
        form_id = json_result["body"]["form_items"][1]["form_id"]
    except Exception as e:
        print("[!] " + str(e))
        call_server_chan(False, name + ": may be login state expire?%0a%0d" + html)
        exit()
    return str(form_id)


def post_health_form(form_id, name, cookie):
    raw = '''POST /form/share?f=json HTTP/1.1
Host: doc.weixin.qq.com
Content-Type: multipart/form-data; boundary=----WebKitFormBoundarynFnLeYS3a4cZQr7B
Origin: https://doc.weixin.qq.com
Accept-Encoding: gzip, deflate
Cookie: %s
Connection: close
Accept: application/json, text/plain, */*
User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 15_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko)  Mobile/15E148 wxwork/3.1.18 MicroMessenger/7.0.1 Language/zh ColorScheme/Light
Referer: https://doc.weixin.qq.com/
Content-Length: 1657
Accept-Language: zh-CN,zh-Hans;q=0.9

------WebKitFormBoundarynFnLeYS3a4cZQr7B
Content-Disposition: form-data; name="type"

2
------WebKitFormBoundarynFnLeYS3a4cZQr7B
Content-Disposition: form-data; name="form_id"

%s
------WebKitFormBoundarynFnLeYS3a4cZQr7B
Content-Disposition: form-data; name="form_reply"

{\"items\":[{\"question_id\":1,\"text_reply\":\"{\\\"type\\\":\\\"\\\",\\\"nation\\\":\\\"\xe4\xb8\xad\xe5\x9b\xbd\\\",\\\"province\\\":\\\"\xe6\xb1\x9f\xe8\x8b\x8f\xe7\x9c\x81\\\",\\\"city\\\":\\\"\xe5\x8d\x97\xe4\xba\xac\xe5\xb8\x82\\\",\\\"district\\\":\\\"\xe6\xa0\x96\xe9\x9c\x9e\xe5\x8c\xba\\\",\\\"addr\\\":\\\"\xe6\xb1\x9f\xe8\x8b\x8f\xe7\x9c\x81\xe5\x8d\x97\xe4\xba\xac\xe5\xb8\x82\xe5\x8d\x97\xe4\xba\xac\xe9\x82\xae\xe7\x94\xb5\xe5\xa4\xa7\xe5\xad\xa6(\xe4\xbb\x99\xe6\x9e\x97\xe6\xa0\xa1\xe5\x8c\xba)\\\",\\\"lat\\\":32.1126594543457,\\\"lng\\\":118.93416595458984,\\\"module\\\":\\\"wework-native\\\",\\\"exportText\\\":\\\"\xe6\xb1\x9f\xe8\x8b\x8f\xe7\x9c\x81\xe5\x8d\x97\xe4\xba\xac\xe5\xb8\x82\xe5\x8d\x97\xe4\xba\xac\xe9\x82\xae\xe7\x94\xb5\xe5\xa4\xa7\xe5\xad\xa6(\xe4\xbb\x99\xe6\x9e\x97\xe6\xa0\xa1\xe5\x8c\xba)\\\"}\",\"option_reply\":[]},{\"question_id\":2,\"text_reply\":\"\",\"option_reply\":[\"1\"]},{\"question_id\":3,\"text_reply\":\"\",\"option_reply\":[\"2\"]},{\"question_id\":4,\"text_reply\":\"\",\"option_reply\":[\"2\"]},{\"question_id\":6,\"text_reply\":\"\",\"option_reply\":[\"2\"]},{\"question_id\":7,\"text_reply\":\"\",\"option_reply\":[\"1\"]},{\"question_id\":8,\"text_reply\":\"\",\"option_reply\":[\"5\"]},{\"question_id\":9,\"text_reply\":\"\",\"option_reply\":[\"2\"]},{\"question_id\":10,\"text_reply\":\"\",\"option_reply\":[\"3\"]},{\"question_id\":11,\"text_reply\":\"\",\"option_reply\":[\"3\"]},{\"question_id\":12,\"text_reply\":\"\",\"option_reply\":[]},{\"question_id\":13,\"text_reply\":\"\",\"option_reply\":[]}]}
------WebKitFormBoundarynFnLeYS3a4cZQr7B
Content-Disposition: form-data; name="f"

json
------WebKitFormBoundarynFnLeYS3a4cZQr7B
Content-Disposition: form-data; name="source"


------WebKitFormBoundarynFnLeYS3a4cZQr7B
Content-Disposition: form-data; name="vcode"

null
------WebKitFormBoundarynFnLeYS3a4cZQr7B--

'''
    try:
        code, head, html, redirect, log = hh.http('https://doc.weixin.qq.com/form/share?f=json', raw = raw % (cookie, form_id))
        # print(html)
        if "is_school_corp" in html and "32.1126594543457" in html:
            call_server_chan(True, name + ": submit success!")
            print("[*] [" + name + "] submit success!")
            return
        elif "32.1126594543457" in html:
            call_server_chan(False, name + ": may be already submitted...%0a%0d" + html)
            return
        else:
            call_server_chan(False, name + ": something error...%0a%0d" + html)
            return
    except Exception as e:
        print("[!] " + str(e))
        call_server_chan(False, name + ": net error?%0a%0d" + html)
        exit()

# https://sct.ftqq.com/
def call_server_chan(submit_status, result_html):
    if submit_status == True:
        title = "健康上报成功~"
    elif submit_status == False:
        title = "健康上报失败!!!"
    try:
        code, head, body, redirect, log = hh.http('https://sctapi.ftqq.com/<SENDKEY>.send', post = "title={}&desp={}".format(title, result_html))
        print("[*] call server chan: " + body)
        return
    except Exception as e:
        print("[!] " + str(e))
        exit()


if __name__ == "__main__":
    for name, cookie in cookie_dict.items():
        form_id = get_health_form_list(name, cookie)
        print("[*] %15s form id: %s"%(name, form_id))
        time.sleep(0.1)
        post_health_form(form_id, name, cookie)
        time.sleep(0.5)