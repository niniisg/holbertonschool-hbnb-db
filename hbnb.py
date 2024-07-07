""" Another way to run the app"""
import os
from src import create_app

app = create_app('src.config.ProductionConfig' if os.environ.get('ENV') == 'production' else 'src.config.DevelopmentConfig')

if __name__ == "__main__":
    app.run()