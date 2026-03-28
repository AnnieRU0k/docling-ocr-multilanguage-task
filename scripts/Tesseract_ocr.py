from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import RapidOcrOptions, PdfPipelineOptions
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.backend.docling_parse_backend import DoclingParseDocumentBackend

def main():
    print("Step 1: Initializing RapidOCR (The Tesseract Alternative)...")
    # We use RapidOcrOptions here to bypass the tesserocr error
    ocr_options = RapidOcrOptions()

    pipeline_options = PdfPipelineOptions()
    pipeline_options.ocr_options = ocr_options

    print("Step 2: Building the Docling bridge...")
    pdf_options = PdfFormatOption(
        pipeline_options=pipeline_options,
        backend=DoclingParseDocumentBackend
    )

    print("Step 3: Converting Page 04.pdf...")
    converter = DocumentConverter(format_options={InputFormat.PDF: pdf_options})
    
    try:
        result = converter.convert("Page 04.pdf")

        print("Step 4: Saving final file...")
        output_filename = "Page04_rapidocr_markdown.md"
        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(result.document.export_to_markdown())
        
        print(f"Success! Created: {output_filename}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()