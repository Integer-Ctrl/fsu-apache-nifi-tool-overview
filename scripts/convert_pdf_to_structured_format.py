
from click import Path
from docling.document_converter import DocumentConverter
from docling.datamodel.document import ConversionResult
from docling.datamodel.base_models import ConversionStatus
from docling_core.types.doc import ImageRefMode

# Change this to a local path or another URL if desired.
# Note: using the default URL requires network access; if offline, provide a
# local file path (e.g., Path("/path/to/file.pdf")).
source = "./example-pdfs/auer24-docling-technical-report.pdf"
doc_filename = source.split("/")[-1].replace(".pdf", "")
output_dir = Path("./output")

converter = DocumentConverter()
result: ConversionResult = converter.convert(source)

if result.status == ConversionStatus.SUCCESS:
    # JSON
    result.document.save_as_json(
        output_dir / f"{doc_filename}.json",
        image_mode=ImageRefMode.PLACEHOLDER,
    )

    # HTML
    result.document.save_as_html(
        output_dir / f"{doc_filename}.html",
        image_mode=ImageRefMode.EMBEDDED,
    )

    # Markdown
    result.document.save_as_markdown(
        output_dir / f"{doc_filename}.md",
        image_mode=ImageRefMode.PLACEHOLDER,
    )

# # Print Markdown to stdout.
# print(result.document.export_to_markdown())
