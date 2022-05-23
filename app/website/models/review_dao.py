class Review:
    def __init__(self, review_id, user_id, game_id, review_text, score, created_at):
        self.review_id = review_id
        self.user_id = user_id
        self.game_id = game_id
        self.review_text = review_text
        self.score = score
        self.created_at = created_at

class ReviewDAO:
    def __init__(self):
        pass
    
    def filter_by_game_id_ordered(self, cursor, game_id, sorting_key):
        try:
            sql_command = "SELECT * FROM Review WHERE game_id = {} ORDER BY {}".format(game_id, sorting_key)
            cursor.execute(sql_command)
            result = cursor.fetchall()
            reviews = [Review(*review) for review in result]
            return reviews
        
        except Exception as e:
            print(e)
            return None
    
    def filter_by_user_id(self, cursor, user_id):
        try:
            sql_command = "SELECT * FROM Review WHERE user_id = {}".format(str(user_id))
            cursor.execute(sql_command)
            result = cursor.fetchall()
            reviews = [Review(*review) for review in result]
            return reviews
        
        except Exception as e:
            print(e)
            return None

    def filter_by_user_id_game_id(self, cursor, user_id, game_id):
        try:
            sql_command = "SELECT * FROM Review WHERE user_id = {} AND game_id = {}".format(str(user_id), str(game_id))
            cursor.execute(sql_command)
            result = cursor.fetchone()
            review = Review(*result)
            return review
        
        except Exception as e:
            print(e)
            return None

    def find_by_id(self, cursor, review_id):
        try:
            sql_command = "SELECT * FROM Review WHERE review_id = {}".format(str(review_id))
            cursor.execute(sql_command)
            result = cursor.fetchone()
            game = Review(*result)
            return game
        
        except Exception as e:
            print(e)
            return None

    def add(self, cursor, review):
        try:
            sql_command = "INSERT INTO Review (user_id, game_id, review_text, score) VALUES ({}, {}, '{}', {})".format(review.user_id, review.game_id, review.review_text, review.score)
            cursor.execute(sql_command)

        except Exception as e:
            print(e)

    def update(self, cursor, review):
        try:
            sql_command = "UPDATE Review SET review_text = %(review_text)s, score = %(score)s WHERE review_id = %(review_id)s"
            data_update = {"review_id": review.review_id, "review_text": review.review_text, "score": review.score}
            cursor.execute(sql_command, data_update)

        except Exception as e:
            print(e)
            return None

    def delete(self, cursor, user_id, review_id):
        try:
            sql_command = "DELETE FROM Review WHERE review_id = {}".format(review_id)
            cursor.execute(sql_command)

        except Exception as e:
            print(e)