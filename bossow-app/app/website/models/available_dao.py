class Available:
    def __init__(self, game_id, console_id):
        self.game_id = game_id
        self.console_id = console_id

class AvailableDAO:
    def __init__(self):
        pass

    def add(self, cursor, available):
        try:
            sql_command = "INSERT INTO Available (game_id, console_id) VALUES ({}, {})".format(available.game_id, available.console_id)            
            cursor.execute(sql_command)

        except Exception as e:
            print(e)

    def find_by_game_id(self, cursor, game_id):
        try:
            sql_command = "SELECT * FROM Available WHERE game_id = {}".format(str(game_id))
            cursor.execute(sql_command)
            result = cursor.fetchall()
            availables = [Available(*available) for available in result]
            return availables
        
        except Exception as e:
            print(e)
            return None
    
    def get_all(self, cursor):
        try:
            sql_command = "SELECT * FROM Available"
            cursor.execute(sql_command)
            result = cursor.fetchall()
            availables = [Available(*available) for available in result]
            return availables
        
        except Exception as e:
            print(e)
            return None

    def delete(self, cursor, available):
        try:
            sql_command = "DELETE FROM Available WHERE game_id = {} AND console_id = {}".format(str(available.game_id), str(available.console_id))
            cursor.execute(sql_command)

        except Exception as e:
            print(e)