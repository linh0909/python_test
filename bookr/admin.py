from django.contrib import admin

class BookrAdminSite(admin.AdminSite):
    title_header = "Bookr Admin"
    site_header = "Bookr Administration"
    index_title = "Bookr Site Admin"
