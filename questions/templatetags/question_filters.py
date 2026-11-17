import re
from django import template
from django.utils.html import escape
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def format_roman_numerals(text):
    """
    Parse and format Roman numeral sub-statements (i., ii., iii., iv., v.)
    to render on separate lines with proper indentation.
    
    Example:
        Input: "Which statements are true? i. Statement one ii. Statement two iii. Statement three"
        Output: "Which statements are true? <br><span class='roman-item'>i. Statement one</span>
                 <br><span class='roman-item'>ii. Statement two</span>
                 <br><span class='roman-item'>iii. Statement three</span>"
    """
    if not text:
        return text
    
    # Escape HTML in the input
    text = escape(text)
    
    # Pattern to match Roman numerals followed by a period and space at word boundaries
    # Matches: i., ii., iii., iv., v., vi., etc.
    # Non-capturing version to avoid duplicate parts in split
    pattern = r'\b(?:i{1,3}|iv|v|vi{1,3}|ix|x{1,3}|xl|l|lx{1,3}|xc|c)\.\s+'
    
    # Use a lookahead to split without consuming the Roman numeral
    parts = re.split(f'(?={pattern})', text)
    
    result = []
    for i, part in enumerate(parts):
        if not part.strip():
            continue
        
        # Check if this part starts with a Roman numeral
        match = re.match(pattern, part)
        if match:
            # This part starts with a Roman numeral
            if result:
                result.append('<br>')
            result.append('<span class="roman-item">')
            result.append(part)
            result.append('</span>')
        else:
            # Regular text
            result.append(part)
    
    return mark_safe(''.join(result))
