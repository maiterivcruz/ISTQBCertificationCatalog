# Quick Reference: Roman Numeral Formatting Filter

## Filter Name
`format_roman_numerals`

## Module
`questions.templatetags.question_filters`

## Usage in Templates

### Basic Usage
```django
{% load question_filters %}

{{ question_text|format_roman_numerals }}
```

### In a Loop
```django
{% load question_filters %}

{% for option in options %}
    <span class="option-text">{{ option|format_roman_numerals }}</span>
{% endfor %}
```

### Chained with Other Filters
```django
{{ text|truncatewords:20|format_roman_numerals }}
```

## What It Formats

The filter detects and formats Roman numeral sub-statements:
- Input: `"i. First ii. Second iii. Third"`
- Output: Three items on separate lines with indentation

## Supported Patterns

✓ Lowercase Roman numerals: i., ii., iii., iv., v., vi., vii., viii., ix., x., ... c.
✗ Uppercase Roman numerals (I., II., III., etc.) - not currently supported
✗ Arabic numerals (1., 2., 3., etc.) - not currently supported
✗ Letter lists (a), b), c), etc.) - not currently supported

## Current Implementation

**Locations where the filter is applied:**
1. Question stems (before and after tables)
2. Answer options
3. Explanations/answers

**File:** `questions/templates/questions/question_list.html`

## CSS Styling

The HTML output uses the class `roman-item` which is styled in:
`questions/static/questions/css/question_list.css`

```css
.roman-item {
    display: block;
    margin-left: 1.5rem;
    padding: 0.25rem 0;
}
```

## HTML Output Example

**Input:**
```
Which statements are true? i. First ii. Second
```

**Output:**
```html
Which statements are true? <br><span class="roman-item">i. First </span><br><span class="roman-item">ii. Second</span>
```

## Safety

✓ HTML is automatically escaped before formatting
✓ The filter uses `mark_safe()` only after processing user input
✓ No XSS vulnerabilities introduced

## Testing the Filter

### In Django Shell
```python
from questions.templatetags.question_filters import format_roman_numerals

test_text = "Which are true? i. First ii. Second"
result = format_roman_numerals(test_text)
print(result)
```

### Expected Output
```html
Which are true? <br><span class="roman-item">i. First </span><br><span class="roman-item">ii. Second</span>
```

## Troubleshooting

### Filter Not Working
1. Ensure `{% load question_filters %}` is at the top of template
2. Check that `questions/templatetags/question_filters.py` exists
3. Ensure `questions/templatetags/__init__.py` exists
4. Restart Django development server

### Text Not Showing Line Breaks
1. Verify CSS rule `.roman-item { display: block; }` is in stylesheet
2. Check browser DevTools to see if the HTML contains `<br>` and `<span>` tags
3. Ensure CSS file is loaded (check browser Network tab)

### Different Roman Numerals Not Formatting
Current pattern supports: i, ii, iii, iv, v, vi, vii, viii, ix, x through c

To add support for:
- **Uppercase (I., II., III., etc.):** Add pattern in filter
- **Arabic numerals (1., 2., 3., etc.):** Add alternative pattern
- **Letters (a), b), c), etc.):** Add alternative pattern

## Performance Considerations

- Filter runs at template render time
- No database queries
- Minimal performance impact
- Consider caching if rendering millions of questions

## Future Expansion

To support additional patterns, modify the regex pattern in:
`questions/templatetags/question_filters.py`

Current pattern:
```python
pattern = r'\b(?:i{1,3}|iv|v|vi{1,3}|ix|x{1,3}|xl|l|lx{1,3}|xc|c)\.\s+'
```

Example: To add uppercase support, modify to:
```python
pattern = r'\b(?:[Ii]{1,3}|[Ii][Vv]|[Vv]|[Vv][Ii]{1,3}|...)\.\s+'
```
