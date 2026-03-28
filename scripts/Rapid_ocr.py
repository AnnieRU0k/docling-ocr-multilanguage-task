from docling.document_converter import DocumentConverter

# Defining the file 
source = "Page 04.pdf"

# Setting up the converter
converter = DocumentConverter()

# Permorming the conversion
result = converter.convert(source)

# Output the results to the terminal
print(result.document.export_to_markdown())