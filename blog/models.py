from django.db import models

class Post(models.Model):
    author_name = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    upgraded_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # on_delete : Commnet는 Post에 속해있는 거잖아.
    # 그러면 속해있는 부모인 Post가 삭제되면 그에 딸린 Comment들은 어쩔건지
    # CASCADE : Post 삭제되면 관련 comment도 다 삭제하겠다.
    massage = models.TextField()

