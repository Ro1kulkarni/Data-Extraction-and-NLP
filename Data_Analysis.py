import pandas as pd  # Data manipulation and analysis library
import syllapy  # Syllable counting library
import nltk  # Natural language processing toolkit
from nltk.corpus import stopwords  # Common words to remove
from nltk.tokenize import word_tokenize, sent_tokenize  # Tokenization functions
from textblob import TextBlob  # Sentiment analysis library
import os  # Operating system interaction

nltk.download('punkt')     # 'punkt' is a pre-trained tokenizer that divides text into a list of sentences by splitting on punctuation and white spaces
nltk.download('stopwords') # 'stopwords' are common words (e.g., 'and', 'the', 'is') that are often filtered out from text during natural language processing tasks

def compute_text_analysis(text):
    if not text:
        return [None] * 14
    
    # TextBlob for sentiment analysis
    blob = TextBlob(text)
    positive_score = sum(1 for sentence in blob.sentences if sentence.sentiment.polarity > 0)
    negative_score = sum(1 for sentence in blob.sentences if sentence.sentiment.polarity < 0)
    polarity_score = blob.sentiment.polarity
    subjectivity_score = blob.sentiment.subjectivity
    
    # Tokenize text for further analysis
    words = word_tokenize(text)
    sentences = sent_tokenize(text)
    word_count = len(words)
    sentence_count = len(sentences)
    avg_sentence_length = word_count / sentence_count
    
    # Compute percentage of complex words
    stop_words = set(stopwords.words('english'))
    complex_word_count = sum(1 for word in words if word.lower() not in stop_words and syllapy.count(word) >= 3)
    percentage_complex_words = (complex_word_count / word_count) * 100
    
    # FOG Index
    fog_index = 0.4 * (avg_sentence_length + percentage_complex_words)
    
    # Compute average number of words per sentence
    avg_words_per_sentence = word_count / sentence_count
    
    # Count personal pronouns
    personal_pronouns = sum(1 for word in words if word.lower() in ['i', 'me', 'my', 'mine', 'myself', 'we', 'us', 'our', 'ours', 'ourselves'])
    
    # Compute average word length
    avg_word_length = sum(len(word) for word in words) / word_count
    
    # Compute syllable per word
    total_syllables = sum(syllapy.count(word) for word in words)
    syllables_per_word = total_syllables / word_count
    
    return [positive_score, negative_score, polarity_score, subjectivity_score, avg_sentence_length,
            percentage_complex_words, fog_index, avg_words_per_sentence, complex_word_count, word_count,
            syllables_per_word, personal_pronouns, avg_word_length]

# Specify the directory where the text files are saved
directory = "C:/Users/Hrishikesh/Desktop/rohan/Blackcoffer/Data_Extraction"

output_data = []
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        url_id = filename[:-4]  # Extract URL_ID from filename
        file_path = os.path.join(directory, filename)
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            title = lines[0].strip().split(": ")[1]  # Extract title from the first line
            url = lines[1].strip().split(": ")[1]  # Extract URL from the second line
            text = ''.join(lines[2:])  # Combine the remaining lines as text
            analysis_result = compute_text_analysis(text)
            output_data.append([url_id, url] + analysis_result)

# Create DataFrame for output data
output_columns = ['URL_ID', 'URL', 'POSITIVE SCORE', 'NEGATIVE SCORE', 'POLARITY SCORE',
                  'SUBJECTIVITY SCORE', 'AVG SENTENCE LENGTH', 'PERCENTAGE OF COMPLEX WORDS', 'FOG INDEX',
                  'AVG NUMBER OF WORDS PER SENTENCE', 'COMPLEX WORD COUNT', 'WORD COUNT', 'SYLLABLE PER WORD',
                  'PERSONAL PRONOUNS', 'AVG WORD LENGTH']
output_df = pd.DataFrame(output_data, columns=output_columns)

# Specify the output directory where you have write permissions
output_directory = "C:/Users/Hrishikesh/Desktop"

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Specify the filename for the output Excel file
output_filename = "Output Data Structure.xlsx"

# Construct the full file path
output_file_path = os.path.join(output_directory, output_filename)

# Print the output file path to verify it
print("Output file path:", output_file_path)

try:
    # Save output to Excel file with 'openpyxl' engine
    output_df.to_excel(output_file_path, index=False, engine='openpyxl')
    print("Excel file saved successfully at:", output_file_path)
except Exception as e:
    print("Error saving Excel file:", e)

# Construct the full file path
output_file_path = os.path.join(output_directory, output_filename)

# Save output to Excel file with 'openpyxl' engine
output_df.to_excel(output_file_path, index=False, engine='openpyxl')

print("Excel file saved successfully at:", output_file_path)
