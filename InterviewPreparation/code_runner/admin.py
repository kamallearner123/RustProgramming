from django.contrib import admin
from .models import CodeExecution, CodeTemplate


@admin.register(CodeExecution)
class CodeExecutionAdmin(admin.ModelAdmin):
    list_display = ['user_or_session', 'language', 'status', 'execution_time', 'created_at']
    list_filter = ['language', 'status', 'created_at']
    search_fields = ['user__username', 'session_id']
    readonly_fields = ['created_at']
    
    def user_or_session(self, obj):
        return obj.user.username if obj.user else f"Session: {obj.session_id}"
    user_or_session.short_description = 'User/Session'


@admin.register(CodeTemplate)
class CodeTemplateAdmin(admin.ModelAdmin):
    list_display = ['name', 'language', 'is_default']
    list_filter = ['language', 'is_default']
    search_fields = ['name', 'description']
