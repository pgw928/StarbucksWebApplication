from django.db import models


class User(models.Model):
    user_name = models.CharField('이름', max_length=10)
    user_id = models.CharField('아이디', max_length=20, unique=True)
    password = models.CharField('비밀번호', max_length=100)
    phone_num = models.CharField('전화번호', max_length=13, default=0)
    point = models.IntegerField('마일리지', default=0)
    select_adr = models.CharField(max_length=20, blank=True, null=True) #김은수

    def __str__(self):
        return self.user_id

    class Meta:
        db_table = "user"


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField('글제목', max_length=1000)
    contents = models.TextField('글내용', max_length=1000)
    created_date = models.DateField('작성시간', null=True)
    qtype = models.CharField('문의유형', max_length=15, default='매장')
    hit = models.PositiveIntegerField('조회수', default=0)

    def __str__(self):
        return self.title

    @property
    def update_counter(self):
        self.hit = self.hit + 1
        self.save()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    author = models.CharField('댓글 작성자', max_length=200)
    text = models.TextField('댓글 내용', max_length=1000)
    created_date = models.DateField('작성시간', null=True)

    def __str__(self):
        return self.text