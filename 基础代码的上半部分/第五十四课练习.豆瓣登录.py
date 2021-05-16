import re
import urllib,urllib2,cookielib
loginurl='https://www.douban.com/accounts/login'
cookie=cookielib.CookieJar()
opener=urllib2.bulid_opener(urllib2.HTTPCookieProcessor(cookie))
params={
    'form_email':'your email',
    'form_password':'you password'
    'source':'index_nav'
}#没有登录就不成功
#从首页提交登录
response=opener.open(loginurl,urllib.urlencode(params))
#验证成功跳转至登录页
if response.geturl="https://www.douban.com/accounts/login":
    html=response.read()
    #验证码图片地址
    imgurl=re.search('<img id="captcha_img"src="(.+?)"alt="captcha" class="captcha_image"/>',html)
    if imgurl:
        url=imgurl.group(1)
        #将验证码图片保存在目录下
        res=urllib.request.urlretrieve(url,'v.jpg')
        #获取captcha-id的参数
        captcha=re.search('<input type="hidden" name="captcha-id" value="(.+?)"/>',html)
        if captcha:
            vcode=raw_input('请输入图片上的验证码')
            data["captcha-solution"]=vcode
            data["captcha-id"]=captcha.group(1)
            data["user_login"]="  登录"
            #提交验证码验证
            response=opener.open(loginurl,urllib.parse.urlencode(data).encode('utf-8'))
            #登录成功跳转至首页
            if response.geturl()=="http://www.douban.com/":
                print('登录成功！')