from word_counter import create_app
from word_counter.config import Config

app = create_app(config_class=Config)

if __name__ == "__main__":
    app.run()
