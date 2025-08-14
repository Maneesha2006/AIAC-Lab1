import re

def extract_urls(text):
    
    url_pattern = r'(https?://[^\s]+|www\.[^\s]+)'
    urls = re.findall(url_pattern, text)
    return urls

if __name__ == "__main__":
    sample_text = """
    Here are some links: https://www.example.com, http://test.org/page?query=1, and www.sample.net.
    Not a url: ftp://not-included.com or just some text.
    """
    urls = extract_urls(sample_text)
    print("Extracted URLs:")
    for url in urls:
        print(url)

