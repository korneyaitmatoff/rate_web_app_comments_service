from src.services.service import Service
from src.schemas.comment import Comment, CommentDict
from src.repositories.repository import Repository


class CommentService(Service):
    """Класс-сервис для работы с сущностью "Сайт" """

    def __init__(self, repository: Repository):
        super().__init__(repository=repository)

    def add_site_comment(self, site_id: int, user_id: int, text: str):
        return self.create(data={
            "site_id": site_id,
            "user_id": user_id,
            "text": text,
        })

    def get_comments_by_site(self, site_id: int) -> list[Comment]:
        return self.read(filters=(self.repository.table.site_id == site_id,))

    def edit_comment(self, comment_id: int, comment: CommentDict):
        return self.repository.update(id=comment_id, data=dict(comment))

    def delete_comment(self, comment_id: int):
        return self.delete(filters=(self.repository.table.id == comment_id,))

    def get_users_comment(self, user_id: int) -> list[Comment]:
        return self.read(filters=(self.repository.table.user_id == user_id,))