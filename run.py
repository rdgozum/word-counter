from word_counter import create_app
from word_counter.config import DevelopmentConfig

app = create_app(config_class=DevelopmentConfig)

if __name__ == "__main__":
    app.run()
