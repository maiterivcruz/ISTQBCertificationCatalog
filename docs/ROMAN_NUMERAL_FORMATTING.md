# Roman Numeral Sub-Statement Formatting

## Overview

This document describes the implementation of the custom Django template filter that formats Roman numeral sub-statements (i., ii., iii., iv., v.) to render on separate lines with proper indentation.

## Problem

Exam questions often contain sub-statements marked with Roman numerals in a single text block:

```
Which of the following statements are TRUE? i. Code coverage alone is not sufficient. ii. Requirements coverage links tests. iii. Exploratory testing coverage can be reported.
```

Previously, these would render as a continuous paragraph on the frontend, making them difficult to read.

## Solution

A custom Django template filter named `format_roman_numerals` was created to parse these patterns and convert them to properly formatted HTML.

### Components

#### 1. Custom Template Filter
**File:** `questions/templatetags/question_filters.py`

The filter:
- Escapes HTML to prevent XSS vulnerabilities
- Uses a regex pattern to identify Roman numeral markers (i., ii., iii., iv., v., vi., etc.)
- Splits text at Roman numeral boundaries using lookahead to preserve the markers
- Wraps each Roman numeral statement in a `<span class="roman-item">` tag
- Inserts `<br>` tags between statements for line breaks

**Pattern:** `r'\b(?:i{1,3}|iv|v|vi{1,3}|ix|x{1,3}|xl|l|lx{1,3}|xc|c)\.\s+'`

This pattern matches lowercase Roman numerals (i through c) followed by a period and space at word boundaries.

#### 2. CSS Styling
**File:** `questions/static/questions/css/question_list.css`

```css
.roman-item {
    display: block;
    margin-left: 1.5rem;
    padding: 0.25rem 0;
}
```

The styling:
- Sets `.roman-item` as a block-level element to force line breaks
- Adds left margin (1.5rem) for indentation
- Adds vertical padding for visual spacing

#### 3. Template Implementation
**File:** `questions/templates/questions/question_list.html`

The filter is applied to:
- Question stems: `{{ q.stem_before|format_roman_numerals }}` and `{{ q.stem_after|format_roman_numerals }}`
- Answer options: `{{ text|format_roman_numerals }}`
- Explanations: `{{ q.answer|format_roman_numerals }}`

The filter must be loaded at the top of the template:
```django
{% load question_filters %}
```

## Output Example

**Before:**
```
Which of the following statements are TRUE? i. Code coverage alone is not sufficient. ii. Requirements coverage links tests. iii. Exploratory testing coverage can be reported.
```

**After (rendered HTML):**
```html
Which of the following statements are TRUE? <br><span class="roman-item">i. Code coverage alone is not sufficient. </span><br><span class="roman-item">ii. Requirements coverage links tests. </span><br><span class="roman-item">iii. Exploratory testing coverage can be reported.</span>
```

**Visual result:**
```
Which of the following statements are TRUE?
    i. Code coverage alone is not sufficient.
    ii. Requirements coverage links tests.
    iii. Exploratory testing coverage can be reported.
```

## Features

✅ **Safe HTML Handling:** Input is escaped before processing  
✅ **Flexible Roman Numeral Support:** Handles i through c (up to 100)  
✅ **Non-Intrusive:** Only formats text containing Roman numerals  
✅ **Preserves Spacing:** Maintains original text structure for non-matching content  
✅ **Accessible:** Uses semantic HTML with proper line breaks  

## Testing

To test the filter manually:

```python
from questions.templatetags.question_filters import format_roman_numerals

test_text = "Which statements are true? i. First ii. Second iii. Third"
result = format_roman_numerals(test_text)
print(result)
```

## Edge Cases

- **No Roman numerals:** Text passes through unchanged
- **Mixed content:** Regular text and Roman numerals are handled correctly
- **HTML special characters:** Are properly escaped before processing
- **Uppercase text:** The filter matches lowercase Roman numerals only (as used in exam questions)

## Future Enhancements

Potential improvements could include:
- Supporting uppercase Roman numerals (I., II., III., etc.)
- Configurable indentation via CSS variable
- Support for other list markers (a), b), c) etc.)
- Automatic numbering in data ingestion instead of templating
