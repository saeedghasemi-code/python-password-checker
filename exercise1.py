
# input username and password
while True:
    user_name = input("Please enter your user name: ")

    if user_name:
        break

    elif not user_name:
        print("Username cannot be empty. please try again.")
    
        
while True:
    user_password = input("Please enter your password: ")

    if user_password:
        break
    elif not user_password:
        print("Password cannot be empty. please try again.")

print("")

print("Filter checks:")
score = 8
# Filter 1
if int(len(user_password)) < 8:
    score -= 1
    print("❌ 1.Password is shorter than 8 characters.")

else:
    
    print("✅ 1.Password length is sufficient.")


# Filter 2
has_letter = False
for letter in user_password:
    if letter.isalpha():
        has_letter = True
        break
if has_letter == True:
    print("✅ 2.Contains at least one English letters.")
elif has_letter == False:
    score -= 1
    print("❌ 2.Password does not contain any English letters.")



# Filter 3
has_special = False
special_chars = "!@$"
for letter in user_password:
    if letter in special_chars:
        has_special = True
        break
if has_special == True:
    print("✅ 3.Contains at least one special characters.")
elif has_special == False:
    score -= 1
    print("❌ 3.Password does not contain any special characters.")




# Filter 4
has_upper = False
for letter in user_password:
    if letter.isupper():
        has_upper = True
        break
if has_upper == True:
    print("✅ 4.Contains at least one uppercase letter.") 
else:
    score -= 1
    print("❌ 4.Password does not contain any uppercase letters.")




# Filter 5
if user_password == user_name:
    score -= 1
    print("❌ 5.Password is identical to the username.")
else:
    print("✅ 5.Not identical to the username.")




# Filter 6
swapcase_chars = user_name.swapcase()
if swapcase_chars == user_password:
    score -= 1
    print("❌ 6.Password is the swapcase version of the username.")
else:
    print("✅ 6.Not the swapcase version of the username.")




# Filter 7

special_user = user_name
special_user = special_user.replace("a", "@")
special_user = special_user.replace("A", "@")
special_user = special_user.replace("i", "!")
special_user = special_user.replace("I", "!")
special_user = special_user.replace("o", "0")
special_user = special_user.replace("O", "0")
special_user = special_user.replace("s", "$")
special_user = special_user.replace("S", "$")
if special_user == user_password:
    score -= 1
    print("❌ 7.Is a special-character version of the username(s -> $, a -> @).")

else:
    print("✅ 7.Not a special-character version of the username.")


# Filter 8
password_list = ["123456", "12345678", "12345", "111111", "123456789", "qwerty", "asdfgh", "zxcvbnm", "password", "admin", "P@s$w0rd"]
has_common = False
for password in password_list:
    if user_password == password:
        has_common = True
        break

if has_common == True:
    score -= 1
    print("❌ 8.Password is one of the most common passwords.")
else:
    print("✅ 8.Not a common password.")
    
# print a blank line
print("")

# print output
print(f"Final Score: {score} out of 8")

if score == 8:
    print("Security Level: Strong")
    print("Congratulations! Your password is highly secure and passed all security checks.")
elif score < 8 and score >=4 :
    print("Security Level: Medium")
    print("Tip: Your password is fairly secure, but try to avoid using patterns based on your username")
else:
    print("Security Level: Very Weak")
    print("Tip: Your password is too simple and easy to guess. Use a mix of letters, numbers, and symbols.")








