from typing import List

from fastapi import FastAPI

from src.app import App
from src.database import tables
from src.repositories import CommentRepository
from src.services.comment_service import CommentService
from src.schemas.comment import Comment
from src.routes.comment import CommentRouter

server = (app := App(server=FastAPI())).get_app()

# Сервисы
comment_service = CommentService(repository=CommentRepository(table=tables.Comment, database_handler=app.db_handler))

# Роутеры
app.register_routes([
    CommentRouter(
        service=comment_service,
        routes=[
            {
                "path": "/{site_id}",
                "responses": {400: {"description": "Bad request"}},
                "response_model": List[Comment],
                "description": "Получение списка комментариев сайта", "methods": ['GET'],
                "endpoint": comment_service.get_comments_by_site
            },
            {
                "path": "/{comment_id}",
                "responses": {400: {"description": "Bad request"}},
                "description": "Изменение комментария", "methods": ['PATCH'],
                "endpoint": comment_service.edit_comment
            },
            {
                "path": "/{comment_id}",
                "responses": {400: {"description": "Bad request"}},
                "description": "Удаление комментария", "methods": ['DELETE'],
                "endpoint": comment_service.delete_comment
            },
            {
                "path": "/{site_id}/{user_id}",
                "responses": {400: {"description": "Bad request"}},
                "description": "Добавление комментария", "methods": ['POST'],
                "endpoint": comment_service.add_site_comment
            },
{
                "path": "/list/{user_id}",
                "responses": {400: {"description": "Bad request"}},
                "description": "Получение комментариев пользователя", "methods": ['GET'],
                "endpoint": comment_service.get_users_comment
            },
        ]
    ).get_router()
])
