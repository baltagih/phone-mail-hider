print("Type 'quit' to exit")
pore = "not"
answers = ["e","E","p","P","quit"]
char = ["+","-"]
mail = []
num = []
atcount = 0
restmail = ""
restnum = ""
finalnum = ""

while pore not in answers:
    pore = str(raw_input("Phone or Email? (P/E): "))
    if pore == "e" or pore == "E":
        email = str(raw_input("Enter the email address: "))
        for ch in email:
            mail.append(ch)
        if "@" not in mail:
            print("Please enter a valid email address")
            exit()
        for tryi in mail:
            if(tryi == "@"):
                break
            else:
                atcount += 1;
        for i in range(atcount+1,len(mail)):
            restmail += str(mail[i])
        print(mail[0]+"*****"+mail[atcount-1]+"@"+restmail)
    elif pore == "p" or pore == "P":
        phone = str(raw_input("Enter the phone number: "))
        for ch in phone:
            num.append(ch)
        for n in num[-4:]:
            restnum += str(n)
        for tri in num:
            if tri not in char:
                finalnum += "*"
            else:
                finalnum += str(tri)
        print(finalnum[:-4]+restnum)


    elif pore == "quit":
        exit()
