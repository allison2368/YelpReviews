from bs4 import BeautifulSoup

def remove_more_from_html(input_html_path):
    with open(input_html_path, 'r', encoding='utf-8') as file:
        content = file.read()

    soup = BeautifulSoup(content, 'html.parser')

    # Find and replace the word "...More" in the HTML content
    for more_tag in soup.find_all(text=lambda text: "...More" in text):
        more_tag.replace_with(more_tag.replace("...More", ""))

    return str(soup)

def create_new_html(output_html_path, modified_content):
    with open(output_html_path, 'w', encoding='utf-8') as file:
        file.write(modified_content)

def main():
    # Replace 'input_file.html' with the path to your input HTML file
    input_html_path = '/Users/allisonpeng/Downloads/chromedriver_mac_arm64/reviews_output_SF.html'

    # Remove the word "...More" from the HTML content
    modified_content = remove_more_from_html(input_html_path)

    # Replace 'output_file.html' with the desired path for the new HTML file
    output_html_path = '/Users/allisonpeng/Downloads/chromedriver_mac_arm64/reviews_output_SF3.html'

    # Create a new HTML file with the modified content
    create_new_html(output_html_path, modified_content)

    print(f'A new HTML file has been created: "{output_html_path}"')

if __name__ == "__main__":
    main()
