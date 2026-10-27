password = input("Enter your password: ")

if len(password) < 8:
  print("Weak Password")

elif not any(char.isdigit() for char in password):
   print("Add at least one number")

elif not any(char.isupper() for char in password):
   print("Add at least one capital letter")

else:
   print("Strong Password")
   