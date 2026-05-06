# Legal-Document-Analyzer

A Python-based legal document analysis tool that extracts text from PDF documents, generates concise summaries, identifies important legal clauses, and provides document statistics. The project is designed to simplify the understanding of lengthy legal documents using Natural Language Processing (NLP) techniques.

Features: 
- Extracts text from PDF legal documents
- Splits large documents into manageable sections
- Generates extractive summaries for each section
- Detects important legal clauses such as:
  - Termination
  - Payment Terms
  - Confidentiality
  - Liability
  - Governing Law
  - Intellectual Property
  - Non-Compete
  - Renewal
- Displays document analytics and compression statistics
- Command-line based workflow


Technologies Used
- Python
- PyMuPDF (fitz)
- Regular Expressions (re)
- NLP-based extractive summarization
  
How It Works
1. The user provides the path to a legal PDF document.
2. The system extracts the text from the PDF.
3. The extracted content is divided into smaller chunks for efficient processing.
4. Each chunk is summarized using extractive summarization techniques.
5. Key legal clauses are identified based on predefined keywords.
6. Document statistics and compression ratios are displayed.


