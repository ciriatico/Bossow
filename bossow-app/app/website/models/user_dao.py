class User:
    def __init__(self, user_id, user_email, password, full_name, role, created_at, profile_picture):
        self.user_id = user_id
        self.user_email = user_email
        self.password = password
        self.full_name = full_name
        self.role = role
        self.created_at = created_at
        self.profile_picture = profile_picture

class UserDAO:
    def __init__(self):
        pass

    def get_all(self, cursor):
        try:
            sql_command = "SELECT * FROM User"
            cursor.execute(sql_command)
            result = cursor.fetchall()
            users = [User(*user) for user in result]
            return users
        
        except Exception as e:
            print(e)
            return None
    
    def find_by_id(self, cursor, user_id):
        try:
            sql_command = "SELECT * FROM User WHERE user_id = {}".format(str(user_id))
            cursor.execute(sql_command)
            result = cursor.fetchone()
            user = User(*result)
            return user
        
        except Exception as e:
            print(e)
            return None

    def find_by_email(self, cursor, user_email):
        try:
            sql_command = "SELECT * FROM User WHERE user_email = '{}'".format(user_email)
            cursor.execute(sql_command)
            result = cursor.fetchone()
            user = User(*result)
            return user
        
        except Exception as e:
            print(e)
            return None

    def add(self, cursor, user):
        try:
            sql_command = "INSERT INTO User (user_email, password, full_name, role, profile_picture) VALUES (%(user_email)s, %(password)s, %(full_name)s, %(role)s, %(profile_picture)s)"
            data_insert = {"user_email": user.user_email, "password": user.password, "full_name": user.full_name, "role": user.role, "profile_picture": user.profile_picture}
            cursor.execute(sql_command, data_insert)

        except Exception as e:
            print(e)

    def update(self, cursor, user):
        try:
            sql_command = "UPDATE User SET user_email = %(user_email)s, password = %(password)s, full_name = %(full_name)s, role = %(role)s, profile_picture = %(profile_picture)s WHERE user_id = %(user_id)s"
            data_update = {"user_email": user.user_email, "password": user.password,  "full_name": user.full_name, "role": user.role, "profile_picture": user.profile_picture, "user_id": user.user_id}
            cursor.execute(sql_command, data_update)

        except Exception as e:
            print(e)

    def delete(self, cursor, user_id):
        try:
            sql_command = "DELETE FROM User WHERE user_id = {}".format(user_id)
            print(sql_command)
            cursor.execute(sql_command)
            
        except Exception as e:
            print(e)