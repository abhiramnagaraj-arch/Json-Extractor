#!/bin/bash
export PYTHONPATH=$PYTHONPATH:.
# Find all .md and .docx files in data/input
FILES=$(find data/input -maxdepth 1 -name "*.md" -o -name "*.docx")

for file_path in $FILES; do
    file=$(basename "$file_path")
    # Skip sample.md if you want, or include it
    if [ "$file" == "sample.md" ]; then continue; fi
    
    # Remove extension for output name
    output_name="${file%.*}_output"
    echo "Processing $file -> $output_name.json"
    ./venv/bin/python3 src/main.py --input "$file_path" --output-name "$output_name" --format json
done
