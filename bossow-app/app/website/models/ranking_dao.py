class Ranking:
    def __init__(self, game_id, game_title, cover_picture, mean_score, count_library):
        self.game_id = game_id
        self.game_title = game_title
        self.cover_picture = cover_picture
        self.mean_score = mean_score
        self.count_library = count_library

class RankingDAO:
    def __init__(self):
        pass
    
    def get_all(self, cursor):
        try:
            sql_command = "SELECT * FROM Ranking"
            cursor.execute(sql_command)
            result = cursor.fetchall()
            rankings = [Ranking(*ranking) for ranking in result]
            return rankings
        
        except Exception as e:
            print(e)
            return None