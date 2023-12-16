import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

# Download VADER lexicon (run once)
nltk.download('vader_lexicon')

def read_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def extract_text_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    text = ' '.join([p.get_text() for p in soup.find_all('p')])
    return text

def perform_sentiment_analysis(text):
    # Remove all occurrences of the word 'more'
    text_without_more = text.replace('more', '')

    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(text_without_more)
    return sentiment_scores

def plot_sentiment_analysis(sentiment_scores, title):
    labels = ['Positive', 'Neutral', 'Negative']
    sizes = [sentiment_scores['pos'], sentiment_scores['neu'], sentiment_scores['neg']]
    colors = ['green', 'gray', 'red']

    plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
    plt.title(title)
    plt.show()

def main():
    # Replace 'file1.html' and 'file2.html' with the actual file paths
    file1_path = '/Users/allisonpeng/Downloads/chromedriver_mac_arm64/reviews_output_SF3.html'
    file2_path = '/Users/allisonpeng/Downloads/chromedriver_mac_arm64/reviews_outputSF_yelp.html'

    # Read HTML files
    html_content1 = read_html_file(file1_path)
    html_content2 = read_html_file(file2_path)

    # Extract text from HTML content
    text1 = extract_text_from_html(html_content1)
    text2 = extract_text_from_html(html_content2)

    # Combine text from both HTML files
    combined_text = text1 + ' ' + text2

    # Perform sentiment analysis on the combined text (with 'more' removed)
    sentiment_scores_combined = perform_sentiment_analysis(combined_text)

    # Display results
    print(f"Sentiment Analysis for Combined Text (without 'more'):")
    print(f"Positive: {sentiment_scores_combined['pos']:.2f}")
    print(f"Neutral: {sentiment_scores_combined['neu']:.2f}")
    print(f"Negative: {sentiment_scores_combined['neg']:.2f}")

    # Plot the sentiment analysis results as a pie chart
    plot_sentiment_analysis(sentiment_scores_combined, 'Sentiment Analysis for San Francisco Reviews')

if __name__ == "__main__":
    main()
