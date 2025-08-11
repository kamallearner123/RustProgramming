from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import CodeExecution, CodeTemplate
import json
import subprocess
import tempfile
import os
import time
import uuid


def code_editor(request):
    """Main code editor page"""
    templates = CodeTemplate.objects.all()
    context = {
        'templates': templates,
    }
    return render(request, 'code_runner/editor.html', context)


@api_view(['POST'])
@permission_classes([AllowAny])
def execute_code(request):
    """Execute code in various languages"""
    try:
        data = request.data
        code = data.get('code', '')
        language = data.get('language', 'rust')
        input_data = data.get('input', '')
        
        if not code.strip():
            return Response({
                'success': False,
                'error': 'Code cannot be empty'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Create execution record
        execution = CodeExecution.objects.create(
            user=request.user if request.user.is_authenticated else None,
            session_id=str(uuid.uuid4()) if not request.user.is_authenticated else '',
            code=code,
            language=language,
            input_data=input_data,
            status='running'
        )
        
        try:
            # Execute the code
            result = run_code(code, language, input_data)
            
            # Update execution record
            execution.output = result.get('output', '')
            execution.error_output = result.get('error', '')
            execution.execution_time = result.get('execution_time', 0)
            execution.status = 'completed' if result.get('success') else 'error'
            execution.save()
            
            return Response({
                'success': result.get('success', False),
                'output': result.get('output', ''),
                'error': result.get('error', ''),
                'execution_time': result.get('execution_time', 0),
                'execution_id': execution.id
            })
            
        except Exception as e:
            execution.error_output = str(e)
            execution.status = 'error'
            execution.save()
            raise e
            
    except Exception as e:
        return Response({
            'success': False,
            'error': f'Execution failed: {str(e)}'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_templates(request):
    """Get code templates for different languages"""
    templates = CodeTemplate.objects.all()
    data = [{
        'id': template.id,
        'name': template.name,
        'language': template.language,
        'template_code': template.template_code,
        'description': template.description,
        'is_default': template.is_default,
    } for template in templates]
    return Response(data)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_template(request, language):
    """Get default template for a specific language"""
    try:
        template = CodeTemplate.objects.filter(
            language=language, 
            is_default=True
        ).first()
        
        if not template:
            # Return basic templates if no default found
            basic_templates = get_basic_templates()
            template_code = basic_templates.get(language, '')
        else:
            template_code = template.template_code
            
        return Response({
            'language': language,
            'template_code': template_code,
        })
    except Exception as e:
        return Response({
            'error': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def run_code(code, language, input_data=''):
    """Execute code in different languages"""
    start_time = time.time()
    
    try:
        if language == 'rust':
            return run_rust_code(code, input_data, start_time)
        elif language == 'python':
            return run_python_code(code, input_data, start_time)
        elif language == 'javascript':
            return run_javascript_code(code, input_data, start_time)
        elif language == 'go':
            return run_go_code(code, input_data, start_time)
        elif language == 'cpp':
            return run_cpp_code(code, input_data, start_time)
        else:
            return {
                'success': False,
                'error': f'Language {language} not supported',
                'execution_time': 0
            }
    except Exception as e:
        return {
            'success': False,
            'error': str(e),
            'execution_time': time.time() - start_time
        }


def run_rust_code(code, input_data, start_time):
    """Execute Rust code"""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create Cargo.toml
        cargo_toml = """[package]
name = "temp_rust"
version = "0.1.0"
edition = "2021"

[dependencies]
"""
        
        # Create source file
        src_dir = os.path.join(temp_dir, 'src')
        os.makedirs(src_dir)
        
        with open(os.path.join(temp_dir, 'Cargo.toml'), 'w') as f:
            f.write(cargo_toml)
            
        with open(os.path.join(src_dir, 'main.rs'), 'w') as f:
            f.write(code)
        
        try:
            # Compile
            compile_result = subprocess.run(
                ['cargo', 'build', '--release'],
                cwd=temp_dir,
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if compile_result.returncode != 0:
                return {
                    'success': False,
                    'error': f'Compilation error:\n{compile_result.stderr}',
                    'execution_time': time.time() - start_time
                }
            
            # Run
            run_result = subprocess.run(
                ['cargo', 'run', '--release'],
                cwd=temp_dir,
                input=input_data,
                capture_output=True,
                text=True,
                timeout=10
            )
            
            return {
                'success': run_result.returncode == 0,
                'output': run_result.stdout,
                'error': run_result.stderr if run_result.returncode != 0 else '',
                'execution_time': time.time() - start_time
            }
            
        except subprocess.TimeoutExpired:
            return {
                'success': False,
                'error': 'Code execution timed out',
                'execution_time': time.time() - start_time
            }


def run_python_code(code, input_data, start_time):
    """Execute Python code"""
    try:
        result = subprocess.run(
            ['python3', '-c', code],
            input=input_data,
            capture_output=True,
            text=True,
            timeout=10
        )
        
        return {
            'success': result.returncode == 0,
            'output': result.stdout,
            'error': result.stderr if result.returncode != 0 else '',
            'execution_time': time.time() - start_time
        }
    except subprocess.TimeoutExpired:
        return {
            'success': False,
            'error': 'Code execution timed out',
            'execution_time': time.time() - start_time
        }


def run_javascript_code(code, input_data, start_time):
    """Execute JavaScript code with Node.js"""
    try:
        # Wrap code to handle input
        wrapped_code = f"""
const readline = require('readline');
const rl = readline.createInterface({{
    input: process.stdin,
    output: process.stdout
}});

let inputData = `{input_data}`;
let inputLines = inputData.split('\\n');
let currentLine = 0;

function readLine() {{
    return inputLines[currentLine++] || '';
}}

{code}
"""
        
        result = subprocess.run(
            ['node', '-e', wrapped_code],
            input=input_data,
            capture_output=True,
            text=True,
            timeout=10
        )
        
        return {
            'success': result.returncode == 0,
            'output': result.stdout,
            'error': result.stderr if result.returncode != 0 else '',
            'execution_time': time.time() - start_time
        }
    except subprocess.TimeoutExpired:
        return {
            'success': False,
            'error': 'Code execution timed out',
            'execution_time': time.time() - start_time
        }


def run_go_code(code, input_data, start_time):
    """Execute Go code"""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.go', delete=False) as f:
        f.write(code)
        f.flush()
        
        try:
            result = subprocess.run(
                ['go', 'run', f.name],
                input=input_data,
                capture_output=True,
                text=True,
                timeout=10
            )
            
            return {
                'success': result.returncode == 0,
                'output': result.stdout,
                'error': result.stderr if result.returncode != 0 else '',
                'execution_time': time.time() - start_time
            }
        except subprocess.TimeoutExpired:
            return {
                'success': False,
                'error': 'Code execution timed out',
                'execution_time': time.time() - start_time
            }
        finally:
            os.unlink(f.name)


def run_cpp_code(code, input_data, start_time):
    """Execute C++ code"""
    with tempfile.TemporaryDirectory() as temp_dir:
        source_file = os.path.join(temp_dir, 'main.cpp')
        executable = os.path.join(temp_dir, 'main')
        
        with open(source_file, 'w') as f:
            f.write(code)
        
        try:
            # Compile
            compile_result = subprocess.run(
                ['g++', '-o', executable, source_file],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if compile_result.returncode != 0:
                return {
                    'success': False,
                    'error': f'Compilation error:\n{compile_result.stderr}',
                    'execution_time': time.time() - start_time
                }
            
            # Run
            run_result = subprocess.run(
                [executable],
                input=input_data,
                capture_output=True,
                text=True,
                timeout=10
            )
            
            return {
                'success': run_result.returncode == 0,
                'output': run_result.stdout,
                'error': run_result.stderr if run_result.returncode != 0 else '',
                'execution_time': time.time() - start_time
            }
            
        except subprocess.TimeoutExpired:
            return {
                'success': False,
                'error': 'Code execution timed out',
                'execution_time': time.time() - start_time
            }


def get_basic_templates():
    """Return basic code templates for different languages"""
    return {
        'rust': '''fn main() {
    println!("Hello, World!");
    
    // Your code here
}''',
        'python': '''def main():
    print("Hello, World!")
    
    # Your code here

if __name__ == "__main__":
    main()''',
        'javascript': '''function main() {
    console.log("Hello, World!");
    
    // Your code here
}

main();''',
        'go': '''package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
    
    // Your code here
}''',
        'cpp': '''#include <iostream>
using namespace std;

int main() {
    cout << "Hello, World!" << endl;
    
    // Your code here
    
    return 0;
}'''
    }
