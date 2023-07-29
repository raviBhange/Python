#Q26. Write a program to Validate url using regular expression.
import re

def validate_url(url):
    pattern = r'^(http|https)://([\w.-]+)\.([\w.-]+)/?'
    match = re.match(pattern, url)
    if match:
        return True
    else:
        return False

# Example usage
#url = "https://www.example.com" then in true statement
url=input("Enter  The Url :")
if validate_url(url):
    print("URL is valid.")
else:
    print("URL is not valid.")
