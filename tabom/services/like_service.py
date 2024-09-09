from tabom.models import Like


def do_like(user_id: int, like_id: int) -> Like:
    like = Like.objects.create(user_id=user_id, article_id=like_id)
    return like


def undo_like(user_id: int, article_id: int) -> None:
    like = Like.objects.filter(user_id=user_id, article_id=article_id).get()
    like.delete()
