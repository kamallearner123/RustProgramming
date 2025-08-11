from django.db import models
from django.contrib.auth.models import User


class CodeExecution(models.Model):
    """Store code execution history"""
    LANGUAGES = [
        ('rust', 'Rust'),
        ('python', 'Python'),
        ('javascript', 'JavaScript'),
        ('go', 'Go'),
        ('cpp', 'C++'),
    ]
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('running', 'Running'),
        ('completed', 'Completed'),
        ('error', 'Error'),
        ('timeout', 'Timeout'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    session_id = models.CharField(max_length=100, blank=True)
    code = models.TextField()
    language = models.CharField(max_length=20, choices=LANGUAGES, default='rust')
    input_data = models.TextField(blank=True)
    output = models.TextField(blank=True)
    error_output = models.TextField(blank=True)
    execution_time = models.FloatField(null=True, blank=True)
    memory_usage = models.IntegerField(null=True, blank=True)  # in KB
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        user_info = self.user.username if self.user else self.session_id
        return f"{user_info} - {self.language} - {self.status}"


class CodeTemplate(models.Model):
    """Pre-defined code templates for different languages"""
    name = models.CharField(max_length=200)
    language = models.CharField(max_length=20)
    template_code = models.TextField()
    description = models.TextField(blank=True)
    is_default = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ['language', 'is_default']

    def __str__(self):
        return f"{self.name} ({self.language})"
