class Library:
    def __init__(self, user_id, game_id, hours_played=None, completion_percentage=None, last_logged_in=None):
        self.user_id = user_id
        self.game_id = game_id
        self.hours_played = hours_played
        self.completion_percentage = completion_percentage
        self.last_logged_in = last_logged_in

class LibraryDAO:
    def __init__(self):
        pass

    def filter_by_user_id_game_id(self, cursor, user_id, game_id):
        try:
            sql_command = "SELECT * FROM Library WHERE user_id = {} AND game_id = {}".format(str(user_id), str(game_id))
            cursor.execute(sql_command)
            result = cursor.fetchone()
            library_game = Library(*result)
            return library_game
        
        except Exception as e:
            print(e)
            return None

    def filter_by_user_id(self, cursor, user_id):
        try:
            sql_command = "SELECT * FROM Library WHERE user_id = {}".format(str(user_id))
            cursor.execute(sql_command)
            result = cursor.fetchall()
            library_games = [Library(*library_game) for library_game in result]
            return library_games
        
        except Exception as e:
            print(e)
            return None

    def add(self, cursor, library_game):
        try:
            sql_command = "INSERT INTO Library (user_id, game_id) VALUES ({}, {})".format(library_game.user_id, library_game.game_id)
            cursor.execute(sql_command)

        except Exception as e:
            print(e)

    def delete(self, cursor, user_id, game_id):
        try:
            sql_command = "DELETE FROM Library WHERE user_id = {} AND game_id = {}".format(user_id, game_id)
            cursor.execute(sql_command)

        except Exception as e:
            print(e)

    def update(self, cursor, library_game):
        try:
            sql_command = "UPDATE Library SET hours_played = %(hours_played)s, completion_percentage = %(completion_percentage)s, last_logged_in = %(last_logged_in)s WHERE user_id = %(user_id)s AND game_id = %(game_id)s"
            data_update = {"hours_played": str(library_game.hours_played),
            "completion_percentage": str(library_game.completion_percentage),
            "last_logged_in": library_game.last_logged_in,
            "user_id": library_game.user_id,
            "game_id": library_game.game_id}
            cursor.execute(sql_command, data_update)

        except Exception as e:
            print(e)