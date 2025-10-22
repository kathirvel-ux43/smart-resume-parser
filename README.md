# Smart Resume Parser

A Python-based application that extracts structured information from resumes in PDF and DOCX formats using Natural Language Processing (NLP).

## 🚀 Features

- **Contact Information Extraction** - Email, phone numbers
- **Skills Detection** - Technical skills, programming languages, tools
- **Education History** - Degrees, fields of study, institutions
- **Work Experience** - Job roles, companies, experience details
- **Resume Scoring** - Automatic quality scoring (0-100 points)
- **Multiple Export Formats** - CSV and JSON export
- **User-Friendly Web Interface** - Built with Streamlit

## 🛠️ Installation

### Prerequisites
- Python 3.13
- pip package manager

### Steps
1. Clone the repository:
   ```
   git clone https://github.com/YOUR_USERNAME/smart-resume-parser.git
   cd smart-resume-parser
   ```
2. Install required packages:
```pip install -r requirements.txt```

3.Download spaCy language model:
```python -m spacy download en_core_web_sm```

4.Run the application:
```streamlit run app.py```

Project Structure
```
smart-resume-parser/
├── app.py                 # Main Streamlit application
├── text_extractor.py      # PDF/DOCX text extraction
├── resume_parser.py       # Core parsing and analysis logic
├── requirements.txt       # Project dependencies
└── README.md             # Project documentation
```
Usage

1.Launch the application using streamlit run app.py
2.Upload resume files in PDF or DOCX format
3.View extracted information including:
    * Contact details
    * Technical skills
    * Education history
    * Work experience
    * Resume quality score
4.Export results in CSV or JSON format

Technology Stack
    Backend: Python
    NLP: spaCy
    PDF Processing: PyMuPDF
    DOCX Processing: python-docx
    Web Framework: Streamlit
    Data Processing: pandas

Contributing
Contributions are welcome! Please feel free to submit pull requests or open issues for suggestions.

License
This project is open source and available under the MIT License.

Author
kathirvel S - GitHub Profile github.com/kathirvel-ux43
