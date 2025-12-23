# Setup the project using uv
setup:
    @echo "Setting up Python environment with uv..."
    uv venv
    uv pip install markdown
    @echo "✓ Python environment ready"
    @echo "✓ All dependencies installed via uv"

# Generate HTML from README.md
html:
    uv run --no-project python generate_html.py

# Open generated HTML in browser
view: html
    open rules.html

# Clean generated files
clean:
    rm -f rules.html

# Show available commands
help:
    @just --list
