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
            cursor.callproc('selectFilteredReview', ["game_id", str(game_id)])
            result = cursor.fetchall()
            full_reviews = [FullReview(*review) for review in result]
            return full_reviews
        
        except Exception as e:
            print(e)
            return None

    def find_by_user_id(self, cursor, user_id):
        try:
            cursor.callproc('selectFilteredReview', ["user_id", str(user_id)])
            result = cursor.fetchall()
            
            full_reviews = [FullReview(*review) for review in result]
            return full_reviews
        
        except Exception as e:
            print(e)
            return None