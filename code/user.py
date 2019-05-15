import sqlite3

class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE user = ?"
        # the parameter need tuple, although there is only one parameter
        result = cursor.execute(query, (username,))
        row = result.fetchone()

        if row:
            # passing it as a set of arguments
            user = cls(*row)
            #user = cls(row[0], row[1], row[2]) # using the current class (Not hard coding the class name here)
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db' )
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id = ?"
        # the parameter need tuple, although there is only one parameter
        result = cursor.execute(query, (_id,))
        row = result.fetchone()

        if row:
            # passing it as a set of arguments
            user = cls(*row)
            #user = cls(row[0], row[1], row[2]) # using the current class (Not hard coding the class name here)
        else:
            user = None

        connection.close()
        return user