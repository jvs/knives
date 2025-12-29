#!/usr/bin/env python3
"""Generate styled HTML from rules.md for viewing and printing."""

import markdown
from pathlib import Path


def convert_to_smart_quotes(text: str) -> str:
    """Convert straight quotes to smart quotes.

    Double quotes:
    - Uses &ldquo; for opening quotes and &rdquo; for closing quotes
    - Assumes quotes are always paired and never nested

    Single quotes:
    - Converts all apostrophes to &rsquo; (for possessives and contractions)

    Skips quotes inside HTML tags.
    """
    result = []
    inside_tag = False

    for i, char in enumerate(text):
        # Track whether we're inside an HTML tag
        if char == '<':
            inside_tag = True
        elif char == '>':
            inside_tag = False
            result.append(char)
            continue

        # Only convert quotes when NOT inside HTML tags
        if not inside_tag:
            # Convert single quotes (apostrophes) to right single quote
            if char == "'":
                result.append('&rsquo;')
            # Convert double quotes based on context
            elif char == '"':
                if i == 0:
                    # Start of string - opening quote
                    result.append('&ldquo;')
                else:
                    prev_char = text[i - 1]
                    # Opening quote: after space, newline, left paren/bracket, or punctuation
                    if prev_char in ' \n\r\t([{:;,—-':
                        result.append('&ldquo;')
                    # Closing quote: after letter, digit, or ending punctuation
                    elif prev_char.isalnum() or prev_char in '.,!?\';:)]}':
                        result.append('&rdquo;')
                    else:
                        # Default to opening quote
                        result.append('&ldquo;')
            else:
                result.append(char)
        else:
            result.append(char)

    return ''.join(result)


def generate_html(input_file: str = "rules.md", output_file: str = "rules.html"):
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

    # Convert straight quotes to smart quotes (after HTML conversion to preserve HTML attributes)
    html_content = convert_to_smart_quotes(html_content)

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

        /* Print styles - compact for tiny rulebook feel */
        @media print {{
            @page {{
                margin: 0.75in;
            }}

            body {{
                padding: 0;
                background: white;
                font-size: 9pt;
                line-height: 1.4;
            }}

            h1 {{
                font-size: 16pt;
                margin: 0.75rem 0 0.5rem 0;
                color: #000;
                border-bottom-color: #333;
                padding-bottom: 0.25rem;
            }}

            h2 {{
                font-size: 12pt;
                margin: 0.75rem 0 0.4rem 0;
                color: #000;
                border-bottom-color: #666;
                padding-bottom: 0.2rem;
            }}

            h3 {{
                font-size: 10pt;
                margin: 0.5rem 0 0.3rem 0;
                color: #000;
            }}

            p {{
                margin: 0.3rem 0;
            }}

            ul, ol {{
                margin: 0.3rem 0 0.3rem 1.5em;
            }}

            li {{
                margin: 0.15rem 0;
            }}

            hr {{
                margin: 0.75rem 0;
                border-top-color: #999;
            }}

            strong {{
                color: #000;
            }}

            code {{
                background-color: #f0f0f0;
                color: #000;
                font-size: 0.85em;
            }}

            /* Ensure links are readable when printed */
            a {{
                color: #000;
                text-decoration: none;
            }}

            /* Hide the print button when printing */
            .print-button {{
                display: none;
            }}

            /* Quick reference formatting */
            h2#one-page-quick-reference {{
                page-break-before: always;
            }}

            /* License as small footnote on quick reference page */
            h2#license {{
                font-size: 7pt;
                margin-top: 1rem;
                margin-bottom: 0.2rem;
                border: none;
            }}

            h2#license + p {{
                font-size: 7pt;
                margin: 0;
                font-style: italic;
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
