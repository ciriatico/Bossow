class FullReview:
    def __init__(self, review_id, user_id, game_id, review_text, score, date_created, email, full_name, profile_picture, game_title, cover_picture):
        self.review_id = review_id
        self.user_id = user_id
        self.game_id = game_id
        self.review_text = review_text
        self.score = score
        self.date_created = date_created
        self.email = email
        self.full_name = full_name
        self.profile_picture = profile_picture
        self.game_title = game_title
        self.cover_picture = cover_picture

class FullReviewDAO:
    def __init__(self):
        pass
    
    def filter_by_game_id(self, cursor, game_id):
        try:
            sql_command = "SELECT review_id, user_id, game_id, review_text, score, date_created, email, full_name, profile_picture, title, cover_picture FROM (SELECT filtered_review.id as review_id, user_id, game_id, review_text, score, filtered_review.date_created, email, full_name, profile_picture FROM (SELECT * FROM review WHERE game_id = {}) as filtered_review INNER JOIN user ON filtered_review.user_id = user.id ORDER BY date_created) as review_user INNER JOIN (SELECT id, title, cover_picture FROM game) as filtered_game ON review_user.game_id = filtered_game.id".format(str(game_id))
            cursor.execute(sql_command)
            result = cursor.fetchall()
            full_reviews = [FullReview(*review) for review in result]
            return full_reviews
        
        except Exception as e:
            print(e)
            return None

    def find_by_user_id(self, cursor, user_id):
        try:
            sql_command = "SELECT review_id, user_id, game_id, review_text, score, date_created, email, full_name, profile_picture, title, cover_picture FROM (SELECT filtered_review.id as review_id, user_id, game_id, review_text, score, filtered_review.date_created, email, full_name, profile_picture FROM (SELECT * FROM review WHERE user_id = {}) as filtered_review INNER JOIN user ON filtered_review.user_id = user.id ORDER BY date_created) as review_user INNER JOIN (SELECT id, title, cover_picture FROM game) as filtered_game ON review_user.game_id = filtered_game.id".format(str(user_id))
            cursor.execute(sql_command)
            result = cursor.fetchall()
            full_reviews = [FullReview(*review) for review in result]
            return full_reviews
        
        except Exception as e:
            print(e)
            return None