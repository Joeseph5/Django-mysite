from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': [
         'pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    # add column name
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # add question filter by date
    list_filter = ['pub_date']
    # add question search box
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)