import fitz  # PyMuPDF

# Create document
doc = fitz.open()

# Page size
width, height = fitz.paper_size("a4")

# Margins
margin = 50
fontsize = 12

# Read text
with open("content.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Helper variables for manual layout
x = margin
y = margin
line_height = fontsize * 1.2

# Initial page
page = doc.new_page(width=width, height=height)

# Function to handle text wrapping and pagination
lines = text.splitlines()

for line in lines:
    words = line.split(" ")
    current_line = ""
    
    for word in words:
        # Check width of logical line + next word
        test_line = current_line + word + " "
        if fitz.get_text_length(test_line, fontsize=fontsize) < width - 2 * margin:
            current_line = test_line
        else:
            # Draw current line
            page.insert_text((x, y), current_line, fontsize=fontsize)
            y += line_height
            current_line = word + " "
            
            # Check if we need a new page
            if y > height - margin:
                page = doc.new_page(width=width, height=height)
                y = margin

    # Draw the remaining part of the line (or the whole line if it was short)
    if current_line:
        page.insert_text((x, y), current_line, fontsize=fontsize)
        y += line_height # Move to next line for the next paragraph/line from file
        
        # Check if we need a new page
        if y > height - margin:
            page = doc.new_page(width=width, height=height)
            y = margin

# Save PDF
doc.save("simple_document.pdf")
doc.close()
