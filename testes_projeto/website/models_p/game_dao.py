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