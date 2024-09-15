class Game:
    def __init__(self, game_id, game_title, release_date, description, developer_id, publisher_id, trailer_url, cover_picture):
        self.game_id = game_id
        self.game_title = game_title
        self.release_date = release_date
        self.description = description
        self.developer_id = developer_id
        self.publisher_id = publisher_id
        self.trailer_url = trailer_url
        self.cover_picture = cover_picture

class GameDAO:
    def __init__(self):
        pass

    def get_all_sorted(self, cursor, sorting_key):
        try:
            sql_command = "SELECT * FROM Game ORDER BY {}".format(sorting_key)
            cursor.execute(sql_command)
            result = cursor.fetchall()
            games = [Game(*game) for game in result]
            return games
        
        except Exception as e:
            print(e)
            return None

    def find_by_id(self, cursor, game_id):
        try:
            sql_command = "SELECT * FROM Game WHERE game_id = {}".format(str(game_id))
            cursor.execute(sql_command)
            result = cursor.fetchone()
            game = Game(*result)
            return game
        
        except Exception as e:
            print(e)
            return None

    def add(self, cursor, game):
        try:
            sql_command = "INSERT INTO Game (game_title, release_date, description, developer_id, publisher_id, trailer_url, cover_picture) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', {})".format(game.game_title, game.release_date, game.description, game.developer_id, game.publisher_id, game.trailer_url, game.cover_picture)            
            cursor.execute(sql_command)

        except Exception as e:
            print(e)

    def update(self, cursor, game):
        try:
            sql_command = "UPDATE Game SET game_title = %(game_title)s, release_date = %(release_date)s, description = %(description)s, developer_id = %(developer_id)s, publisher_id = %(publisher_id)s, trailer_url = %(trailer_url)s, cover_picture = %(cover_picture)s WHERE game_id = %(game_id)s"
            data_update = {"game_title": game.game_title, "release_date": game.release_date, "description": game.description, "developer_id": game.developer_id, "publisher_id": game.publisher_id, "trailer_url": game.trailer_url, "cover_picture": game.cover_picture, "game_id": game.game_id}
            cursor.execute(sql_command, data_update)

        except Exception as e:
            print(e)
            return None

    def delete(self, cursor, game_id):
        try:
            sql_command = "DELETE FROM Game WHERE game_id = {}".format(str(game_id))
            cursor.execute(sql_command)

        except Exception as e:
            print(e)