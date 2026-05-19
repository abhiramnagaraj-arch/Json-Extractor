import re
from typing import List, Dict

class Parser:
    @staticmethod
    def split_sections(content: str) -> List[str]:
        """Splits a document into sections by Markdown headings."""
        # Prepend newline to ensure the first heading matches if it's at start of file
        content = '\n' + content.strip()
        # Split by newline followed by ##
        sections = re.split(r'\n(?=## )', content)
        # Clean and filter empty sections
        return [s.strip() for s in sections if s.strip()]

    @staticmethod
    def extract_metadata(section: str) -> Dict[str, str]:
        """Extracts fields from a single markdown section using regex."""
        data = {
            "title": "",
            "section_id": "",
            "category": "",
            "subcategory": "",
            "alternate_questions": "",
            "answer": "",
            "keywords": ""
        }
        
        # Single line extractions
        patterns = {
            "title": r"^##\s+(.*)",
            "section_id": r"ID:\s*(.*)",
            "category": r"Category:\s*(.*)",
            "subcategory": r"Subcategory:\s*(.*)",
            "keywords": r"Keywords:\s*(.*)",
        }
        
        for key, pattern in patterns.items():
            match = re.search(pattern, section, flags=re.MULTILINE)
            if match:
                data[key] = match.group(1).strip()
                
        # Multi-line extractions (using lookahead for next heading, next known key, or end of string)
        # Known keys: ID, Category, Subcategory, Sub Category, Source section, Alternate questions, Answer, Case Description, Keywords
        keys = ["ID", "Category", "Subcategory", "Sub Category", "Source section", "Alternate questions", "Answer", "Case Description", "Keywords"]
        keys_pattern = "|".join(keys)
        key_lookahead = f"(?=\\n(?:{keys_pattern}):|\\n## |\\Z)"
        
        alt_q_match = re.search(r"Alternate questions:\s*(.*?)" + key_lookahead, section, flags=re.DOTALL | re.MULTILINE)
        if alt_q_match:
            data["alternate_questions"] = alt_q_match.group(1).strip()
            
        ans_match = re.search(r"(?:Answer|Case Description):\s*(.*?)" + key_lookahead, section, flags=re.DOTALL | re.MULTILINE)
        if ans_match:
            data["answer"] = ans_match.group(1).strip()
            
        return data
