from django.contrib import admin

from .models import (
    Audio, Image, Story, Video
)

def approve(modeladmin, request, queryset):
    queryset.update(approved=True)
approve.short_description = "Approve memories"

class MemoryAdmin(admin.ModelAdmin):
    list_display = ("title", "uploaded_by", "approved")
    actions = [approve]    

@admin.register(Story)
class StoryAdmin(MemoryAdmin):
    pass

@admin.register(Image)
class ImageAdmin(MemoryAdmin):
    pass

@admin.register(Video)
class VideoAdmin(MemoryAdmin):
    pass

@admin.register(Audio)
class AudioAdmin(MemoryAdmin):
    pass


# class UnitOrProgramInline(admin.TabularInline):
#     model = UnitOrProgram
#     extra = 0


# @admin.register(Division)
# class DivisionAdmin(admin.ModelAdmin):
#     list_display = ("name",)
#     inlines = (UnitOrProgramInline,)


# @admin.register(JobTitle)
# class JobTitleAdmin(admin.ModelAdmin):
#     list_display = ("name", "position_description_link")


# @admin.register(Employee)
# class EmployeeAdmin(admin.ModelAdmin):
#     list_display = ("username", "job_title", "unit_or_program", "manager",)


# class SignatureReminderInline(admin.TabularInline):
#     model = SignatureReminder
#     fields = ("employee", "date", "next_date")
#     readonly_fields = ("date",)
#     extra = 0


# class SignatureInline(admin.TabularInline):
#     model = Signature
#     fields = ("employee", "date",)
#     readonly_fields = ("date",)
#     extra = 0


# @admin.register(PerformanceReview)
# class PerformanceReviewAdmin(admin.ModelAdmin):
#     list_display = ("username", "status", "effective_date")
#     inlines = (SignatureInline, SignatureReminderInline)


# @admin.register(ReviewNote)
# class ReviewNoteAdmin(admin.ModelAdmin):
#     list_display = ("manager", "employee", "date")
#     readonly_fields = ("date",)