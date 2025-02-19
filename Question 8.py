def is_valid_url(url):
    if "http://" in url or "https://" in url:
        print("Valid URL")
    else:
        print("Invalid URL")
#Here we are defining what the URL is, if it has hhttps then its valid, if not, its invalid
url = input("Enter a URL: ")
is_valid_url(url)
#Here im just asking for an input by the user




