import requests
from bs4 import BeautifulSoup

# Standard headers to fetch a website
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

def fetch_website_contents(url):
    """
    Return the title and contents of the website at the given url;
    truncate to 2,000 characters as a sensible limit
    """

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.title.string if soup.title else "title not found"
    if soup.body:
        for irrelevant in soup.body(["script", "style", "img", "input"]):
            irrelevant.decompose()
        text = soup.body.get_text(separator="\n", strip=True)
    else:
        text = ""
    
    return (title + '\n\n' + text)[:2000]



def fetch_website_links(url):
    """
    Return the links on the webiste at the given url
    """
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    links = [link.get("href") for link in soup.find_all("a")]
    return [link for link in links if link]





















"""
response = requests.get(url, headers=headers)

This sends an HTTP GET request to the URL.

Meaning:
requests.get(...) downloads the webpage
headers=headers sends extra request metadata (often to pretend to be a normal browser)

Example of headers:
headers = {
    "User-Agent": "Mozilla/5.0"
}

Why use headers?
Some websites block “bot-like” requests
A browser-like User-Agent often helps

--------------------------------------------------------------------------------------------------

soup = BeautifulSoup(response.content, "html.parser")

This parses the downloaded HTML using BeautifulSoup.

Meaning:
response.content = raw HTML of the page
BeautifulSoup(..., "html.parser") turns the HTML into a structure you can search

So instead of manually reading HTML tags, you can do things like:
soup.title
soup.body
soup.find(...)

----------------------------------------------------------------------------------------------------

for irrelevant in soup.body(["script", "style", "img", "input"]):
   irrelevant.decompose()

This removes unwanted elements from the page before extracting text.

Tags removed:
<script> → JavaScript code
<style> → CSS styling
<img> → images
<input> → form fields

Why remove them?
Because they usually do not help if your goal is readable text.

decompose()
Completely removes that element from the parsed HTML tree.

----------------------------------------------------------------------------------------------------

text = soup.body.get_text(separator="\n", strip=True)

This extracts plain text from the webpage body.

Parameters:
separator="\n" → put each block on a new line
strip=True → remove extra whitespace at the beginning/end

So HTML like:
<body>
  <h1>Hello</h1>
  <p>Welcome to my site</p>
</body>

becomes roughly:
"Hello\nWelcome to my site"

----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------

Find all anchor tags and extract href values

links = [link.get("href") for link in soup.find_all("a")]

This is the most important line.
soup.find_all("a")

Finds all HTML anchor tags:
<a href="https://google.com">Google</a>
<a href="/about">About</a>
<a>Broken link</a>

link.get("href")
For each <a> tag, it gets the value of the href attribute.

So this line builds a list like:
[
    "https://google.com",
    "/about",
    None
]

Why None?
Because some <a> tags may exist without an href.

----------------------------------------------------------------------------------------------------

Remove empty or missing links:

return [link for link in links if link]

This filters out invalid values like:
None
empty strings ""

So if links is:
["https://google.com", "/about", None, ""]

It returns:
["https://google.com", "/about"]

----------------------------------------------------------------------------------------------------
"""