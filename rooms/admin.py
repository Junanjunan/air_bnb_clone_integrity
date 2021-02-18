from django.contrib import admin
from django.utils.html import mark_safe
# Django 에게 html 문자를 쓸 수 있게 mark_safe를 호출하는 것임
from . import models

# Register your models here.


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    list_display = ('name', 'used_by')

    def used_by(self, obj):
        return obj.rooms.count()

# InlineModelAdmin : admin 안에 또 다른 admin을 넣는 방법
# 다른 admin을 이용 : 현재 PhotoAdmin에서 사용하는 사진 올리기 기능을 다른 Admin에서도 사용하기 위해서 진행하는 작업임
# TabularInline <-> StackedInline (보여지는 방식의 차이)
# ForeignKey 가 있기 때문에 가능하다고 함.


class PhotoInline(admin.TabularInline):

    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    inlines = (PhotoInline,)

    fieldsets = (
        ('Basic Info', {'fields': ('name', 'description', 'room_type', 'country', 'city', 'address', 'price')},
         ),
        (
            'Times', {'fields': ('check_in', 'check_out', 'instant_book')},
        ),
        (
            'Spaces', {'fields': ('guests', 'beds', 'bedrooms', 'baths')},
        ),
        (
            'More About the Spaces', {
                'classes': ('collapse',),
                'fields': ('amenities', 'facilities', 'house_rules')},
        ),
        (
            'Last Details', {'fields': ('host',)}
        )

    )

    list_display = (
        'name',
        'country',
        'city',
        'price',
        'address',
        'guests',
        'beds',
        'bedrooms',
        'baths',
        'check_in',
        'check_out',
        'instant_book',
        'count_amenities',
        'count_photos',
        'total_rating'
    )

    ordering = ('name', 'price', 'bedrooms')

    list_filter = (
        'instant_book',
        'host__superhost',
        'room_type',
        'amenities',
        'facilities',
        'house_rules',
        # 'city',
        'country'
    )

    raw_id_fields = ("host", )
    # ForeignKey를 좀 더 나은 방법으로 찾을 수 잇게 해줌
    # host를 통으로 셀렉트 하는게 아니라, id를 줘서 검색할수 있게 해줌 (search 모양 클릭하면 많은 user list를 볼 수 있음)

    search_fields = ('city', '^host__username')

    filter_horizontal = ('amenities', 'facilities', 'house_rules')

    # self 는 admin class (여기서는 RoomAdmin), obj는 현재 행(row) 의미??
    def count_amenities(self, obj):
        return obj.amenities.count()

    def count_photos(self, obj):
        return obj.photos.count()
    count_photos.short_description = 'Photo Count'


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition """

    list_display = ('__str__', 'get_thumbnail')

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')
    get_thumbnail.short_description = "Thumbnail"
