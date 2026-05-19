import argparse
import sys
from pathlib import Path

from src.pipeline.loader import FileLoader
from src.pipeline.parser import Parser
from src.pipeline.transformer import Transformer
from src.pipeline.exporter import Exporter
from src.models.schema import ExtractedDocument
from src.utils.logger import get_logger

logger = get_logger("DocumentExtractor")

def main():
    parser = argparse.ArgumentParser(description="Rule-based Document Extraction Pipeline")
    parser.add_argument("--input", default="data/input", help="File or directory containing input markdown/txt files")
    parser.add_argument("--output", default="data/output", help="Directory to save output files")
    parser.add_argument("--output-name", default="output", help="Base name for the output file(s)")
    parser.add_argument("--format", choices=["json", "ndjson", "both"], default="ndjson", help="Output format")
    args = parser.parse_args()

    loader = FileLoader(args.input)
    exporter = Exporter(args.output)

    all_docs = []

    # Process files
    for file_content in loader.load_files():
        sections = Parser.split_sections(file_content)

        file_docs_count = 0
        for section in sections:
            try:
                # 1. Extract raw metadata
                raw_data = Parser.extract_metadata(section)

                # Basic validation: ensure it looks like a document section
                if not raw_data.get("title") and not raw_data.get("section_id"):
                    continue

                # 2. Transform and clean
                transformed_data = Transformer.transform(raw_data)

                # 3. Validate with Pydantic
                doc = ExtractedDocument(**transformed_data)
                all_docs.append(doc)
                file_docs_count += 1
            except Exception as e:
                logger.error(f"Error processing section '{raw_data.get('title', 'Unknown')}': {e}")

        logger.info(f"Extracted {file_docs_count} documents from current file.")

    if not all_docs:
        logger.warning("No valid documents extracted. Please check your input files.")
        sys.exit(0)

    logger.info(f"Successfully processed {len(all_docs)} total documents.")

    # 4. Export
    if args.format in ["json", "both"]:
        exporter.export_json(all_docs, f"{args.output_name}.json")
    if args.format in ["ndjson", "both"]:
        exporter.export_ndjson(all_docs, f"{args.output_name}.ndjson")

    logger.info(f"Pipeline execution completed. Results saved in {args.output}")


if __name__ == "__main__":
    main()
