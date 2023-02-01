def get_domain(url):
    """Returns the domain of the given URL."""
    from urllib.parse import urlparse
    parsed_url = urlparse(url)
    return parsed_url.netloc

def is_valid(url):
    """Returns True if the given URL is valid, False otherwise."""
    from urllib.parse import urlparse
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False
