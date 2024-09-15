class FullLibrary:
    def __init__(self, user_id, game_id, hours_played, completion_percentage, last_logged_in, game_title, release_date, description, developer_id, publisher_id, trailer_url, cover_picture):
        self.user_id = user_id
        self.game_id = game_id
        self.hours_played = hours_played
        self.completion_percentage = completion_percentage
        self.last_logged_in = last_logged_in,
        self.game_title = game_title
        self.release_date = release_date
        self.description = description
        self.developer_id = developer_id
        self.publisher_id = publisher_id
        self.trailer_url = trailer_url
        self.cover_picture = cover_picture

class FullLibraryDAO:
    def __init__(self):
        pass

    def find_by_user_id(self, cursor, user_id):
        try:
            # cursor.callproc('selectLibrary', [str(user_id)])
            # result = cursor.fetchall()

            sql_command = "SELECT user_id, Game.game_id, hours_played, completion_percentage, last_logged_in, game_title, release_date, description, developer_id, publisher_id, trailer_url, cover_picture FROM (SELECT * FROM Library WHERE user_id = {}) as filtered_library INNER JOIN Game ON filtered_library.game_id = Game.game_id;".format(str(user_id))
            cursor.execute(sql_command)
            result = cursor.fetchall()

            games = [FullLibrary(*game) for game in result]
            return games
        
        except Exception as e:
            print(e)
            return None