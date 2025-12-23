#!/usr/bin/env python3
"""Generate styled HTML from README.md for viewing and printing."""

import markdown
from pathlib import Path


def generate_html(input_file: str = "README.md", output_file: str = "rules.html"):
    """Convert markdown file to styled HTML."""

    # Read the markdown file
    md_content = Path(input_file).read_text()

    # Convert markdown to HTML with extensions
    html_content = markdown.markdown(
        md_content,
        extensions=[
            'extra',          # Tables, footnotes, etc.
            'nl2br',          # Newline to <br>
            'toc',            # Table of contents
        ]
    )

    # Full HTML document with beautiful print-optimized styling
    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Knives - A Five-Player Trick-Taking Game</title>
    <style>
        /* Print-specific styles */
        @page {{
            size: letter;
            margin: 0.75in;
        }}

        @page :first {{
            margin-top: 0.5in;
        }}

        /* Prevent page breaks inside important elements */
        h1, h2, h3 {{
            page-break-after: avoid;
        }}

        ul, ol {{
            page-break-inside: avoid;
        }}

        /* Base styles */
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
            font-size: 11pt;
            line-height: 1.6;
            color: #1a1a1a;
            max-width: 8.5in;
            margin: 0 auto;
            padding: 1rem;
            background: #ffffff;
        }}

        /* Typography */
        h1 {{
            font-size: 28pt;
            font-weight: 700;
            margin: 1.5rem 0 1rem 0;
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 0.5rem;
        }}

        h1:first-child {{
            margin-top: 0;
        }}

        h2 {{
            font-size: 18pt;
            font-weight: 600;
            margin: 1.5rem 0 0.75rem 0;
            color: #34495e;
            border-bottom: 2px solid #95a5a6;
            padding-bottom: 0.3rem;
        }}

        h3 {{
            font-size: 14pt;
            font-weight: 600;
            margin: 1.25rem 0 0.5rem 0;
            color: #2c3e50;
        }}

        p {{
            margin: 0.5rem 0;
        }}

        /* Horizontal rules */
        hr {{
            border: none;
            border-top: 2px solid #bdc3c7;
            margin: 1.5rem 0;
            page-break-after: avoid;
        }}

        /* Lists */
        ul, ol {{
            margin: 0.5rem 0 0.5rem 2em;
        }}

        li {{
            margin: 0.25rem 0;
        }}

        /* Strong text */
        strong {{
            font-weight: 600;
            color: #2c3e50;
        }}

        /* Code */
        code {{
            background-color: #f8f9fa;
            padding: 0.15em 0.4em;
            border-radius: 3px;
            font-family: 'Monaco', 'Menlo', 'Courier New', monospace;
            font-size: 0.9em;
            color: #e74c3c;
        }}

        /* Print styles */
        @media print {{
            body {{
                padding: 0;
                background: white;
            }}

            h1 {{
                color: #000;
                border-bottom-color: #333;
            }}

            h2 {{
                color: #000;
                border-bottom-color: #666;
            }}

            h3 {{
                color: #000;
            }}

            strong {{
                color: #000;
            }}

            code {{
                background-color: #f0f0f0;
                color: #000;
            }}

            hr {{
                border-top-color: #999;
            }}

            /* Ensure links are readable when printed */
            a {{
                color: #000;
                text-decoration: none;
            }}
        }}

        /* Screen-only styles */
        @media screen {{
            body {{
                background: #f5f6fa;
                box-shadow: 0 0 20px rgba(0,0,0,0.1);
                padding: 2rem;
                margin: 2rem auto;
            }}

            .print-button {{
                position: fixed;
                top: 20px;
                right: 20px;
                padding: 0.75rem 1.5rem;
                background: #3498db;
                color: white;
                border: none;
                border-radius: 5px;
                font-size: 14pt;
                font-weight: 600;
                cursor: pointer;
                box-shadow: 0 2px 10px rgba(52, 152, 219, 0.3);
                transition: all 0.3s ease;
            }}

            .print-button:hover {{
                background: #2980b9;
                box-shadow: 0 4px 15px rgba(52, 152, 219, 0.4);
                transform: translateY(-2px);
            }}

            .print-button:active {{
                transform: translateY(0);
            }}
        }}
    </style>
</head>
<body>
    <button class="print-button" onclick="window.print()">🖨️ Print Rules</button>
    {html_content}

    <script>
        // Add keyboard shortcut for printing
        document.addEventListener('keydown', function(e) {{
            if ((e.ctrlKey || e.metaKey) && e.key === 'p') {{
                e.preventDefault();
                window.print();
            }}
        }});
    </script>
</body>
</html>
"""

    # Write the HTML file
    Path(output_file).write_text(full_html, encoding='utf-8')
    print(f"✓ Generated {output_file}")
    print(f"  Open in browser to view or print")


if __name__ == "__main__":
    generate_html()
