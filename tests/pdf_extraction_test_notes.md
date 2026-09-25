# PDF Extraction Test Results

The PDF extractor was tested successfully on four different PDF files.

| Test PDF | Result |
|---|---|
| `01_simple_resume.pdf` | Pass |
| `02_two_page_resume.pdf` | Pass |
| `03_two_column_resume.pdf` | Pass |
| `04_minimal_text.pdf` | Pass |

All tested PDFs were successfully processed, and the extracted text was readable and suitable for further processing by the AI layer.



# PDF Extractor Test Report

## Summary

The PDF extractor was tested against five resumes with different
document structures and formatting characteristics.

### Results

| PDF | Result | Observation |
|---|---|---|
| 01_simple_resume.pdf | PASS | Clean and structured text |
| 02_two_page_resume.pdf | PASS | Both pages extracted in correct order; one sentence contains a line break |
| 03_two_column_resume.pdf | PASS | Text is linearized; semantic content remains usable |
| 04_minimal_text.pdf | PASS | Text extracted correctly, but source contains very little information |
| La-Salle-Resume-Erika-Explorer-F22.pdf | PASS | Extra blank lines were successfully reduced |

## Conclusion

The extractor successfully extracts usable text from resumes with
different structures.

The cleaning stage successfully reduces excessive spaces and blank
lines.

The extracted text is generally suitable as input for an AI system.
However, multi-column PDFs are converted from visual layout into
linear text, and some sentences may contain line breaks caused by
the original PDF layout.