from typing import List

from fastapi import APIRouter

from src.services.service import Service


class CommentRouter:
    router: APIRouter

    def __init__(self, service: Service, routes: List[dict]):
        self.service = service
        self.router = APIRouter(prefix='/comment', tags=['comment'])

        self.register_routes(routes)

    def register_routes(self, routes):
        """Регистрация роутов"""
        for route in routes:
            self.router.add_api_route(**route)

    def get_router(self):
        """Геттер роута"""
        return self.router
