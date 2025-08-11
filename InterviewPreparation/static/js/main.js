// Global JavaScript utilities and functions

// CSRF Token handling
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Setup CSRF token for AJAX requests
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    }
});

// Utility Functions
const Utils = {
    // Show loading state
    showLoading: function(element, text = 'Loading...') {
        const originalText = element.html();
        element.data('original-text', originalText);
        element.prop('disabled', true).html(`<i class="fas fa-spinner fa-spin"></i> ${text}`);
    },

    // Hide loading state
    hideLoading: function(element) {
        const originalText = element.data('original-text');
        element.prop('disabled', false).html(originalText);
    },

    // Show notification
    showNotification: function(message, type = 'info') {
        const alertClass = `alert-${type}`;
        const iconClass = {
            'success': 'fas fa-check-circle',
            'danger': 'fas fa-exclamation-triangle',
            'warning': 'fas fa-exclamation-circle',
            'info': 'fas fa-info-circle'
        }[type] || 'fas fa-info-circle';

        const notification = $(`
            <div class="alert ${alertClass} alert-dismissible fade show" role="alert">
                <i class="${iconClass}"></i> ${message}
                <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
            </div>
        `);

        $('main .container').prepend(notification);
        
        // Auto-dismiss after 5 seconds
        setTimeout(() => {
            notification.alert('close');
        }, 5000);
    },

    // Format execution time
    formatTime: function(seconds) {
        if (seconds < 1) {
            return `${(seconds * 1000).toFixed(0)}ms`;
        }
        return `${seconds.toFixed(2)}s`;
    },

    // Debounce function
    debounce: function(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }
};

// Code Editor utilities
const CodeEditorUtils = {
    // Language mode mapping for CodeMirror
    languageModes: {
        'rust': 'rust',
        'python': 'python',
        'javascript': 'javascript',
        'go': 'go',
        'cpp': 'text/x-c++src',
        'c': 'text/x-csrc',
        'java': 'text/x-java'
    },

    // Default templates
    defaultTemplates: {
        'rust': `fn main() {
    println!("Hello, World!");
    
    // Your code here
}`,
        'python': `def main():
    print("Hello, World!")
    
    # Your code here

if __name__ == "__main__":
    main()`,
        'javascript': `function main() {
    console.log("Hello, World!");
    
    // Your code here
}

main();`,
        'go': `package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
    
    // Your code here
}`,
        'cpp': `#include <iostream>
using namespace std;

int main() {
    cout << "Hello, World!" << endl;
    
    // Your code here
    
    return 0;
}`
    },

    // Initialize CodeMirror editor
    initializeEditor: function(textareaId, language = 'rust') {
        const textarea = document.getElementById(textareaId);
        if (!textarea) return null;

        return CodeMirror.fromTextArea(textarea, {
            mode: this.languageModes[language] || 'text',
            theme: 'monokai',
            lineNumbers: true,
            indentUnit: 4,
            lineWrapping: true,
            autoCloseBrackets: true,
            matchBrackets: true,
            extraKeys: {
                "Ctrl-Space": "autocomplete",
                "F11": function(cm) {
                    cm.setOption("fullScreen", !cm.getOption("fullScreen"));
                },
                "Esc": function(cm) {
                    if (cm.getOption("fullScreen")) cm.setOption("fullScreen", false);
                }
            }
        });
    },

    // Change editor language
    changeLanguage: function(editor, language) {
        if (editor && this.languageModes[language]) {
            editor.setOption('mode', this.languageModes[language]);
        }
    },

    // Load template for language
    loadTemplate: function(editor, language) {
        if (editor && this.defaultTemplates[language]) {
            editor.setValue(this.defaultTemplates[language]);
        }
    }
};

// API utilities
const API = {
    // Execute code
    executeCode: function(code, language, input = '') {
        return $.ajax({
            url: '/api/code/api/execute/',
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            data: JSON.stringify({
                code: code,
                language: language,
                input: input
            })
        });
    },

    // Submit code for problem
    submitCode: function(problemId, code, language) {
        return $.ajax({
            url: '/api/submit/',
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            data: JSON.stringify({
                problem_id: problemId,
                code: code,
                language: language
            })
        });
    },

    // Get template for language
    getTemplate: function(language) {
        return $.get(`/api/code/api/template/${language}/`);
    },

    // Get problem details
    getProblem: function(problemId) {
        return $.get(`/api/problem/${problemId}/`);
    }
};

// DOM Ready
$(document).ready(function() {
    // Initialize tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Initialize popovers
    const popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });

    // Smooth scrolling for anchor links
    $('a[href^="#"]').on('click', function(event) {
        const target = $(this.getAttribute('href'));
        if (target.length) {
            event.preventDefault();
            $('html, body').stop().animate({
                scrollTop: target.offset().top - 100
            }, 1000);
        }
    });

    // Auto-resize textareas
    $('textarea').on('input', function() {
        this.style.height = 'auto';
        this.style.height = (this.scrollHeight) + 'px';
    });

    // Add fade-in animation to cards
    $('.card').addClass('fade-in');

    // Handle responsive navigation
    $('.navbar-toggler').on('click', function() {
        $('.navbar-collapse').toggleClass('show');
    });
});

// Export for global use
window.Utils = Utils;
window.CodeEditorUtils = CodeEditorUtils;
window.API = API;
