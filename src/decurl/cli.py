import requests
import httpx

from decurl.core import parse

def to_requests(curl_command):
    request_info = parse(curl_command)
    response = requests.request(
        method=request_info["method"],
        url=request_info["url"],
        headers=request_info["headers"],
        data=request_info["body"]
    )

    return {
        "url": request_info["url"],
        "method": request_info["method"],
        "headers": request_info["headers"],
        "body": request_info["body"],
        "response": response
    }

def to_httpx(curl_command):
    request_info = parse(curl_command)
    response = httpx.request(
        method=request_info["method"],
        url=request_info["url"],
        headers=request_info["headers"],
        content=request_info["body"]
    )
    
    return {
        "url": request_info["url"],
        "method": request_info["method"],
        "headers": request_info["headers"],
        "body": request_info["body"],
        "response": response
    }


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Convert cURL commands to Python requests or httpx code.")
    parser.add_argument("curl_command", type=str, help="The cURL command to convert.")
    parser.add_argument("--httpx", action="store_true", help="Use httpx instead of requests.")

    args = parser.parse_args()

    if args.httpx:
        result = to_httpx(args.curl_command)
    else:
        result = to_requests(args.curl_command)

    print(f"Converted command:\n{result}")

if __name__ == "__main__":
    main()