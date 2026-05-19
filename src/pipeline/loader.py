import os
from pathlib import Path
from typing import List, Generator
import re
from docx import Document

from src.utils.logger import get_logger

logger = get_logger(__name__)

class FileLoader:
    def __init__(self, input_path: str):
        self.input_path = Path(input_path)

    def _load_docx(self, path: Path) -> str:
        """Reads a .docx file and returns its content as a string with markdown-like headings."""
        try:
            doc = Document(path)
            full_text = []
            for para in doc.paragraphs:
                text = para.text.strip()
                if not text:
                    continue
                # If it looks like a Case start, turn it into a heading
                if re.match(r'^Case\s+\d+:', text, re.IGNORECASE):
                    text = f"## {text}"
                full_text.append(text)
            return '\n'.join(full_text)
        except Exception as e:
            logger.error(f"Error reading docx {path}: {e}")
            return ""

    def load_files(self) -> Generator[str, None, None]:
        """Generator that yields the content of .md, .txt, and .docx files."""
        if not self.input_path.exists():
            logger.warning(f"Input path does not exist: {self.input_path}")
            return
            
        valid_extensions = {".md", ".txt", ".docx"}
        
        if self.input_path.is_file():
            if self.input_path.suffix.lower() in valid_extensions:
                if self.input_path.suffix.lower() == ".docx":
                    yield self._load_docx(self.input_path)
                else:
                    try:
                        with open(self.input_path, 'r', encoding='utf-8') as f:
                            yield f.read()
                        logger.info(f"Loaded file: {self.input_path}")
                    except Exception as e:
                        logger.error(f"Error reading {self.input_path}: {e}")
            else:
                logger.warning(f"File {self.input_path} does not have a valid extension {valid_extensions}")
        else:
            for root, _, files in os.walk(self.input_path):
                for file in files:
                    file_path = Path(root) / file
                    if file_path.suffix.lower() in valid_extensions:
                        if file_path.suffix.lower() == ".docx":
                            content = self._load_docx(file_path)
                            if content:
                                yield content
                                logger.info(f"Loaded docx file: {file_path}")
                        else:
                            try:
                                with open(file_path, 'r', encoding='utf-8') as f:
                                    yield f.read()
                                logger.info(f"Loaded file: {file_path}")
                            except UnicodeDecodeError:
                                logger.error(f"Failed to read {file_path}. Please ensure it is UTF-8 encoded.")
                            except Exception as e:
                                logger.error(f"Error reading {file_path}: {e}")
