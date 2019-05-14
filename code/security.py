from user import User

# let us immediately get the data by knowing the username or userid
user = [
    {
        'id': 1,
        'username': 'Jane',
        'password': 'qwer'
    }
]

username_mapping = { 'Jane': {
        'id': 1,
        'username': 'Jane',
        'password': 'qwer'
    }
}

userid_mapping = { 1: {
        'id': 1,
        'username': 'Jane',
        'password': 'qwer'
    }
}

def authenticate(username, password):
    # get() : a way of accessing the dictionary, it gives us the value of the key
    user = username_mapping.get(username, None)
    if user and user.password == password:
        return user

# the payload is the contents of JWT token
def identity(payload):
    userid = payload['identity']
    return userid_mapping.get(userid, None)