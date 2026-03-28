from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import EasyOcrOptions, PdfPipelineOptions
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.backend.docling_parse_backend import DoclingParseDocumentBackend

# 1. Setup the OCR Pipeline (Forced full-page for comparison)
pipeline_options = PdfPipelineOptions()
pipeline_options.ocr_options = EasyOcrOptions(force_full_page_ocr=True)

# 2. Build the 'Bridge' required for Version 2.82.0
pdf_options = PdfFormatOption(
    pipeline_options=pipeline_options,
    backend=DoclingParseDocumentBackend
)

# 3. Initialize and Run
converter = DocumentConverter(format_options={InputFormat.PDF: pdf_options})
result = converter.convert("Page 04.pdf")

# 4. Save to file
with open("Page04_easyocr_markdown.md", "w", encoding="utf-8") as f:
    f.write(result.document.export_to_markdown())