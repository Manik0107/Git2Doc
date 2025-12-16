import fitz  # PyMuPDF
import re

def generate_pdf(input_file="content.txt", output_file="simple_document.pdf"):
    """
    Generate a formatted PDF from a text file with markdown-style formatting.
    
    Args:
        input_file: Path to the input text file
        output_file: Path to the output PDF file
    """
    # Create document
    doc = fitz.open()

    # Page size
    width, height = fitz.paper_size("a4")

    # Margins and indentation
    margin = 50
    base_indent = margin
    list_indent = 20  # Additional indent for list items
    nested_indent = 15  # Additional indent for nested content
    
    # Font sizes
    main_heading_fontsize = 19.5  # # heading
    sub_heading_fontsize = 12     # ## heading
    body_fontsize = 10.5

    # Read text
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()

    # Helper variables for manual layout
    x = base_indent
    y = margin

    # Initial page
    page = doc.new_page(width=width, height=height)
    
    # Counter for numbered lists
    list_counter = {}  # Track counters for different list levels

    # Function to get heading level
    def get_heading_level(line):
        """Returns the heading level (1 for #, 2 for ##, etc.) or 0 if not a heading"""
        match = re.match(r'^(#+)\s', line.strip())
        return len(match.group(1)) if match else 0

    # Function to clean heading (remove # symbols)
    def clean_heading(line):
        return re.sub(r'^#+\s*', '', line.strip())

    # Function to check if line is a bullet/list item
    def is_list_item(line):
        """Check if line starts with *, -, or numbered list"""
        stripped = line.strip()
        return stripped.startswith('*') or stripped.startswith('-') or re.match(r'^\d+\.', stripped)
    
    # Function to check if line already has a number
    def has_existing_number(line):
        """Check if line already starts with a number"""
        stripped = line.strip()
        return bool(re.match(r'^\d+\.', stripped))
    
    # Function to get indentation level
    def get_indent_level(line):
        """Count leading spaces/tabs to determine indentation level"""
        return len(line) - len(line.lstrip())

    # Function to parse bold text (**text** or __text__)
    def parse_bold_segments(text):
        """Returns list of (text, is_bold) tuples"""
        segments = []
        # Split by ** or __ markers
        parts = re.split(r'(\*\*.*?\*\*|__.*?__)', text)
        
        for part in parts:
            if part.startswith('**') and part.endswith('**'):
                segments.append((part[2:-2], True))
            elif part.startswith('__') and part.endswith('__'):
                segments.append((part[2:-2], True))
            elif part:
                segments.append((part, False))
        
        return segments

    # Function to insert text with proper formatting
    def insert_formatted_line(page, doc, x_pos, y, line, heading_level=0, indent_level=0, list_number=None, preserve_number=False):
        """Insert a formatted line and return updated page, doc, and y position"""
        
        # Determine font size based on heading level
        if heading_level == 1:
            # Main heading (#)
            fontsize = main_heading_fontsize
            line_height = fontsize * 1.5
            fontname = "hebo"
            text_content = clean_heading(line)
        elif heading_level == 2:
            # Subheading (##)
            fontsize = sub_heading_fontsize
            line_height = fontsize * 1.4
            fontname = "hebo"
            text_content = clean_heading(line)
        elif heading_level >= 3:
            # Smaller headings (###, ####, etc.)
            fontsize = body_fontsize + 1  # Slightly larger than body
            line_height = fontsize * 1.4
            fontname = "hebo"  # Still bold
            text_content = clean_heading(line)
        else:
            # Body text
            fontsize = body_fontsize
            line_height = fontsize * 1.4
            fontname = "helv"
            text_content = line.strip()
            
            # Handle list items
            if preserve_number:
                # Keep existing number from markdown
                text_content = text_content
            elif list_number is not None:
                # Add new number for bullet points
                text_content = f"{list_number}. {text_content.lstrip('*-').strip()}"
        
        # Calculate x position with indentation
        current_x = x_pos + (indent_level * nested_indent)
        if list_number is not None:
            current_x += list_indent
        
        max_width = width - margin - (current_x - base_indent)
        
        # For headings, insert as single line
        if heading_level > 0:
            page.insert_text((current_x, y), text_content, fontsize=fontsize, fontname=fontname)
            return page, doc, y + line_height
        
        # For body text, parse bold segments and wrap
        segments = parse_bold_segments(text_content)
        
        for text, is_bold in segments:
            words = text.split(" ")
            
            for word in words:
                word_with_space = word if current_x == x_pos + (indent_level * nested_indent) + (list_indent if list_number else 0) else " " + word
                
                fontname = "hebo" if is_bold else "helv"
                word_width = fitz.get_text_length(word_with_space, fontsize=fontsize, fontname=fontname)
                
                if current_x + word_width > x_pos + max_width and current_x > x_pos + (indent_level * nested_indent):
                    # Move to next line
                    y += line_height
                    current_x = x_pos + (indent_level * nested_indent) + (list_indent if list_number else 0)
                    word_with_space = word
                    
                    # Check if we need a new page
                    if y > height - margin:
                        page = doc.new_page(width=width, height=height)
                        y = margin
                        current_x = x_pos + (indent_level * nested_indent) + (list_indent if list_number else 0)
                
                # Insert word
                page.insert_text((current_x, y), word_with_space, fontsize=fontsize, fontname=fontname)
                current_x += fitz.get_text_length(word_with_space, fontsize=fontsize, fontname=fontname)
        
        return page, doc, y + line_height

    # Process lines
    lines = text.splitlines()
    current_list_level = 0

    for line in lines:
        # Skip empty lines but add spacing
        if not line.strip():
            y += body_fontsize * 0.8
            current_list_level = 0  # Reset list counter on empty line
            list_counter = {}
            continue
        
        # Check if we need a new page before processing
        if y > height - margin - 30:  # Leave some buffer
            page = doc.new_page(width=width, height=height)
            y = margin
        
        # Determine line type and formatting
        heading_level = get_heading_level(line)
        indent_level = get_indent_level(line) // 4  # Assume 4 spaces per indent level
        
        if heading_level > 0:
            # Add extra spacing before headings
            if heading_level == 1:
                y += main_heading_fontsize * 0.5
            else:
                y += sub_heading_fontsize * 0.3
            
            page, doc, y = insert_formatted_line(page, doc, x, y, line, heading_level=heading_level)
            
            # Add spacing after headings
            y += body_fontsize * 0.5
            list_counter = {}  # Reset list counter after heading
            
        elif is_list_item(line):
            # Check if line already has a number
            if has_existing_number(line):
                # Preserve existing number from markdown
                page, doc, y = insert_formatted_line(page, doc, x, y, line, 
                                                    heading_level=0, 
                                                    indent_level=indent_level,
                                                    list_number=None,
                                                    preserve_number=True)
            else:
                # Add new number for bullet points (*, -)
                if indent_level not in list_counter:
                    list_counter[indent_level] = 1
                else:
                    list_counter[indent_level] += 1
                
                page, doc, y = insert_formatted_line(page, doc, x, y, line, 
                                                    heading_level=0, 
                                                    indent_level=indent_level,
                                                    list_number=list_counter[indent_level],
                                                    preserve_number=False)
        else:
            # Regular body text
            page, doc, y = insert_formatted_line(page, doc, x, y, line, 
                                                heading_level=0, 
                                                indent_level=indent_level)

    # Save PDF
    doc.save(output_file)
    doc.close()
    print(f"✅ PDF generated successfully: {output_file}")

# Allow running as standalone script
if __name__ == "__main__":
    generate_pdf()
