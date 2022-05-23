print("\t Welcome to Computer bhhhh..");
print("\nlogin(L)\nregister(R)\nedit details(E)\nexit(e)")
ch=input("Select ypur choice:")
if ch=='L':
  name=input("\t user name=")
  password=input("\t password=")
  if name=="basha" and password=="basha" :
    print("Login successful for basha")
    king=input("\n1.work\n2.Sleep\n Enter your choice:")
    if king=='w':
      print("Work place is being ready for u, Get started please...");
    elif king=='s':
      print("go for sleep...")
  elif name=="bhanu" and password=="bhanu" :
      print("Login successful by BHANU")
  else:
      print("ERROR...!")
elif ch=='R':
  b=18
  age=int(input("Enter Your age:"))
  if age >= b:
    name1=input("Enter your name:")
    usname=input("Create username:")
    pass1=input("Create password:")
    print(name1,usname,pass1)
  else:
    print("Your are not eligible...'SORRY'")