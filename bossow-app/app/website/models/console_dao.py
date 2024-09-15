class Console:
    def __init__(self, console_id, console_name, specifications, developer, release_date, product_picture):
        self.console_id = console_id
        self.console_name = console_name
        self.specifications = specifications
        self.developer = developer
        self.release_date = release_date
        self.product_picture = product_picture

class ConsoleDAO:
    def __init__(self):
        pass
    
    def get_all(self, cursor):
        try:
            sql_command = "SELECT * FROM Console"
            cursor.execute(sql_command)
            result = cursor.fetchall()
            consoles = [Console(*console) for console in result]
            return consoles
        
        except Exception as e:
            print(e)
            return None