import requests as rq

def download_file(url, file_name):
    # open in binary mode
    with open(file_name, "wb") as file:
        # get request
        response = rq.get(url)
        # write to file
        file.write(response.content)
