from xhtml2pdf import pisa

# Function to convert HTML file to PDF


def convert_html_file_to_pdf(input_html_file, output_pdf_file):
    # Read HTML content from file
    with open(input_html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Create a PDF file
    with open(output_pdf_file, 'wb') as output_pdf:
        # Convert HTML to PDF
        pisa_status = pisa.CreatePDF(html_content, dest=output_pdf)

    if pisa_status.err:
        print(f"Failed to generate PDF: {pisa_status.err}")
    else:
        print(f"PDF successfully generated: {output_pdf_file}")


# Input HTML file path and output PDF file path
# Replace with the path to your HTML file
input_html_path = 'D:/Projects/Html/doc/index.html'
output_pdf_path = 'output.pdf'  # Replace with the desired output PDF file path

# Convert HTML file to PDF
convert_html_file_to_pdf(input_html_path, output_pdf_path)
