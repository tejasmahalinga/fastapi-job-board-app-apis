from apis.base import api_router
from core.config import settings
from db.base import Base
from db.session import engine
from fastapi import FastAPI
# from apis.general_pages.route_homepage import general_pages_router

def include_router(app):
	app.include_router(api_router)

def create_tables():
	Base.metadata.create_all(bind=engine)



def start_application():
    app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
    include_router(app)
    create_tables()
    return app


app = start_application()
