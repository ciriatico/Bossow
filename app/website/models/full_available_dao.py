class FullAvailable:
    def __init__(self, game_id, console_id, console_name, product_picture):
        self.game_id = game_id
        self.console_id = console_id
        self.console_name = console_name
        self.product_picture = product_picture

class FullAvailableDAO:
    def __init__(self):
        pass
    
    def find_by_game_id(self, cursor, game_id):
        try:
            sql_command = "SELECT game_id, Console.console_id, console_name, product_picture FROM Available INNER JOIN Console ON Available.console_id = Console.console_id WHERE game_id = {}".format(str(game_id))
            cursor.execute(sql_command)
            result = cursor.fetchall()
            full_available = [FullAvailable(*available) for available in result]
            return full_available
        
        except Exception as e:
            print(e)
            return None