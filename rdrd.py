import requests, re, wget, pyfiglet

print(pyfiglet.figlet_format('RDRD', font = "banner3-D"))
print('-=-=Recursive Docker Registry Downloader=-=-')
print('-=-=-=-=-=-=-Made by zw1tt3r1on-=-=-=-=-=-=-')
print('==================')

base_url = input('Enter Target URL: ')

try:
    catalog_url = f'{base_url}/_catalog'
    repositories = requests.get(catalog_url).json()['repositories']

    all_digests = []
    for repository in repositories:
        tag_list = f'{base_url}/{repository}/tags/list#'
        response = requests.get(tag_list).json()
        for tag in response['tags']:
            manifest_url = f'{base_url}/{repository}/manifests/{tag}'
            response = str(requests.get(manifest_url).json())
            digests = re.findall(r'sha256:[a-fA-F0-9]+', response)
            for digest in digests:
                print(digest)
                file_to_download = f'{base_url}/{repository}/blobs/{digest}'
                print(f'Downloading: {file_to_download}')
                file_name = wget.download(file_to_download, f'{digest.split(":")[1]}')

    print('Download Finished')
except:
    print('''Invalid Target URL
Include the "http://" and version in the target URL
Example: python3 script.py https://zw1tt3r1on.example.com/v2

Terminating Script...''')