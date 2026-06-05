username = input(f"Enter your username: ")

email = input("Enter your email: ")

valid_user = username or "User"

valid_user = username or "User"

print(f"Hello {valid_user}, " + ((email and f"your email is {email}") or ("please provide a valid email address.")))