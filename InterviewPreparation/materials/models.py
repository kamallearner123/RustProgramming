from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    """Main topic areas like System Design, Backend Concepts, etc."""
    title = models.CharField(max_length=200)
    description = models.TextField()
    day_number = models.IntegerField()
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['day_number', 'order']

    def __str__(self):
        return f"Day {self.day_number}: {self.title}"


class Subtopic(models.Model):
    """Subtopics within each main topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='subtopics')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.topic.title} - {self.title}"


class Material(models.Model):
    """Study materials for each subtopic"""
    MATERIAL_TYPES = [
        ('concept', 'Concept Explanation'),
        ('example', 'Example'),
        ('tutorial', 'Tutorial'),
        ('reference', 'Reference'),
    ]
    
    subtopic = models.ForeignKey(Subtopic, on_delete=models.CASCADE, related_name='materials')
    title = models.CharField(max_length=200)
    content = models.TextField()
    material_type = models.CharField(max_length=20, choices=MATERIAL_TYPES, default='concept')
    code_example = models.TextField(blank=True)
    language = models.CharField(max_length=50, default='rust')
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.subtopic.title} - {self.title}"


class Question(models.Model):
    """Interview questions for each topic"""
    DIFFICULTY_LEVELS = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]
    
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='questions')
    subtopic = models.ForeignKey(Subtopic, on_delete=models.CASCADE, related_name='questions', null=True, blank=True)
    question_text = models.TextField()
    expected_answer = models.TextField(blank=True)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_LEVELS, default='medium')
    hints = models.TextField(blank=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Q{self.order}: {self.question_text[:50]}..."


class Problem(models.Model):
    """Coding problems for practice"""
    DIFFICULTY_LEVELS = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]
    
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='problems')
    subtopic = models.ForeignKey(Subtopic, on_delete=models.CASCADE, related_name='problems', null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    starter_code = models.TextField(blank=True)
    solution = models.TextField(blank=True)
    test_cases = models.JSONField(default=list)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_LEVELS, default='medium')
    language = models.CharField(max_length=50, default='rust')
    time_limit = models.IntegerField(default=30)  # minutes
    
    def __str__(self):
        return f"{self.title} ({self.difficulty})"


class UserProgress(models.Model):
    """Track user progress through materials"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    subtopic = models.ForeignKey(Subtopic, on_delete=models.CASCADE, null=True, blank=True)
    material = models.ForeignKey(Material, on_delete=models.CASCADE, null=True, blank=True)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, null=True, blank=True)
    completed = models.BooleanField(default=False)
    completion_date = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(blank=True)
    
    class Meta:
        unique_together = ['user', 'topic', 'subtopic', 'material', 'problem']


class CodeSubmission(models.Model):
    """Store user code submissions"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    code = models.TextField()
    language = models.CharField(max_length=50, default='rust')
    submitted_at = models.DateTimeField(auto_now_add=True)
    execution_result = models.JSONField(null=True, blank=True)
    passed_tests = models.IntegerField(default=0)
    total_tests = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-submitted_at']

    def __str__(self):
        return f"{self.user.username} - {self.problem.title} - {self.submitted_at}"
