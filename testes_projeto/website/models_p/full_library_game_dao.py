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
            print(f"user_id {user_id}")
            cursor.callproc('selectLibrary', ["user_id", str(user_id)])
            result = cursor.fetchall()
            print(f"games {games}")
            games = [FullLibraryGame(*game) for game in result]
            return games
        
        except Exception as e:
            print(e)
            return None