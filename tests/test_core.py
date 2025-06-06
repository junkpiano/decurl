import decurl

def test_basic_parse():
    curl = 'curl -X GET https://example.com'
    parsed = decurl.parse(curl)
    assert parsed["method"] == "GET"
    assert parsed["url"] == "https://example.com"

def test_parse_with_headers():
    curl = 'curl -X POST -H "Content-Type: application/json" https://example.com'
    parsed = decurl.parse(curl)
    assert parsed["method"] == "POST"
    assert parsed["url"] == "https://example.com"
    assert parsed["headers"]["Content-Type"] == "application/json"


def test_parse_with_data():
    curl = 'curl -X POST --data "key=value" https://example.com'
    parsed = decurl.parse(curl)
    assert parsed["method"] == "POST"
    assert parsed["url"] == "https://example.com"
    assert parsed["body"] == "key=value"

def test_parse_infer_post():
    curl = 'curl --data "key=value" https://example.com'
    parsed = decurl.parse(curl)
    assert parsed["method"] == "POST"
    assert parsed["url"] == "https://example.com"
    assert parsed["body"] == "key=value"

def test_parse_with_multiple_headers():
    curl = 'curl -X GET -H "Accept: application/json" -H "Authorization: Bearer token" https://example.com'
    parsed = decurl.parse(curl)
        
    assert parsed["url"] == "https://example.com"
    assert parsed["headers"]["Accept"] == "application/json"
    assert parsed["headers"]["Authorization"] == "Bearer token"

