# Setup the project using uv
setup:
    @echo "Setting up Python environment with uv..."
    uv venv
    uv pip install markdown xhtml2pdf
    @echo "✓ Python environment ready"
    @echo "✓ All dependencies installed via uv"

# Generate PDF from README.md
pdf:
    uv run --no-project python generate_pdf.py

# Clean generated files
clean:
    rm -f README.pdf

# Show available commands
help:
    @just --list
