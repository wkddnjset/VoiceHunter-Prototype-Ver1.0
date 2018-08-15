from django.contrib import admin
from .models import *

# Register your models here.
# ------------------------------------------------------------------
# TableName   : Sido
# Description : 시/도 테이블
# ------------------------------------------------------------------
@admin.register(Sido)
class SidoAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Sido._meta.fields]

# ------------------------------------------------------------------
# TableName   : Gugun
# Description : 구/군 테이블
# ------------------------------------------------------------------
@admin.register(Gugun)
class GugunAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Gugun._meta.fields]

# ------------------------------------------------------------------
# TableName   : Project
# Description : 프로젝트 테이블
# ------------------------------------------------------------------
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'type', 'gender', 'cost','period','deadline','gugun']

# ------------------------------------------------------------------
# TableName   : Tag
# Description : 태그 테이블
# ------------------------------------------------------------------
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Tag._meta.fields]

# ------------------------------------------------------------------
# TableName   : ProjectTag
# Description : 프로젝트별 태그 테이블
# ------------------------------------------------------------------
@admin.register(ProjectTag)
class ProjectTagAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ProjectTag._meta.fields]

# ------------------------------------------------------------------
# TableName   : ProjectApply
# Description : 프로젝트 지원 테이블
# ------------------------------------------------------------------
@admin.register(ProjectApply)
class ProjectApplyAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ProjectApply._meta.fields]