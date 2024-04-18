# Data Extraction and NLP Test Assignment

## Objective

The objective of this assignment is to extract textual data articles from the given URL and perform text analysis to compute variables as explained below.

## Data Extraction

### Input

The input data is provided in the `input.xlsx` file. For each article listed in the input file, the program should extract the article title and text and save it in a text file with the `URL_ID` as its file name.

### Tools and Libraries

You must use Python programming for data extraction. You can use libraries like BeautifulSoup, Selenium, Scrapy, or any other Python libraries for web crawling.

## Data Analysis

For each extracted text, perform textual analysis to compute the variables specified in the "Text Analysis.docx" file. The output should be saved in the exact order as given in the "Output Data Structure.xlsx" file.

### Variables

- Positive Score
- Negative Score
- Polarity Score
- Subjectivity Score
- Average Sentence Length
- Percentage of Complex Words
- FOG Index
- Average Number of Words per Sentence
- Complex Word Count
- Word Count
- Syllables per Word
- Personal Pronouns
- Average Word Length

## Output Data Structure

### Output Variables

All input variables from `Input.xlsx`, along with the variables computed during data analysis, should be included in the output. The format of the output should match the structure provided in the "Output Data Structure.xlsx" file.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/data-extraction-nlp-assignment.git
