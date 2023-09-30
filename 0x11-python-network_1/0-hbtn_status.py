#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""



if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- utf8: {}".format(content.decode('utf-8')))
