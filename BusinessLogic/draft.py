
user_name = 'hello'
password = "world"

query = ("INSERT INTO user (user_name, password, user_type) VALUES ('%s', '%s', 'Student')" % (user_name, password))
print(query)
