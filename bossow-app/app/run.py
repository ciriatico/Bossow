from website import app
from config import Config

if __name__ == '__main__':
    app.config.from_object(Config)
    app.run(host='0.0.0.0', port=5000)
