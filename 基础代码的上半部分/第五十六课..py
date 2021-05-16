import urllib.request
import os
import base64

def url_open(url):
    rep = urllib.request.Request(url)
    print(rep)
    rep.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362')
    response = urllib.request.urlopen(url)
    html=response.read()

    return html

def get_page(url):
    html=url_open(url).decode('utf-8')

    a=html.find('current-comment-page')+23
    b=html.find(']',a)
    print(html[a:b])
    return html[a:b]
def find_imgs(url):
    url_open(url).decode('utf-8')
    img_addrs=[]

    a = html.find('img src=')

    while a!=-1:
        b = html.find('.jpg',a,a+255)
        if b!=-1:
            img_addrs.append(html[a+9:b+4])
        else:
            b=a+9
        a=html.find("img src",b)
    return img_addrs

def save_imgs(folder,img_addrs):
    for each in img_addrs:
        filename= each.split('/')[-1]
        with open(filename,'wb') as f:
            img=open_url(each)
            f.write(img)

def download_mm(folder='OOXX',pages=10):
    os.mkdir(folder)
    os.chdir(folder)

    url="http://jandan.net/ooxx/"
    page_num=int(base64.b64decode(get_page(url)).decode("utf-8"))


    for i in range(pages):
        page_num -= 1
        page_url=url+str(page_num)+'#comments'
        print(page_url)
        img_addrs=find_imgs(page_url)
        save_imgs(folder,img_addrs)

if __name__ == '__main__':
    download_mm()
