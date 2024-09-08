from tabom.models import Like


def do_like(user_id: int, like_id: int) -> Like:
    like = Like.objects.create(user_id=user_id, article_id=like_id)
    return like
