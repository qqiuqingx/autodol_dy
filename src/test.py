
import requests
from urllib.parse import unquote, urlparse, parse_qs, urlencode, urlunparse
def my_function():
    fake_headers={
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
            'Referer':'https://live.douyin.com/'
    }
    page = requests.get(
                build_request_url(f"https://v.douyin.com/idwQmndN/"),
                headers=fake_headers, timeout=5).text
    return "result"


def build_request_url(url: str) -> str:
        parsed_url = urlparse(url)
        existing_params = parse_qs(parsed_url.query)
        existing_params['aid'] = ['6383']
        existing_params['device_platform'] = ['web']
        existing_params['browser_language'] = ['zh-CN']
        existing_params['browser_platform'] = ['Win32']
        existing_params['browser_name'] = ['Chrome']
        existing_params['browser_version'] = ['92.0.4515.159']
        new_query_string = urlencode(existing_params, doseq=True)
        new_url = urlunparse((
            parsed_url.scheme,
            parsed_url.netloc,
            parsed_url.path,
            parsed_url.params,
            new_query_string,
            parsed_url.fragment
        ))
        return new_url
if __name__ == "__main__":
    #config.load(None)
    url = "https://live.douyin.com/105217819063"
    # url='https://v.douyin.com/idTmHYJ1/'
    fname = "output_file"
    #result = download_from_url(url, fname)
    my_function()
    #print(result)