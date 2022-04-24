class Review:
    def __init__(self, id, user_id, game_id, review_text, score, date_created):
        self.id = id
        self.user_id = user_id
        self.game_id = game_id
        self.review_text = review_text
        self.score = score
        self.date_created = date_created

class ReviewDAO:
    def __init__(self):
        pass
    
    def filter_by_game_id_ordered(self, cursor, game_id, sorting_key):
        try:
            sql_command = "SELECT * FROM review WHERE game_id = {} ORDER BY {}".format(game_id, sorting_key)
            cursor.execute(sql_command)
            result = cursor.fetchall()
            reviews = [Review(*review) for review in result]
            return reviews
        
        except Exception as e:
            print(e)
            return None
    
    def filter_by_user_id(self, cursor, user_id):
        try:
            sql_command = "SELECT * FROM review WHERE user_id = {}".format(str(user_id))
            cursor.execute(sql_command)
            result = cursor.fetchall()
            reviews = [Review(*review) for review in result]
            return reviews
        
        except Exception as e:
            print(e)
            return None