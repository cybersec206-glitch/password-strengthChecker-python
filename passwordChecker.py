password = input("enter your password: ")


score=0
feedback =[]
#check length
def check_length(password):
    return len(password)>=8
        
    
if check_length(password):
    print("good length")
    score += 1
else:
    feedback.append("Use at least 8 characters")


#check for uppercase
def check_uppercase(password):
    return any(char.isupper() for char in password)
       
if check_uppercase(password):
    print("contains uppercase")
    score += 1
else:
    feedback.append("Add an uppercase letter")
    

    
#check for lowercase
def check_lowercase(password):
    return any(char.islower() for char in password)
      
if check_lowercase(password):
    print("contains lowercase")
    score += 1
else:
     feedback.append("Add a lowercase letter")


#check for digest
def check_digit(password):
    return any(char.isdigit() for char in password)
     
if check_digit(password):
    print("contains digit")
    score += 1
else:
    feedback.append("Add a digit")

     

#check for special character
def check_special(password):
   return any(char in"!@#$%^&*" for char in password)
     
if check_special(password):
    print("contains special character")
    score += 1
else:
    feedback.append("Add a special character")
    

print("\n"+ "=" *30)
print("PASSWORD SECURITY REPORT")
print("="*30)

if score<=2:
    print("weak password")
elif score <=4:
    print("medium password")
else:
    print("strong password")

if feedback:
    print("\nSuggestions:")
    for suggestion in feedback:
        print("-",suggestion)

