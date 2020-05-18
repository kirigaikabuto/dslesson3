phonebook=[]
e1={"name":"alibek","phone":92384}
e2={"name":"aydos","phone":92384}
e3={"name":"zhan","phone":92384}
phonebook.append(e1),
phonebook.append(e2),
phonebook.append(e3),
print(phonebook)
askname=""
askname=input("--> name?")

for i in phonebook:
    if i["name"]==askname:
        print(i["phone"])