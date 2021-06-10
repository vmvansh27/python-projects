import random
f=open("passwords.txt","a")
lowercase="qwertyuioplkjhgfdsazxcvbnm"
uppercase="QWERTYUIOPLKJHGFDSAZXCVBNM"
num="1234567890"
symbols=",./@*_"
all=lowercase+uppercase+num+symbols
length=int(input("Enter the length of the password: "))
password="".join(random.sample(all,length))
print(password)
f.write("\n"+password)
f.close()
