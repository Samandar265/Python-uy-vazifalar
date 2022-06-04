import random as r

length=int(input("Password length: "))
letters="ABCDEFGHIJKLMNOPQRTUVWXYZabcdefghijklmnopqrtsuvwxyz0123456789!@#$%^&*()_-+<>?"
password="".join(r.sample(letters,length))

print(password)