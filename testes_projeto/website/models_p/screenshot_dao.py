class Screenshot:
    def __init__(self, pic_id, user_id, game_id):
        self.pic_id = pic_id
        self.user_id = user_id
        self.game_id = game_id

class ScreenshotDAO:
    def __init__(self):
        pass

    def filter_by_user_id_game_id(self, cursor, user_id, game_id):
        try:
            sql_command = "SELECT * FROM screenshot WHERE user_id = {} AND game_id = {}".format(str(user_id), str(game_id))
            cursor.execute(sql_command)
            result = cursor.fetchall()
            screenshots = [Screenshot(*screenshot) for screenshot in result]
            print(screenshots)
            return screenshots
        
        except Exception as e:
            print(e)
            return None

    def add(self, cursor, screenshot):
        try:
            sql_command = "INSERT INTO screenshot (pic_id, user_id, game_id) VALUES ({}, {}, {})".format(screenshot.pic_id, screenshot.user_id, screenshot.game_id)
            cursor.execute(sql_command)

        except Exception as e:
            print(e)