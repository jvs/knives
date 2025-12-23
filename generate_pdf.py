#!/usr/bin/env python3
"""Generate PDF from README.md using pure Python libraries."""

import markdown
from xhtml2pdf import pisa
from pathlib import Path
import io


def generate_pdf(input_file: str = "README.md", output_file: str = "README.pdf"):
    """Convert markdown file to PDF."""

    # Read the markdown file
    md_content = Path(input_file).read_text()

    # Convert markdown to HTML with extensions
    html_content = markdown.markdown(
        md_content,
        extensions=[
            'extra',          # Tables, footnotes, etc.
            'nl2br',          # Newline to <br>
        ]
    )

    # Wrap in a full HTML document with styling
    full_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Knives - Card Game Rules</title>
        <style>
            @page {{
                size: letter;
                margin: 0.75in;
            }}
            body {{
                font-family: Helvetica, Arial, sans-serif;
                font-size: 11pt;
                line-height: 1.6;
                color: #24292e;
            }}
            h1 {{
                font-size: 24pt;
                border-bottom: 2px solid #cccccc;
                padding-bottom: 0.3em;
                margin-top: 24pt;
                margin-bottom: 16pt;
            }}
            h2 {{
                font-size: 18pt;
                border-bottom: 1px solid #cccccc;
                padding-bottom: 0.3em;
                margin-top: 20pt;
                margin-bottom: 12pt;
            }}
            h3 {{
                font-size: 14pt;
                margin-top: 16pt;
                margin-bottom: 8pt;
            }}
            hr {{
                border: 0;
                border-top: 2px solid #cccccc;
                margin: 24pt 0;
            }}
            ul, ol {{
                padding-left: 2em;
            }}
            li {{
                margin: 0.25em 0;
            }}
            code {{
                background-color: #f0f0f0;
                padding: 0.2em 0.4em;
                font-family: Courier, monospace;
                font-size: 0.9em;
            }}
            strong {{
                font-weight: bold;
            }}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """

    # Convert HTML to PDF
    with open(output_file, "wb") as pdf_file:
        pisa_status = pisa.CreatePDF(
            io.StringIO(full_html),
            dest=pdf_file
        )

    if pisa_status.err:
        print(f"✗ Error generating PDF")
        return False
    else:
        print(f"✓ Generated {output_file}")
        return True


if __name__ == "__main__":
    generate_pdf()
