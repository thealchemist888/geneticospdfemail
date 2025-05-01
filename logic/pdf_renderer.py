import markdown
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration
import os

def render_markdown_to_pdf(markdown_content: str, output_path: str) -> None:
    # Convert markdown to HTML
    html_content = markdown.markdown(markdown_content)
    
    # Add basic styling
    styled_html = f"""
    <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    line-height: 1.6;
                    margin: 2cm;
                    color: #333;
                }}
                h1, h2, h3 {{
                    color: #2c3e50;
                }}
                code {{
                    background-color: #f8f9fa;
                    padding: 2px 4px;
                    border-radius: 3px;
                }}
                pre {{
                    background-color: #f8f9fa;
                    padding: 1em;
                    border-radius: 5px;
                    overflow-x: auto;
                }}
            </style>
        </head>
        <body>
            {html_content}
        </body>
    </html>
    """
    
    # Configure fonts
    font_config = FontConfiguration()
    
    # Generate PDF
    HTML(string=styled_html).write_pdf(
        output_path,
        font_config=font_config
    ) 