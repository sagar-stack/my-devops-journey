def format_url(url):
    if not url.startswith("http"):
        return "https://" + url
    return url
