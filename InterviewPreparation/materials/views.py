from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import Topic, Subtopic, Material, Question, Problem, UserProgress, CodeSubmission
import json


def home(request):
    """Home page showing all topics"""
    topics = Topic.objects.all().prefetch_related('subtopics', 'questions', 'problems')
    context = {
        'topics': topics
    }
    return render(request, 'materials/home.html', context)


def topic_detail(request, topic_id):
    """Detailed view of a specific topic"""
    topic = get_object_or_404(Topic, id=topic_id)
    subtopics = topic.subtopics.all().prefetch_related('materials', 'questions', 'problems')
    questions = topic.questions.all()
    problems = topic.problems.all()
    
    context = {
        'topic': topic,
        'subtopics': subtopics,
        'questions': questions,
        'problems': problems,
    }
    return render(request, 'materials/topic_detail.html', context)


def subtopic_detail(request, subtopic_id):
    """Detailed view of a specific subtopic"""
    subtopic = get_object_or_404(Subtopic, id=subtopic_id)
    materials = subtopic.materials.all()
    questions = subtopic.questions.all()
    problems = subtopic.problems.all()
    
    context = {
        'subtopic': subtopic,
        'materials': materials,
        'questions': questions,
        'problems': problems,
    }
    return render(request, 'materials/subtopic_detail.html', context)


def problem_detail(request, problem_id):
    """Detailed view of a coding problem with editor"""
    problem = get_object_or_404(Problem, id=problem_id)
    user_submissions = []
    if request.user.is_authenticated:
        user_submissions = CodeSubmission.objects.filter(
            user=request.user, 
            problem=problem
        ).order_by('-submitted_at')[:5]
    
    context = {
        'problem': problem,
        'user_submissions': user_submissions,
    }
    return render(request, 'materials/problem_detail.html', context)


def practice_problems(request):
    """List all practice problems"""
    problems = Problem.objects.all().select_related('topic', 'subtopic')
    difficulty = request.GET.get('difficulty')
    topic_id = request.GET.get('topic')
    
    if difficulty:
        problems = problems.filter(difficulty=difficulty)
    if topic_id:
        problems = problems.filter(topic_id=topic_id)
    
    topics = Topic.objects.all()
    
    context = {
        'problems': problems,
        'topics': topics,
        'current_difficulty': difficulty,
        'current_topic': topic_id,
    }
    return render(request, 'materials/practice_problems.html', context)


# API Views
@api_view(['GET'])
@permission_classes([AllowAny])
def api_topics(request):
    """API endpoint to get all topics"""
    topics = Topic.objects.all()
    data = [{
        'id': topic.id,
        'title': topic.title,
        'description': topic.description,
        'day_number': topic.day_number,
        'subtopics_count': topic.subtopics.count(),
        'questions_count': topic.questions.count(),
        'problems_count': topic.problems.count(),
    } for topic in topics]
    return Response(data)


@api_view(['GET'])
@permission_classes([AllowAny])
def api_topic_detail(request, topic_id):
    """API endpoint to get topic details"""
    topic = get_object_or_404(Topic, id=topic_id)
    subtopics = [{
        'id': st.id,
        'title': st.title,
        'description': st.description,
        'materials_count': st.materials.count(),
    } for st in topic.subtopics.all()]
    
    questions = [{
        'id': q.id,
        'question_text': q.question_text,
        'difficulty': q.difficulty,
        'hints': q.hints,
    } for q in topic.questions.all()]
    
    problems = [{
        'id': p.id,
        'title': p.title,
        'description': p.description,
        'difficulty': p.difficulty,
        'language': p.language,
    } for p in topic.problems.all()]
    
    data = {
        'id': topic.id,
        'title': topic.title,
        'description': topic.description,
        'day_number': topic.day_number,
        'subtopics': subtopics,
        'questions': questions,
        'problems': problems,
    }
    return Response(data)


@api_view(['GET'])
@permission_classes([AllowAny])
def api_problem_detail(request, problem_id):
    """API endpoint to get problem details"""
    problem = get_object_or_404(Problem, id=problem_id)
    data = {
        'id': problem.id,
        'title': problem.title,
        'description': problem.description,
        'starter_code': problem.starter_code,
        'test_cases': problem.test_cases,
        'difficulty': problem.difficulty,
        'language': problem.language,
        'time_limit': problem.time_limit,
        'topic': problem.topic.title,
        'subtopic': problem.subtopic.title if problem.subtopic else None,
    }
    return Response(data)


@api_view(['POST'])
@permission_classes([AllowAny])
def api_submit_code(request):
    """API endpoint to submit code for a problem"""
    try:
        data = request.data
        problem_id = data.get('problem_id')
        code = data.get('code')
        language = data.get('language', 'rust')
        
        problem = get_object_or_404(Problem, id=problem_id)
        
        # Create code submission
        submission = CodeSubmission.objects.create(
            user=request.user if request.user.is_authenticated else None,
            problem=problem,
            code=code,
            language=language,
        )
        
        # TODO: Implement actual code execution
        # For now, we'll simulate the result
        passed_tests = len(problem.test_cases) if problem.test_cases else 0
        submission.passed_tests = passed_tests
        submission.total_tests = passed_tests
        submission.execution_result = {
            'status': 'success',
            'output': 'Code executed successfully',
            'execution_time': 0.1
        }
        submission.save()
        
        return Response({
            'success': True,
            'submission_id': submission.id,
            'passed_tests': submission.passed_tests,
            'total_tests': submission.total_tests,
            'execution_result': submission.execution_result,
        })
        
    except Exception as e:
        return Response({
            'success': False,
            'error': str(e)
        }, status=status.HTTP_400_BAD_REQUEST)
