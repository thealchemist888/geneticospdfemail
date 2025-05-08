from logic.pdf_renderer import render_markdown_to_pdf
from logic.mailer import send_report_email
import os

def test_pdf_generation_and_email():
    markdown_content = """# Welcome to Markdown Showcase 🚀

## 1. Headers

Markdown supports six levels of headers:

# H1 Header
## H2 Header
### H3 Header
#### H4 Header
##### H5 Header
###### H6 Header

---

## 2. Emphasis

You can use **bold**, *italic*, or ***bold italic***.  
Also: __bold__, _italic_, and ___bold italic___ work too.

> "Markdown is not a replacement for HTML, or even close to it..."  
> — John Gruber

---

## 3. Lists

**Unordered list**:
- Apple 🍎
- Banana 🍌
  - Ripe
  - Overripe
- Cherry 🍒

**Ordered list**:
1. Wake up
2. Drink water
3. Code something
   1. Write logic
   2. Fix bugs

---

## 4. Code Blocks

Inline code: `const answer = 42;`

Multiline code:
```python
def greet(name):
    return f"Hello, {name}!"

print(greet("World"))
```"""

    output_path = "test_markdown.pdf"
    
    # Generate the PDF
    render_markdown_to_pdf(markdown_content, output_path)
    print(f"PDF generated successfully at: {output_path}")
    
    # Send the PDF via email
    try:
        send_report_email("normangrande@gmail.com", output_path)
        print("Email sent successfully")
    except Exception as e:
        print(f"Error sending email: {str(e)}")
    finally:
        # Clean up the PDF file
        if os.path.exists(output_path):
            os.unlink(output_path)

if __name__ == "__main__":
    test_pdf_generation_and_email() 