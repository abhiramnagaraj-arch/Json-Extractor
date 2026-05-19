import re
from typing import List, Dict, Any

from src.pipeline.cleaner import Cleaner

STOPWORDS = {
    "a", "an", "the", "and", "or", "but", "in", "on", "at", "to", "for", 
    "of", "with", "by", "as", "is", "are", "was", "were", "be", "this", 
    "that", "it", "how", "what", "when", "where", "why", "can", "do", "does"
}

class Transformer:
    @staticmethod
    def transform_id(raw_id: str) -> str:
        """Removes backticks, preserves underscores, converts to lowercase."""
        cleaned = raw_id.replace('`', '')
        return cleaned.lower().strip()
        
    @staticmethod
    def transform_title(raw_title: str) -> str:
        """Removes markdown symbols from title."""
        return Cleaner.clean_markdown_artifacts(raw_title)

    @staticmethod
    def build_tags(category: str, subcategory: str, keywords: str, title: str) -> List[str]:
        """Builds deduplicated, lowercased tags filtering out stopwords, max 15."""
        raw_words = []
        if category:
            raw_words.append(category)
        if subcategory:
            raw_words.append(subcategory)
        if keywords:
            raw_words.extend([k.strip() for k in keywords.split(',')])
            
        # Add title words
        title_cleaned = re.sub(r'[^\w\s]', '', title)
        raw_words.extend(title_cleaned.split())
        
        tags = []
        seen = set()
        for word in raw_words:
            w = word.lower().strip()
            if w and w not in STOPWORDS and w not in seen:
                seen.add(w)
                tags.append(w)
                if len(tags) >= 15:
                    break
        return tags

    @staticmethod
    def generate_snippet(answer: str) -> str:
        """Generates a summary within 50 words while preserving some readability."""
        if not answer:
            return ""
        
        # Clean slightly just for the snippet to make it a concise summary
        cleaned = re.sub(r'\s+', ' ', answer).strip()
        words = cleaned.split()
        
        if len(words) <= 50:
            return cleaned
        
        return ' '.join(words[:50]) + "..."

    @classmethod
    def transform(cls, raw_data: Dict[str, Any]) -> Dict[str, Any]:
        """Transforms raw extracted metadata according to specific user requirements."""
        title = raw_data.get("title", "").strip()
        section_id = raw_data.get("section_id", "").strip()
        
        # Fallback: if section_id is missing, generate one from the title
        if not section_id and title:
            section_id = re.sub(r'[^\w\s]', '', title).lower().replace(' ', '_')
            
        return {
            "section_id": cls.transform_id(section_id),
            "title": title,
            "category_tags": [],
            "short_snippet": "",
            "description": raw_data.get("answer", "").strip(),
            "faqs": []
        }
