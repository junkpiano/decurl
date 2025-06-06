import shlex

def parse(curl_command):
    tokens = shlex.split(curl_command)
    method = "GET"
    url = None
    headers = {}
    data = None

    i = 1  # skip 'curl'
    while i < len(tokens):
        token = tokens[i]
        if token in ("-X", "--request"):
            method = tokens[i + 1].upper()
            i += 2
        elif token in ("-H", "--header"):
            header = tokens[i + 1]
            if ":" in header:
                key, value = header.split(":", 1)
                headers[key.strip()] = value.strip()
            i += 2
        elif token in ("-d", "--data", "--data-raw", "--data-binary"):
            data = tokens[i + 1]
            if method == "GET":
                method = "POST"
            i += 2
        elif token.startswith("http://") or token.startswith("https://"):
            url = token
            i += 1
        else:
            i += 1

    if not url:
        raise Exception("No URL found in curl command.")

    return {
        "url": url,
        "method": method,
        "headers": headers,
        "body": data,
    }
