import json
from typing import List, Any
from pathlib import Path

from src.models.schema import ExtractedDocument
from src.utils.logger import get_logger

logger = get_logger(__name__)

class Exporter:
    def __init__(self, output_dir: str):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def export_json(self, data: List[ExtractedDocument], filename: str = "output.json"):
        filepath = self.output_dir / filename
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                # Convert pydantic models to dicts
                dicts = [doc.model_dump() for doc in data]
                json.dump(dicts, f, indent=2, ensure_ascii=False)
            logger.info(f"Successfully exported {len(data)} documents to JSON: {filepath}")
        except Exception as e:
            logger.error(f"Failed to export JSON: {e}")

    def export_ndjson(self, data: List[ExtractedDocument], filename: str = "output.ndjson"):
        filepath = self.output_dir / filename
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                for doc in data:
                    # Convert to JSON string and write with newline
                    json_str = doc.model_dump_json()
                    f.write(json_str + '\n')
            logger.info(f"Successfully exported {len(data)} documents to NDJSON: {filepath}")
        except Exception as e:
            logger.error(f"Failed to export NDJSON: {e}")
