email = input("Enter your Email\n")
k , j, d = 0 , 0 , 0
# Check Length 
if len(email) >= 6:
    # Check First Alphabet
    if email[0].isalpha():
        #Check presence of @ and it occurs once
        if "@" in email and email.count("@") == 1:
            if (email[-4] == ".") ^ (email[-3] == "."):
                for c in email:
                    if c == " ":
                        k = 1
                    elif c.isalpha():
                        if c == c.upper():
                            j = 1
                    elif c.isdigit():
                        continue
                    elif c == "_" or c == "." or c == "@":
                        continue
                    else :
                        d = 1
                if k == 1:
                    print("Your email have Spaces")
                if j == 1:
                    print("Email have UpperCase character")
                if d == 1:
                    print("Email have unknown character")
            else :
                print("You have no top-level domains in your email")
        else:
            print("There is no @ in the email")
        pass
    else:
        print(f" {email[0]} Character is not Alphabet.")
else:
    print("Length is less than 6")
