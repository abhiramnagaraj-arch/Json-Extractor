The JSON Extractor project is a modular Python-based pipeline designed to transform unstructured or semi-structured
  documents (Markdown, TXT, and Word .docx) into structured, validated JSON or NDJSON data.

  Here is the detailed flow and working of the code:

  1. Orchestration & Entry Point
   * process_all.sh: This shell script acts as a batch processor. It scans the data/input/ directory for supported files,
     removes their extensions, and runs the main Python application for each file, naming the output accordingly.
   * src/main.py: The primary entry point. It handles command-line arguments (input/output paths, formats) and coordinates
     the lifecycle of a single file through the pipeline stages: Load → Parse → Transform → Validate → Export.

  2. Loading Phase (src/pipeline/loader.py)
   * The FileLoader class is responsible for reading source files.
   * DOCX Handling: It uses the python-docx library to read Word documents. Crucially, it converts specific patterns (like
     "Case 123:") into Markdown headings (## Case 123:) so that the rest of the pipeline can treat them as consistent
     sections.
   * It yields the raw string content of the files to the next stage.

  3. Parsing Phase (src/pipeline/parser.py)
   * split_sections: Uses regular expressions to split the document into logical chunks based on ## Markdown headings. Each
     chunk typically represents one FAQ or support case.
   * extract_metadata: For each section, it applies several regex patterns to pull out specific fields such as:
       * ID: Unique identifier for the entry.
       * Title: The text following the ## heading.
       * Category/Subcategory: Organizational metadata.
       * Answer/Case Description: The main body of the section (supports multi-line extraction).
       * Keywords: Tagging information.

  4. Transformation & Cleaning Phase
   * src/pipeline/transformer.py: Normalizes the raw data. It generates a section_id from the title if one is missing and
     prepares the final dictionary structure.
       * Note: It contains utility methods like build_tags and generate_snippet to further enrich data (e.g., filtering
         stopwords and summarizing text).
   * src/pipeline/cleaner.py: A helper class that provides "surgical" cleaning:
       * Removes Markdown symbols (bold, italic, backticks).
       * Normalizes whitespace.
       * Converts bullet points into full, readable sentences.

  5. Validation Phase (src/models/schema.py)
   * The pipeline uses Pydantic (ExtractedDocument model) to enforce data integrity. Before any data is exported, it is
     passed through this model to ensure all required fields are present and correctly typed. If a section is malformed, the
     pipeline logs an error and skips that specific entry rather than crashing.

  6. Exporting Phase (src/pipeline/exporter.py)
   * The Exporter class handles saving the processed data to the data/output/ directory.
   * It supports two formats:
       * JSON: A single standard array of objects.
       * NDJSON: Newline Delimited JSON, where each line is a separate JSON object (ideal for streaming or large datasets).

  Directory Summary
   * src/pipeline/: Contains the logic for each step of the processing.
   * src/models/: Defines the "contract" or schema the data must follow.
   * data/input/: Source files (.md, .docx, .txt).
   * data/output/: Resulting structured data files.