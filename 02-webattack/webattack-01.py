import mechanize


br = mechanize.Browser()
br.open("https://afeladat2017.whiteshield.net/login")
br.select_form(nr=0)

for form in br.forms():
    print("Form name:", form.name)
    print(form)


br.form['username']="admin"
br.form['password']="admin"

req = br.submit()

print(req)