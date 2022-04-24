class FullLibraryGame:
    def __init__(self, user_id, game_id, hours_played, completion_percentage, last_logged_in, title, release_date, description, developer, publisher, trailer_url, cover_picture):
        self.user_id = user_id
        self.game_id = game_id
        self.hours_played = hours_played
        self.completion_percentage = completion_percentage
        self.last_logged_in = last_logged_in,
        self.title = title
        self.release_date = release_date
        self.description = description
        self.developer = developer
        self.publisher = publisher
        self.trailer_url = trailer_url
        self.cover_picture = cover_picture

class FullLibraryGameDAO:
    def __init__(self):
        pass

    def find_by_user_id(self, cursor, user_id):
        try:
            sql_command = "SELECT user_id, game_id, hours_played, completion_percentage, last_logged_in, title, release_date, description, developer, publisher, trailer_url, cover_picture FROM (SELECT * FROM library_game WHERE user_id = {}) as filtered_library INNER JOIN game ON filtered_library.game_id = game.id;".format(str(user_id))
            cursor.execute(sql_command)
            result = cursor.fetchall()
            games = [FullLibraryGame(*game) for game in result]
            return games
        
        except Exception as e:
            print(e)
            return None