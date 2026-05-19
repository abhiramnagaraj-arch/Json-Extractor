import re

class Cleaner:
    @staticmethod
    def normalize_whitespace(text: str) -> str:
        """Removes excessive whitespace and newlines."""
        if not text:
            return ""
        # Replace multiple spaces/newlines with a single space (while keeping single newlines where appropriate? Actually, we want to normalize it entirely for description)
        # But wait, "preserve steps" means we shouldn't destroy all newlines if they format a step.
        # Actually, let's just strip excessive spaces but keep single newlines.
        
        # Replace 3+ newlines with 2 newlines
        text = re.sub(r'\n{3,}', '\n\n', text)
        
        # Replace multiple spaces with a single space
        text = re.sub(r'[ \t]+', ' ', text)
        return text.strip()

    @staticmethod
    def clean_markdown_artifacts(text: str) -> str:
        """Removes common markdown symbols."""
        if not text:
            return ""
        
        # Remove markdown bold/italic
        text = re.sub(r'[*_]{1,3}([^*_]+)[*_]{1,3}', r'\1', text)
        # Remove inline code backticks
        text = re.sub(r'`([^`]+)`', r'\1', text)
        # Remove hash headings but keep text
        text = re.sub(r'^#+\s+', '', text, flags=re.MULTILINE)
        
        return text.strip()

    @staticmethod
    def clean_bullets(text: str) -> str:
        """Converts bullet points into sentences."""
        if not text:
            return ""
            
        lines = text.split('\n')
        cleaned_lines = []
        for line in lines:
            stripped = line.strip()
            # If it's a bullet
            if stripped.startswith('- ') or stripped.startswith('* ') or re.match(r'^\d+\.\s+', stripped):
                # Remove the bullet characters
                cleaned = re.sub(r'^([-*]\s+|\d+\.\s+)', '', stripped)
                # Ensure it ends with a period if it doesn't already
                if cleaned and not cleaned[-1] in '.!?':
                    cleaned += '.'
                cleaned_lines.append(cleaned)
            else:
                cleaned_lines.append(stripped)
                
        # Rejoin. Let's separate sentences with a space instead of a newline for bullets.
        # But the instructions said "preserve steps" in description and for snippet convert bullet to "Login. Navigate."
        return ' '.join(filter(bool, cleaned_lines))
        
    @classmethod
    def clean_answer(cls, answer: str) -> str:
        """Pipeline for cleaning the answer text."""
        text = cls.clean_markdown_artifacts(answer)
        text = cls.clean_bullets(text)
        # Convert all multiple spaces that might have been created to single space
        text = re.sub(r'\s+', ' ', text)
        return text.strip()
