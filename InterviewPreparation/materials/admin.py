from django.contrib import admin
from .models import Topic, Subtopic, Material, Question, Problem, UserProgress, CodeSubmission


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['title', 'day_number', 'order', 'created_at']
    list_filter = ['day_number']
    ordering = ['day_number', 'order']


@admin.register(Subtopic)
class SubtopicAdmin(admin.ModelAdmin):
    list_display = ['title', 'topic', 'order']
    list_filter = ['topic']
    ordering = ['topic__day_number', 'order']


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtopic', 'material_type', 'language', 'order']
    list_filter = ['material_type', 'language', 'subtopic__topic']
    search_fields = ['title', 'content']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text_short', 'topic', 'difficulty', 'order']
    list_filter = ['difficulty', 'topic']
    search_fields = ['question_text']
    
    def question_text_short(self, obj):
        return obj.question_text[:50] + "..." if len(obj.question_text) > 50 else obj.question_text
    question_text_short.short_description = 'Question'


@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ['title', 'topic', 'difficulty', 'language', 'time_limit']
    list_filter = ['difficulty', 'language', 'topic']
    search_fields = ['title', 'description']


@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = ['user', 'topic', 'subtopic', 'completed', 'completion_date']
    list_filter = ['completed', 'topic']
    search_fields = ['user__username']


@admin.register(CodeSubmission)
class CodeSubmissionAdmin(admin.ModelAdmin):
    list_display = ['user', 'problem', 'language', 'passed_tests', 'total_tests', 'submitted_at']
    list_filter = ['language', 'submitted_at']
    search_fields = ['user__username', 'problem__title']
