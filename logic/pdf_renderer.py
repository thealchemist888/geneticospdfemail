import markdown
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration
import os

def render_markdown_to_pdf(markdown_content: str, output_path: str) -> None:
    # Convert markdown to HTML with extensions for better formatting
    html_content = markdown.markdown(
        markdown_content,
        extensions=[
            'markdown.extensions.tables',  # For tables
            'markdown.extensions.fenced_code',  # For code blocks
            'markdown.extensions.codehilite',  # For syntax highlighting
            'markdown.extensions.extra'  # For various other features
        ]
    )
    
    # Add enhanced styling
    styled_html = f"""
    <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    line-height: 1.6;
                    margin: 2cm;
                    color: #333;
                    max-width: 800px;
                    margin: 2cm auto;
                }}
                h1, h2, h3, h4, h5, h6 {{
                    color: #2c3e50;
                    margin-top: 1.5em;
                    margin-bottom: 0.5em;
                }}
                h1 {{ font-size: 2em; }}
                h2 {{ font-size: 1.75em; }}
                h3 {{ font-size: 1.5em; }}
                
                p {{
                    margin-bottom: 1em;
                }}
                
                code {{
                    background-color: #f8f9fa;
                    padding: 2px 4px;
                    border-radius: 3px;
                    font-family: 'Courier New', monospace;
                    font-size: 0.9em;
                }}
                
                pre {{
                    background-color: #f8f9fa;
                    padding: 1em;
                    border-radius: 5px;
                    overflow-x: auto;
                    margin: 1em 0;
                }}
                
                pre code {{
                    background-color: transparent;
                    padding: 0;
                }}
                
                blockquote {{
                    border-left: 4px solid #2c3e50;
                    margin: 1em 0;
                    padding: 0.5em 1em;
                    background-color: #f8f9fa;
                }}
                
                table {{
                    border-collapse: collapse;
                    width: 100%;
                    margin: 1em 0;
                }}
                
                th, td {{
                    border: 1px solid #ddd;
                    padding: 8px;
                    text-align: left;
                }}
                
                th {{
                    background-color: #f8f9fa;
                }}
                
                img {{
                    max-width: 100%;
                    height: auto;
                }}
                
                ul, ol {{
                    margin: 1em 0;
                    padding-left: 2em;
                }}
                
                li {{
                    margin: 0.5em 0;
                }}
                
                hr {{
                    border: none;
                    border-top: 2px solid #eee;
                    margin: 2em 0;
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