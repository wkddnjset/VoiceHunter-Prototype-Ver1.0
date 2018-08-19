from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# ------------------------------------------------------------------
# TableName   : Sido
# Description : 시/도 테이블
# ------------------------------------------------------------------
class Sido(models.Model):
    class Meta:
        verbose_name_plural = " 시/도 테이블"

    sido = models.CharField(max_length=10, verbose_name='시/도')

    def __str__(self):
        return str(self.sido)
# ------------------------------------------------------------------
# TableName   : Gugun
# Description : 구/군 테이블
# ------------------------------------------------------------------
class Gugun(models.Model):
    class Meta:
        verbose_name_plural = " 구/군 테이블"

    sido = models.ForeignKey(Sido, on_delete=models.CASCADE, verbose_name='시/도')
    gugun = models.CharField(max_length=10, verbose_name='구/군')

    def __str__(self):
        return str(self.gugun)

# ------------------------------------------------------------------
# TableName   : Project
# Description : 프로젝트 테이블
# ------------------------------------------------------------------
class Project(models.Model):
    class Meta:
        verbose_name_plural = "   프로젝트 테이블"
        ordering = ["-id"]
    TYPE_CHOICES = (
        ('none', '----'),
        ('pro', '프로'),
        ('under', '언더'),
        ('both', '상관없음')
    )
    GENDER_CHOICES = (
        ('none', '----'),
        ('male', '남자'),
        ('female', '여자'),
        ('both', '성별무관')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='유저')
    title = models.CharField(max_length=100, verbose_name='프로젝트 명')
    gugun = models.ForeignKey(Gugun, on_delete=models.CASCADE, verbose_name='위치')
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, verbose_name='성우타입')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, verbose_name='성별')
    cost = models.PositiveIntegerField(verbose_name='예상금액')
    period = models.PositiveIntegerField(verbose_name='예상기간')
    deadline = models.DateField(verbose_name='마감기간')
    content = models.TextField(verbose_name='프로젝트 내용')
    start_at = models.DateField(verbose_name='예상 시작일')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='등록일자')

    def __str__(self):
        return str(self.title)

# ------------------------------------------------------------------
# TableName   : Tag
# Description : 태그 테이블
# ------------------------------------------------------------------
class Tag(models.Model):
    class Meta:
        verbose_name_plural = "  태그 테이블"

    name = models.CharField(max_length=20, verbose_name='태그명')

    def __str__(self):
        return str(self.name)

# ------------------------------------------------------------------
# TableName   : ProjectTag
# Description : 프로젝트별 태그 테이블
# ------------------------------------------------------------------
class ProjectTag(models.Model):
    class Meta:
        verbose_name_plural = "  프로젝트별 태그 테이블"
        unique_together = ("project", "tag")

    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='프로젝트')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name='태그')

    def __str__(self):
        return str(self.project)+' - '+str(self.tag)


# ------------------------------------------------------------------
# TableName   : ProjectApply
# Description : 프로젝트 지원 테이블
# ------------------------------------------------------------------
class ProjectApply(models.Model):
    class Meta:
        verbose_name_plural = "   프로젝트 지원 테이블"

    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='프로젝트')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='유저')
    cost = models.PositiveIntegerField(verbose_name='지원금액')
    period = models.PositiveIntegerField(verbose_name='지원기간')
    content = models.TextField(verbose_name='지원내용')
    voice = models.FileField(verbose_name='녹음파일')

    def __str__(self):
        return str(self.project)+' - '+str(self.user)