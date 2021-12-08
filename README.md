# qiye_weixin_health_check

南京邮电大学企业微信健康打卡脚本

## 环境

Python2

## 使用

1. 使用前请先安装`hackhttp`库

    ```sh
    pip2 install hackhttp
    ```

2. 添加你的企业微信cookie（因为考虑到多人使用，所以使用了dict，可以添加多个cookie，会遍历提交）
    先使用浏览器打开新的无痕窗口，访问：[https://doc.weixin.qq.com/disklogin/login_page](https://doc.weixin.qq.com/disklogin/login_page)，然后使用你登陆了南京邮电大学的**企业微信**（不是微信）扫码登陆

    登录后按F12打开开发者工具，或者在网页空白处右键点击“检查”，如下图：

    ![image](https://user-images.githubusercontent.com/66706544/144440784-d825f6ea-1657-470e-8fe5-ee94025789cd.png)
  
    然后在控制台(console)输入`document.cookie`查看当前cookie字符串：
  
    ![image](https://user-images.githubusercontent.com/66706544/144441988-90e30845-8a31-4c28-9751-1202047df99d.png)

    复制后粘贴到脚本中即可


3. 运行

    ```sh
    python2 auto_health_check.py
    ```

    脚本中使用了server酱进行通知，打卡成功或者失败都将通知到手机，<SENDKEY>需要自行替换，具体用法参考[https://sct.ftqq.com/](https://sct.ftqq.com/)，如果不需要，可以自行删除这部分代码

    ~~关于自动打卡，可以挂在服务器上设置定时任务运行，或者直接在代码中加sleep 24h。~~
    
    由于微文档的cookie只有一天有效期，无法持续自动打卡，所以去看了一下企业微信的授权认证方式，发现是通过传wwapp_cst、wwapp_deviceid等参数给服务端，服务端确认后才set-cookie
    
    ![1D52FDC01412243CF39B623B0AD37268](https://user-images.githubusercontent.com/66706544/145207955-43edaed3-3b32-4dd6-a8f0-ffb6825f7494.jpg)
    
    deviceid和vid是固定不变的，cst是客户端生成的，所以需要逆向企业微信看生成的算法，看能不能自己生成
    
    逆向ing...

    
