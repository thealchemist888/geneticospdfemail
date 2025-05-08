from weasyprint import HTML
import os

def test_html_to_pdf():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 40px;
            }
            h1 {
                color: #2c3e50;
                border-bottom: 2px solid #3498db;
                padding-bottom: 10px;
            }
            .card {
                border: 1px solid #ddd;
                border-radius: 8px;
                padding: 20px;
                margin: 20px 0;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            .highlight {
                background-color: #f8f9fa;
                padding: 10px;
                border-radius: 4px;
                font-family: monospace;
            }
            table {
                width: 100%;
                border-collapse: collapse;
                margin: 20px 0;
            }
            th, td {
                border: 1px solid #ddd;
                padding: 8px;
                text-align: left;
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <h1>HTML to PDF Test</h1>
        
        <div class="card">
            <h2>Styling Example</h2>
            <p>This is a styled paragraph with <strong>bold</strong> and <em>italic</em> text.</p>
            <div class="highlight">
                This is a highlighted code block
            </div>
        </div>

        <div class="card">
            <h2>Table Example</h2>
            <table>
                <tr>
                    <th>Name</th>
                    <th>Age</th>
                    <th>Role</th>
                </tr>
                <tr>
                    <td>John Doe</td>
                    <td>30</td>
                    <td>Developer</td>
                </tr>
                <tr>
                    <td>Jane Smith</td>
                    <td>25</td>
                    <td>Designer</td>
                </tr>
            </table>
        </div>

        <div class="card">
            <h2>Images and Links</h2>
            <p>Here's a link to <a href="https://example.com">Example.com</a></p>
            <p>Note: Images and links in PDFs are static and won't be clickable.</p>
        </div>
    </body>
    </html>
    """

    output_path = "test_html.pdf"
    
    try:
        # Convert HTML to PDF
        HTML(string=html_content).write_pdf(output_path)
        print(f"PDF generated successfully at: {output_path}")
    except Exception as e:
        print(f"Error generating PDF: {str(e)}")

if __name__ == "__main__":
    test_html_to_pdf() 