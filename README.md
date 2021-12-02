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
