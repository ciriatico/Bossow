class Image:
    def __init__(self, id, img, filename, mimetype, created_at):
        self.id = id
        self.img = img
        self.filename = filename
        self.mimetype = mimetype
        self.created_at = created_at

class ImageDAO:
    def __init__(self):
        pass

    def get_all(self, cursor):
        try:
            sql_command = "SELECT * FROM image"
            cursor.execute(sql_command)
            result = cursor.fetchall()
            images = [Image(*image) for image in result]
            return images
        
        except Exception as e:
            print(e)
            return None
    
    def find_by_id(self, cursor, id):
        try:
            sql_command = "SELECT * FROM image WHERE id = {}".format(str(id))
            cursor.execute(sql_command)
            result = cursor.fetchone()
            image = Image(*result)
            return image
        
        except Exception as e:
            print(e)
            return None
    
    def add(self, cursor, img):
        try:
            sql_command = "INSERT INTO image (img, filename, mimetype) VALUES (%(img)s, %(filename)s, %(mimetype)s)"
            data_insert = {"img": img.img, "filename": img.filename, "mimetype": img.mimetype}
            cursor.execute(sql_command, data_insert)

        except Exception as e:
            print(e)
    
    def delete(self, cursor, id):
        try:
            sql_command = "DELETE FROM image WHERE id = {}".format(id)
            cursor.execute(sql_command)
            
        except Exception as e:
            print(e)