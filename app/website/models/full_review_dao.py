class FullReview:
    def __init__(self, review_id, user_id, game_id, review_text, score, created_at, user_email, full_name, profile_picture, game_title, cover_picture):
        self.review_id = review_id
        self.user_id = user_id
        self.game_id = game_id
        self.review_text = review_text
        self.score = score
        self.created_at = created_at
        self.user_email = user_email
        self.full_name = full_name
        self.profile_picture = profile_picture
        self.game_title = game_title
        self.cover_picture = cover_picture

class FullReviewDAO:
    def __init__(self):
        pass
    
    def filter_by_game_id(self, cursor, game_id):
        try:
            cursor.callproc('selectFilteredReview2', [str(game_id)])
            result = cursor.fetchall()
            full_reviews = [FullReview(*review) for review in result]
            return full_reviews
        
        except Exception as e:
            print(e)
            return None

    def find_by_user_id(self, cursor, user_id):
        try:
            cursor.callproc('selectFilteredReview2', [str(user_id)])
            result = cursor.fetchall()
            full_reviews = [FullReview(*review) for review in result]
            return full_reviews
        
        except Exception as e:
            print(e)
            return None