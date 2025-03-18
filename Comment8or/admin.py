from django.contrib import admin

# tao doi tuong adminsite moi ( buoc 3)
class Comment8orAdminSite(admin.AdminSite):
    title_header = "c8admin"
    site_header = "c8admin"
    index_title = "c8admin"
    logout_template = "comment8or/logged_out.html"

