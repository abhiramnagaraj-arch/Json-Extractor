 This project is a modular data extraction pipeline that converts semi-structured Markdown text into strictly structured
  JSON data using Python and Pydantic.

  Here is a breakdown of how the components work together:

  1. The Flow of Data
  The script follows a "Linear Pipeline" pattern:
  Load File → Split into Sections → Extract Raw Metadata → Clean & Transform → Validate → Export.

  2. Component Breakdown

  A. The Loader (src/pipeline/loader.py)
   * Purpose: Reads the input files.
   * Logic: It checks if the path is a single file or a folder. It uses a Generator (yield) to read files one by one, which
     keeps memory usage low even if you have hundreds of documents.

  B. The Parser (src/pipeline/parser.py)
  This is the "Brain" of the extraction.
   * Splitting: It uses Regex to find the ## Markdown headers. Every time it sees ##, it knows a new question/answer block
     has started.
   * Metadata Extraction: It uses specific Regular Expression patterns to find keys like ID:, Category:, and Answer:.
       * Example Pattern: r"ID:\s*(.*)" looks for the literal text "ID:", skips any spaces, and captures everything after it.

  C. The Transformer & Cleaner (src/pipeline/transformer.py & cleaner.py)
  Raw text from Markdown is often "noisy" (contains stars *, backticks `  ``, or extra newlines).
   * Cleaning: The Cleaner removes Markdown symbols and normalizes whitespace. It also converts bullet points into full
     sentences for the short_snippet.
   * Transformation: The Transformer builds the category_tags. It takes the category, subcategory, keywords, and title,
     merges them, removes "stopwords" (like a, an, the, is), and ensures you have a clean list of tags for searching.

  D. The Schema (src/models/schema.py)
   * Purpose: Enforcement.
   * Logic: It uses Pydantic. Before any JSON is saved, Pydantic checks the data. If a section_id is missing or faqs isn't a
     list, the script will throw an error. This ensures your output is always "machine-readable" and never broken.

  E. The Exporter (src/pipeline/exporter.py)
   * Purpose: Saving the data.
   * Logic: It takes the validated Python objects and converts them into a standard JSON array or NDJSON (Newline Delimited
     JSON) format.

  3. The Orchestrator (src/main.py)
  This is the entry point that ties everything together. It handles the Command Line Arguments (like --input and --format)
  and loops through the files provided by the Loader, passing them through the Parser, Transformer, and Exporter in order.

  Summary of the "Rule-Based" Approach
  Unlike AI, which can be unpredictable, this script is Rule-Based. It relies on the consistent structure of your Markdown
  files (using ID:, Answer:, etc.). This makes it:
   1. Extremely Fast: Processes dozens of files in milliseconds.
   2. Deterministic: You get the exact same output every time you run it.
   3. Cheap: It runs locally on your machine without needing an API key.
