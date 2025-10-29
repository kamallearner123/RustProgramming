// Rust Syntax Highlighter
document.addEventListener('DOMContentLoaded', function() {
    const codeBlocks = document.querySelectorAll('.code-block');
    
    const rustKeywords = [
        'fn', 'let', 'mut', 'const', 'static', 'if', 'else', 'match', 'loop', 'while', 
        'for', 'in', 'break', 'continue', 'return', 'pub', 'mod', 'use', 'as', 'struct',
        'enum', 'trait', 'impl', 'type', 'where', 'async', 'await', 'move', 'ref',
        'unsafe', 'extern', 'crate', 'super', 'self', 'Self', 'true', 'false'
    ];
    
    const rustTypes = [
        'i8', 'i16', 'i32', 'i64', 'i128', 'isize',
        'u8', 'u16', 'u32', 'u64', 'u128', 'usize',
        'f32', 'f64', 'bool', 'char', 'str', 'String',
        'Vec', 'Option', 'Result', 'Box', 'Rc', 'Arc'
    ];
    
    codeBlocks.forEach(block => {
        let code = block.textContent;
        
        // Escape HTML
        code = code.replace(/&/g, '&amp;')
                   .replace(/</g, '&lt;')
                   .replace(/>/g, '&gt;');
        
        // Highlight comments (// and /* */)
        code = code.replace(/(\/\/.*$)/gm, '<span class="comment">$1</span>');
        code = code.replace(/(\/\*[\s\S]*?\*\/)/g, '<span class="comment">$1</span>');
        
        // Highlight strings
        code = code.replace(/("(?:[^"\\]|\\.)*")/g, '<span class="string">$1</span>');
        code = code.replace(/('(?:[^'\\]|\\.)*')/g, '<span class="string">$1</span>');
        
        // Highlight numbers
        code = code.replace(/\b(\d+\.?\d*)\b/g, '<span class="number">$1</span>');
        
        // Highlight macros (println!, vec!, etc.)
        code = code.replace(/\b(\w+!)/g, '<span class="macro">$1</span>');
        
        // Highlight types
        rustTypes.forEach(type => {
            const regex = new RegExp('\\b(' + type + ')\\b', 'g');
            code = code.replace(regex, '<span class="type">$1</span>');
        });
        
        // Highlight keywords
        rustKeywords.forEach(keyword => {
            const regex = new RegExp('\\b(' + keyword + ')\\b', 'g');
            code = code.replace(regex, '<span class="keyword">$1</span>');
        });
        
        // Highlight function names (word followed by ()
        code = code.replace(/\b([a-z_]\w*)\s*\(/g, '<span class="function">$1</span>(');
        
        block.innerHTML = code;
    });
});
