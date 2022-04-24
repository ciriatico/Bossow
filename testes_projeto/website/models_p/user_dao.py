class User:
    def __init__(self, id, email, password, full_name, role, created_at, profile_picture):
        self.id = id
        self.email = email
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
            sql_command = "SELECT * FROM user"
            cursor.execute(sql_command)
            result = cursor.fetchall()
            users = [User(*user) for user in result]
            return users
        
        except Exception as e:
            print(e)
            return None
    
    def find_by_id(self, cursor, id):
        try:
            sql_command = "SELECT * FROM user WHERE id = {}".format(str(id))
            cursor.execute(sql_command)
            result = cursor.fetchone()
            user = User(*result)
            return user
        
        except Exception as e:
            print(e)
            return None

    def find_by_email(self, cursor, email):
        try:
            sql_command = "SELECT * FROM user WHERE email = '{}'".format(email)
            cursor.execute(sql_command)
            result = cursor.fetchone()
            user = User(*result)
            return user
        
        except Exception as e:
            print(e)
            return None

    def add(self, cursor, user):
        try:
            sql_command = "INSERT INTO user (email, password, full_name, role, profile_picture) VALUES (%(email)s, %(password)s, %(full_name)s, %(role)s, %(profile_picture)s)"
            data_insert = {"email": user.email, "password": user.password, "full_name": user.full_name, "role": user.role, "profile_picture": user.profile_picture}
            cursor.execute(sql_command, data_insert)

        except Exception as e:
            print(e)

    def update(self, cursor, user):
        try:
            sql_command = "UPDATE user SET email = %(email)s, password = %(password)s, full_name = %(full_name)s, role = %(role)s, profile_picture = %(profile_picture)s WHERE id = %(id)s"
            data_update = {"email": user.email, "password": user.password,  "full_name": user.full_name, "role": user.role, "profile_picture": user.profile_picture, "id": user.id}
            cursor.execute(sql_command, data_update)

        except Exception as e:
            print(e)

    def delete(self, cursor, id):
        try:
            sql_command = "DELETE FROM user WHERE id = {}".format(id)
            print(sql_command)
            cursor.execute(sql_command)
            
        except Exception as e:
            print(e)