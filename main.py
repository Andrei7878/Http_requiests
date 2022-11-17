import requests
import re
import json

dict_links = {}


def http_requests(text):
    for i in text:
        if re.match(r"(?P<url>https?://[^\s]+)", i):
            list_requests = [requests.get(i), requests.head(i), requests.post(i),
                             requests.put(i), requests.delete(i), requests.options(i)]
            dict_links[i] = {j.request.method: j.status_code for j in list_requests if j.status_code != 405}

            write_json(dict_links)
        else:
            print(f'"{i}" - не является ссылкой')


def write_json(dict_l):
    requests_json = json.dumps(dict_l, indent=4)

    with open("requests.json", "w") as my_file:
        my_file.write(requests_json)


data = [input() for _ in range(int(input()))]


if __name__ == '__main__':
    http_requests(data)
