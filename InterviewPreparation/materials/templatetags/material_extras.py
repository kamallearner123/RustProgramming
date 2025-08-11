from django import template

register = template.Library()

@register.filter
def get_difficulty_color(difficulty):
    """Return Bootstrap color class for difficulty level"""
    color_map = {
        'easy': 'success',
        'medium': 'warning', 
        'hard': 'danger'
    }
    return color_map.get(difficulty, 'secondary')

@register.filter
def get_material_type_icon(material_type):
    """Return Font Awesome icon for material type"""
    icon_map = {
        'concept': 'fas fa-lightbulb',
        'example': 'fas fa-code',
        'tutorial': 'fas fa-book-open',
        'reference': 'fas fa-bookmark'
    }
    return icon_map.get(material_type, 'fas fa-file')

@register.filter
def truncate_code(code, length=100):
    """Truncate code while preserving structure"""
    if len(code) <= length:
        return code
    return code[:length] + '...'
