class Developer:
    def __init__(self, developer_id, developer_name, headquarters, foundation_date, logo_picture):
        self.developer_id = developer_id
        self.developer_name = developer_name
        self.headquarters = headquarters
        self.foundation_date = foundation_date
        self.logo_picture = logo_picture

class DeveloperDAO:
    def __init__(self):
        pass
    
    def get_all(self, cursor):
        try:
            sql_command = "SELECT * FROM Developer"
            cursor.execute(sql_command)
            result = cursor.fetchall()
            developers = [Developer(*developer) for developer in result]
            return developers
        
        except Exception as e:
            print(e)
            return None