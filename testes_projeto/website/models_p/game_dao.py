class Game:
    def __init__(self, id, title, release_date, description, developer, publisher, trailer_url, cover_picture):
        self.id = id
        self.title = title
        self.release_date = release_date
        self.description = description
        self.developer = developer
        self.publisher = publisher
        self.trailer_url = trailer_url
        self.cover_picture = cover_picture

class GameDAO:
    def __init__(self):
        pass

    def get_all_sorted(self, cursor, sorting_key):
        try:
            sql_command = "SELECT * FROM game ORDER BY {}".format(sorting_key)
            cursor.execute(sql_command)
            result = cursor.fetchall()
            games = [Game(*game) for game in result]
            return games
        
        except Exception as e:
            print(e)
            return None

    def find_by_id(self, cursor, id):
        try:
            sql_command = "SELECT * FROM game WHERE id = {}".format(str(id))
            cursor.execute(sql_command)
            result = cursor.fetchone()
            game = Game(*result)
            return game
        
        except Exception as e:
            print(e)
            return None

    def add(self, cursor, game):
        try:
            sql_command = "INSERT INTO game (title, release_date, description, developer, publisher, trailer_url, cover_picture) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', {})".format(game.title, game.release_date, game.description, game.developer, game.publisher, game.trailer_url, game.cover_picture)            
            cursor.execute(sql_command)

        except Exception as e:
            print(e)

    def update(self, cursor, game):
        try:
            sql_command = "UPDATE game SET title = %(title)s, release_date = %(release_date)s, description = %(description)s, developer = %(developer)s, publisher = %(publisher)s, trailer_url = %(trailer_url)s, cover_picture = %(cover_picture)s WHERE id = %(id)s"
            data_update = {"title": game.title, "release_date": game.release_date, "description": game.description, "developer": game.developer, "publisher": game.publisher, "trailer_url": game.trailer_url, "cover_picture": game.cover_picture, "id": game.id}
            cursor.execute(sql_command, data_update)

        except Exception as e:
            print(e)
            return None

    def delete(self, cursor, user_id, game_id):
        try:
            sql_command = "DELETE FROM game WHERE id = {}".format(game_id)
            cursor.execute(sql_command)

        except Exception as e:
            print(e)