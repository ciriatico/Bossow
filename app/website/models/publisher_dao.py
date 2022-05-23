class Publisher:
    def __init__(self, publisher_id, publisher_name, headquarters, foundation_date, logo_picture):
        self.publisher_id = publisher_id
        self.publisher_name = publisher_name
        self.headquarters = headquarters
        self.foundation_date = foundation_date
        self.logo_picture = logo_picture

class PublisherDAO:
    def __init__(self):
        pass
    
    def get_all(self, cursor):
        try:
            sql_command = "SELECT * FROM Publisher"
            cursor.execute(sql_command)
            result = cursor.fetchall()
            publishers = [Publisher(*publisher) for publisher in result]
            return publishers
        
        except Exception as e:
            print(e)
            return None