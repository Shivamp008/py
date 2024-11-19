import argparse 

import requests
def DownloadFile(url, local_filename):
    local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
            # if chunk: # filter out keep-alive new chunks
                f.write(chunk)
    # f.close()
    return local_filename


parser = argparse.ArgumentParser()
parser.add_argument("url", help="url of the file to download")
parser.add_argument("output", help="by which name do you want to save your file")

args = parser.parse_args()

print(args.url)
print(args.output)
DownloadFile(args.url, args.output)

