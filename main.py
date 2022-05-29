import pymongo

client = pymongo.MongoClient("mongodb+srv://emil:emil@cluster0.a8cyb.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test#database name
records = db.guvi131#collection name
#
from typing import NamedTuple
import re
import string
import json

def check_phno(phno):
  s = phno
  if (len(s) == 10):
    return 1
  else:
     print("Invalid phno")
     return 0

def check_email(email):
   x = r'\b[A-Za-z0-9]+@[A-Za-z0-9.-]+.[A-Z|a-z]{2,}\b'
   if (re.fullmatch(x, email)):
     return 1
   else:
      print("Invalid Email")
      return 0

def check_name(name):
  #y = r'\b[A-Za-z]\b'
  #if (re.fullmatch(y, name)):
  if name.isalpha():
    return 1
  else:
    print("Please enter the name without numbers or special characters")
    return 0

def Register():
   e = 0
   u = 0
   p = 0
   n = input('Enter the name')
   e = check_name(n)
   pn = input('Enter the phno')
   p = check_phno(pn)
   email = input('Enter the email')
   u = check_email(email)
   if u == 1 and p == 1 and e == 1:
     global records
     records = db.guvi131
     dict1 = { "name" : n,
         "phonenumber" : pn,
         "email" : email, }
     records.insert_one(dict1)
     print("Phone number entered successfully")

def update():
  myquery = {"name":input("enter the name")}
  newvalues ={"$set": { "phonenumber": int(input("Enter the new phone number"))}}

  records.update_one(myquery,newvalues)
  print("The phone number has been updated")

def delete():
  myquery = {"name":input("enter the name")}
  records.delete_one(myquery)
  print("The phone number has been deleted")

def forgot_phno():
  global records
  key = input("enter the name")
  Query={"name":key}
  v = records.find(Query)
  for i in v:
   print(i)
 # for i in records.find({"name":key},{"_id":0, "name":1, "phonenumber":1, "email":1}):
    # print(key)



print("enter 0 to Create contact \n enter 1 to update contact \n enter 2 to delete contact ")
print("If you have forgotton your phno and wants to retrieve it please enter 3 ")
n = int(input())

if n == 0:
  Register()

elif n == 1:
  update()

elif n == 2:
  delete()

elif n==3:
  forgot_phno()