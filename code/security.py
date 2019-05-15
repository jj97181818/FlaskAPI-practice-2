from user import User

def authenticate(username, password):
    # get() : a way of accessing the dictionary, it gives us the value of the key
    user = User.find_by_username(username)
    if user and user.password == password:
        return user

# the payload is the contents of JWT token
def identity(payload):
    userid = payload['identity']
    return User.find_by_id(userid)