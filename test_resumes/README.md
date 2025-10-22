# Smart Resume Parser

A Python-based application that extracts structured information from resumes in PDF and DOCX formats.

## Features
- Extract contact information (email, phone)
- Identify skills and technologies
- Parse education history
- Detect work experience
- Export to CSV/JSON formats
- Web interface using Streamlit

## Installation
1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Download spaCy model: `python -m spacy download en_core_web_sm`
4. Run the app: `streamlit run app.py`

## Usage
1. Launch the application
2. Upload PDF or DOCX resume files
3. View extracted information
4. Download results in CSV or JSON format