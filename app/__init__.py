import os
from functools import lru_cache

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
from dotenv import load_dotenv

from config import Settings

templates = Jinja2Templates(directory='app/templates')


@lru_cache
def get_setttings():
    return Settings()


dotenv_path = 'env/.env'
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

logger.add('log/debug.log', level='DEBUG',
           format='{time} {level} {message}', rotation='10 KB', compression='zip')


def create_app():
    app = FastAPI()

    # Routers

    from .main import main as main_router

    app.include_router(main_router)

    return app


app = create_app()

app.mount('/static', StaticFiles(directory='app/static'), name='static')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
