from django.contrib import admin
from reviews.models import (Publisher, Contributor, Book, BookContributor, Review)

class BookAdmin(admin.ModelAdmin):
 date_hierarchy = 'publication_date'

 # các cột hiển thị thông tin
 list_display = ('title', 'isbn13', 'has_isbn')
 # lọc thông tin
 list_filter = ('publisher', 'publication_date')

 search_fields = ('title', 'isbn')


 # Muc E2 trang 19
 @admin.display(ordering='isbn', description='ISBN-13',empty_value='-/-')
 def isbn13(self, obj):
  """ '9780316769174' => '978-0-31-676917-4' """
  return "{}-{}-{}-{}-{}".format(obj.isbn[0:3],
                                 obj.isbn[3:4], obj.isbn[4:6], obj.isbn[6:12],
                                 obj.isbn[12:13])

 #Muc E3 trang 19
 @admin.display(boolean=True, description='Has ISBN', )
 def has_isbn(self, obj):
  """ '9780316769174' => True """
  return bool(obj.isbn)
# Register your models here.

# Mục II trang 22
# Mục II này tạo class này giong như BookAdmin , sau do them register o duoi y chang BookAdmin

class ReviewAdmin(admin.ModelAdmin):
 exclude = ('date_edited',)
 # 3. trang 23 thi bo commen nay di
 # fields = ('content', 'rating', 'creator', 'book')

 # 4. trang 24 ( nho bo comment dong o tren)
 # fieldsets = (
 #  ("Linkage", {"fields": ("creator", "book")}),
 #  ("Review content", {"fields": ("content", "rating")}),
 # )

 #5. trang 24
 fieldsets = (
  (None, {'fields': ('creator', 'book')}),
  ('Review content', {'fields': ('content','rating')})
 )

class ContributorAdmin(admin.ModelAdmin):
 #hien thi cot last name va first name
 list_display = ("last_names", "first_names")

 # them hop thoai tim kiem theo leasr name va first name
 search_fields = ('last_names__startswith', 'first_name')

 #them bo loc last name ( canh phai )
 list_filter = ('last_names',)


admin.site.register(Publisher)
admin.site.register(Contributor, ContributorAdmin) # them tuong tu BookAdmin
admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor)
admin.site.register(Review, ReviewAdmin)