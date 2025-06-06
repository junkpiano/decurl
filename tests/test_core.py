import decurl

def test_basic_parse():
    curl = 'curl -X GET https://example.com'
    parsed = decurl.parse(curl)
    assert parsed["method"] == "GET"
    assert parsed["url"] == "https://example.com"