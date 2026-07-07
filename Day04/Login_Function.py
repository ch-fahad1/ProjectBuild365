def login(username, password):

    if username == "admin" and password == "12345":
        return "Login Successful"

    else:
        return "Invalid Credentials"

print(login("admin", "12345"))