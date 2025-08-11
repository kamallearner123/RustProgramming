from django.core.management.base import BaseCommand
from materials.models import Topic, Subtopic, Material, Question, Problem
from code_runner.models import CodeTemplate


class Command(BaseCommand):
    help = 'Populate database with Rust interview preparation content'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting to populate database...'))
        
        # Create topics
        topics_data = [
            {
                'day': 1,
                'title': 'System Design',
                'description': 'Learn scalable system design concepts including distributed systems, load balancing, and fault tolerance.',
                'subtopics': [
                    'Scalability and Load Balancing',
                    'Distributed Systems',
                    'Database Design and Caching',
                    'Microservices Architecture',
                    'System Reliability and Fault Tolerance'
                ],
                'questions': [
                    "How would you design a scalable web service using Rust?",
                    "Explain the role of load balancers in system design.",
                    "How can Rust's async features improve system scalability?",
                    "What are the key considerations for designing a distributed system?",
                    "How would you handle data consistency in a distributed system using Rust?",
                    "Describe the CAP theorem and its implications for system design.",
                    "How can Rust's ownership model help in designing fault-tolerant systems?",
                    "What is sharding, and how would you implement it in a Rust-based system?",
                    "Explain how you would use caching to improve system performance.",
                    "How does Rust's memory safety benefit database interactions?",
                    "Design a URL shortening service using Rust. What components would you include?",
                    "How would you handle rate limiting in a Rust-based API?",
                    "What are the trade-offs between monolithic and microservices architectures?",
                    "How can Rust's concurrency model support microservices?",
                    "Explain how you would design a system to handle high-throughput logging.",
                    "What strategies would you use to ensure high availability in a Rust system?",
                    "How would you implement a message queue in a Rust-based system?",
                    "Discuss the role of API gateways in system design.",
                    "How would you design a system to handle real-time data processing in Rust?",
                    "What are the challenges of integrating Rust with existing legacy systems?",
                    "How would you design a content delivery network (CDN) using Rust?",
                    "Explain the use of circuit breakers in system design with Rust."
                ]
            },
            {
                'day': 2,
                'title': 'Backend Concepts',
                'description': 'Master backend development concepts including APIs, authentication, database interactions, and performance optimization.',
                'subtopics': [
                    'REST and GraphQL APIs',
                    'Authentication and Authorization',
                    'Database Interactions',
                    'Middleware and Request Handling',
                    'Performance Optimization'
                ],
                'questions': [
                    "What is the difference between REST and GraphQL APIs in Rust?",
                    "How would you implement JWT authentication in a Rust backend?",
                    "Explain how Rust's async/await works in backend development.",
                    "How do you handle database connections in a Rust backend?",
                    "What are the benefits of using Actix Web for backend development?",
                    "How would you implement OAuth2 in a Rust-based application?",
                    "Describe how to handle CORS in a Rust backend.",
                    "How can Rust's type system improve backend API reliability?",
                    "What is connection pooling, and how is it implemented in Rust?",
                    "How would you optimize database queries in a Rust backend?",
                    "Explain the role of middleware in a Rust web framework.",
                    "How do you handle errors in a Rust backend application?",
                    "What are the advantages of using Diesel for database operations in Rust?",
                    "How would you implement rate limiting in a Rust backend?",
                    "Describe how to secure API endpoints in a Rust application.",
                    "How do you handle file uploads in a Rust backend?",
                    "What is the role of serde in Rust backend development?",
                    "How would you implement WebSockets in a Rust backend?",
                    "Explain how to use environment variables in a Rust backend.",
                    "How do you test a Rust backend application?",
                    "What are the challenges of handling large payloads in Rust APIs?",
                    "How would you implement logging in a Rust backend?"
                ]
            },
            {
                'day': 3,
                'title': 'Rust Internals',
                'description': 'Deep dive into Rust internals including ownership, borrowing, lifetimes, memory management, and concurrency.',
                'subtopics': [
                    'Ownership and Borrowing',
                    'Lifetimes',
                    'Memory Management',
                    'Concurrency Model',
                    'Unsafe Rust'
                ],
                'questions': [
                    "What is the ownership model in Rust, and why is it important?",
                    "Explain the concept of borrowing in Rust.",
                    "How do lifetimes work in Rust?",
                    "What are the differences between &str and String in Rust?",
                    "How does Rust ensure memory safety without a garbage collector?",
                    "What is the purpose of the unsafe keyword in Rust?",
                    "Explain the role of the borrow checker in Rust.",
                    "How does Rust handle stack vs. heap memory allocation?",
                    "What is a reference-counted pointer (Rc) in Rust?",
                    "Explain the Arc type and its use in concurrent programming.",
                    "How does Rust's mutex differ from other languages?",
                    "What are the benefits of Rust's zero-cost abstractions?",
                    "How does Rust handle memory leaks?",
                    "Explain the concept of a lifetime annotation in Rust.",
                    "What is the difference between Box<T> and Rc<T>?",
                    "How does Rust's concurrency model prevent data races?",
                    "What is the role of the Send and Sync traits in Rust?",
                    "How does Rust optimize memory usage in high-performance systems?",
                    "Explain the use of Cell and RefCell in Rust.",
                    "What are the risks of using unsafe Rust code?",
                    "How does Rust handle raw pointers?",
                    "Explain the concept of interior mutability in Rust."
                ]
            },
            {
                'day': 4,
                'title': 'Rust Programming',
                'description': 'Practice Rust programming fundamentals including syntax, error handling, traits, generics, and testing.',
                'subtopics': [
                    'Basic Syntax and Semantics',
                    'Error Handling',
                    'Traits and Generics',
                    'Modules and Crates',
                    'Testing in Rust'
                ],
                'questions': [
                    "What is the difference between let and let mut in Rust?",
                    "How does Rust's match expression work?",
                    "Explain the Result and Option types in Rust.",
                    "How do you create a custom error type in Rust?",
                    "What are traits in Rust, and how are they used?",
                    "Explain generics in Rust with an example.",
                    "How do you organize code using modules in Rust?",
                    "What is a crate in Rust, and how is it different from a module?",
                    "How do you write unit tests in Rust?",
                    "Explain the use of the #[derive] attribute in Rust.",
                    "How do you handle string manipulation in Rust?",
                    "What is the purpose of the Cargo tool in Rust?",
                    "How do you implement a trait for a custom type?",
                    "Explain the concept of closures in Rust.",
                    "How do you use iterators in Rust?",
                    "What is the difference between Vec<T> and &[T]?",
                    "How do you handle file I/O in Rust?",
                    "Explain the use of macros in Rust.",
                    "How do you implement a simple HTTP client in Rust?",
                    "What are the best practices for error handling in Rust?",
                    "How do you use the tokio crate for async programming?",
                    "Explain the role of the cfg attribute in Rust."
                ]
            }
        ]
        
        for topic_data in topics_data:
            topic, created = Topic.objects.get_or_create(
                day_number=topic_data['day'],
                defaults={
                    'title': topic_data['title'],
                    'description': topic_data['description'],
                    'order': topic_data['day']
                }
            )
            
            if created:
                self.stdout.write(f"Created topic: {topic.title}")
                
                # Create subtopics
                for i, subtopic_title in enumerate(topic_data['subtopics']):
                    subtopic, sub_created = Subtopic.objects.get_or_create(
                        topic=topic,
                        title=subtopic_title,
                        defaults={
                            'description': f"Learn about {subtopic_title.lower()} in {topic.title.lower()}",
                            'order': i + 1
                        }
                    )
                    if sub_created:
                        self.stdout.write(f"  Created subtopic: {subtopic.title}")
                
                # Create questions
                for i, question_text in enumerate(topic_data['questions']):
                    question, q_created = Question.objects.get_or_create(
                        topic=topic,
                        question_text=question_text,
                        defaults={
                            'order': i + 1,
                            'difficulty': 'medium' if i % 3 == 0 else 'easy' if i % 3 == 1 else 'hard'
                        }
                    )
                    if q_created:
                        self.stdout.write(f"  Created question {i+1}")
        
        # Create some practice problems
        problems_data = [
            {
                'topic_day': 1,
                'title': 'Design a URL Shortener',
                'description': '''Design and implement a URL shortener service like bit.ly.

Requirements:
- Shorten long URLs to short codes
- Redirect short codes to original URLs
- Handle high traffic (millions of URLs)
- Provide analytics (click counts)

Consider:
- Database schema design
- Scalability concerns
- Caching strategies
- Rate limiting''',
                'starter_code': '''// URL Shortener Service
use std::collections::HashMap;

struct UrlShortener {
    // TODO: Define your data structure
}

impl UrlShortener {
    fn new() -> Self {
        // TODO: Initialize the service
        todo!()
    }
    
    fn shorten(&mut self, long_url: String) -> String {
        // TODO: Implement URL shortening logic
        todo!()
    }
    
    fn expand(&self, short_code: &str) -> Option<String> {
        // TODO: Implement URL expansion logic
        todo!()
    }
}

fn main() {
    let mut shortener = UrlShortener::new();
    let short_url = shortener.shorten("https://www.example.com/very/long/url".to_string());
    println!("Short URL: {}", short_url);
    
    if let Some(original) = shortener.expand(&short_url) {
        println!("Original URL: {}", original);
    }
}''',
                'difficulty': 'hard'
            },
            {
                'topic_day': 2,
                'title': 'JWT Authentication Middleware',
                'description': '''Implement JWT authentication middleware for a Rust web service.

Requirements:
- Parse and validate JWT tokens
- Extract user information from tokens
- Handle token expiration
- Secure route protection

The middleware should:
- Check Authorization header
- Validate token signature
- Check expiration
- Pass user info to handlers''',
                'starter_code': '''use std::collections::HashMap;

#[derive(Debug)]
struct Claims {
    user_id: String,
    username: String,
    exp: u64,  // expiration timestamp
}

struct JwtMiddleware {
    secret: String,
}

impl JwtMiddleware {
    fn new(secret: String) -> Self {
        Self { secret }
    }
    
    fn validate_token(&self, token: &str) -> Result<Claims, String> {
        // TODO: Implement JWT validation
        // 1. Parse the token
        // 2. Verify signature
        // 3. Check expiration
        // 4. Return claims
        todo!()
    }
    
    fn extract_token_from_header(&self, auth_header: &str) -> Option<String> {
        // TODO: Extract token from "Bearer <token>" format
        todo!()
    }
}

fn main() {
    let middleware = JwtMiddleware::new("secret_key".to_string());
    
    // Simulate request with Authorization header
    let auth_header = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...";
    
    if let Some(token) = middleware.extract_token_from_header(auth_header) {
        match middleware.validate_token(&token) {
            Ok(claims) => println!("Valid token for user: {}", claims.username),
            Err(e) => println!("Invalid token: {}", e),
        }
    }
}''',
                'difficulty': 'medium'
            },
            {
                'topic_day': 3,
                'title': 'Custom Smart Pointer',
                'description': '''Implement a custom smart pointer that provides reference counting with weak references.

Requirements:
- Implement Rc-like behavior
- Support weak references to break cycles
- Handle proper cleanup when ref count reaches zero
- Implement Clone for the smart pointer

Your implementation should demonstrate understanding of:
- Rust's ownership system
- Interior mutability
- Reference counting
- Memory management''',
                'starter_code': '''use std::cell::RefCell;
use std::rc::{Rc, Weak};

struct MyRc<T> {
    // TODO: Define your smart pointer structure
}

struct MyWeak<T> {
    // TODO: Define weak reference structure
}

impl<T> MyRc<T> {
    fn new(value: T) -> Self {
        // TODO: Create new MyRc
        todo!()
    }
    
    fn downgrade(&self) -> MyWeak<T> {
        // TODO: Create weak reference
        todo!()
    }
    
    fn strong_count(&self) -> usize {
        // TODO: Return strong reference count
        todo!()
    }
}

impl<T> MyWeak<T> {
    fn upgrade(&self) -> Option<MyRc<T>> {
        // TODO: Try to upgrade to strong reference
        todo!()
    }
}

impl<T> Clone for MyRc<T> {
    fn clone(&self) -> Self {
        // TODO: Implement cloning with ref count increment
        todo!()
    }
}

impl<T> Drop for MyRc<T> {
    fn drop(&mut self) {
        // TODO: Implement proper cleanup
        todo!()
    }
}

fn main() {
    let rc1 = MyRc::new(42);
    let rc2 = rc1.clone();
    let weak = rc1.downgrade();
    
    println!("Strong count: {}", rc1.strong_count());
    
    drop(rc1);
    drop(rc2);
    
    // weak should not be upgradeable now
    assert!(weak.upgrade().is_none());
}''',
                'difficulty': 'hard'
            },
            {
                'topic_day': 4,
                'title': 'Generic Data Structure',
                'description': '''Implement a generic binary search tree with iterator support.

Requirements:
- Generic over any type that implements Ord
- Support insert, find, and delete operations
- Implement an iterator that traverses in order
- Handle edge cases properly

Bonus:
- Implement Display trait for pretty printing
- Add methods for tree traversal (preorder, postorder)
- Balance the tree (convert to AVL or Red-Black tree)''',
                'starter_code': '''use std::cmp::Ordering;
use std::fmt::Display;

#[derive(Debug)]
struct BinarySearchTree<T> {
    root: Option<Box<Node<T>>>,
}

#[derive(Debug)]
struct Node<T> {
    value: T,
    left: Option<Box<Node<T>>>,
    right: Option<Box<Node<T>>>,
}

impl<T: Ord> BinarySearchTree<T> {
    fn new() -> Self {
        Self { root: None }
    }
    
    fn insert(&mut self, value: T) {
        // TODO: Implement insertion
        todo!()
    }
    
    fn find(&self, value: &T) -> bool {
        // TODO: Implement search
        todo!()
    }
    
    fn delete(&mut self, value: &T) -> bool {
        // TODO: Implement deletion
        todo!()
    }
    
    fn iter(&self) -> BSTIterator<T> {
        // TODO: Return iterator for in-order traversal
        todo!()
    }
}

struct BSTIterator<T> {
    // TODO: Define iterator state
}

impl<T> Iterator for BSTIterator<T> {
    type Item = &T;
    
    fn next(&mut self) -> Option<Self::Item> {
        // TODO: Implement in-order traversal
        todo!()
    }
}

fn main() {
    let mut bst = BinarySearchTree::new();
    
    // Insert some values
    bst.insert(5);
    bst.insert(3);
    bst.insert(7);
    bst.insert(1);
    bst.insert(9);
    
    // Test find
    assert!(bst.find(&5));
    assert!(!bst.find(&10));
    
    // Test iterator
    let values: Vec<_> = bst.iter().collect();
    println!("In-order traversal: {:?}", values);
}''',
                'difficulty': 'medium'
            }
        ]
        
        for problem_data in problems_data:
            topic = Topic.objects.get(day_number=problem_data['topic_day'])
            problem, created = Problem.objects.get_or_create(
                topic=topic,
                title=problem_data['title'],
                defaults={
                    'description': problem_data['description'],
                    'starter_code': problem_data['starter_code'],
                    'difficulty': problem_data['difficulty'],
                    'language': 'rust',
                    'test_cases': [
                        {'input': '', 'output': 'Compilation successful'},
                    ]
                }
            )
            if created:
                self.stdout.write(f"Created problem: {problem.title}")
        
        # Create code templates
        templates_data = [
            {
                'name': 'Rust Hello World',
                'language': 'rust',
                'is_default': True,
                'template_code': '''fn main() {
    println!("Hello, World!");
    
    // Your code here
}''',
                'description': 'Basic Rust program template'
            },
            {
                'name': 'Python Basic',
                'language': 'python',
                'is_default': True,
                'template_code': '''def main():
    print("Hello, World!")
    
    # Your code here

if __name__ == "__main__":
    main()''',
                'description': 'Basic Python program template'
            },
            {
                'name': 'JavaScript Basic',
                'language': 'javascript',
                'is_default': True,
                'template_code': '''function main() {
    console.log("Hello, World!");
    
    // Your code here
}

main();''',
                'description': 'Basic JavaScript program template'
            }
        ]
        
        for template_data in templates_data:
            template, created = CodeTemplate.objects.get_or_create(
                name=template_data['name'],
                language=template_data['language'],
                defaults={
                    'template_code': template_data['template_code'],
                    'description': template_data['description'],
                    'is_default': template_data['is_default']
                }
            )
            if created:
                self.stdout.write(f"Created template: {template.name}")
        
        self.stdout.write(self.style.SUCCESS('Database populated successfully!'))
        self.stdout.write(f"Created {Topic.objects.count()} topics")
        self.stdout.write(f"Created {Subtopic.objects.count()} subtopics")
        self.stdout.write(f"Created {Question.objects.count()} questions")
        self.stdout.write(f"Created {Problem.objects.count()} problems")
        self.stdout.write(f"Created {CodeTemplate.objects.count()} code templates")
