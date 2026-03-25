from utility import format_url

def test_formal_url_adds_https():
    # If i give it 'google.com'. It should return 'https://google.com'
    assert format_url("google.com") == "https://google.com"

def test_format_url_leaves_http_alone():
    # If it already has it, it shouldnt change anything
    assert format_url("https://github.com") == "https://github.com"
