email = input("Enter your email: ")

username=email[:email.index("@")]
domain=email[email.index("@"):]

print(f"Your username is: {username} and your domain is: {domain}")