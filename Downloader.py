import time

import requests


def download_to_dir(url, outDir):
    requestor = requests.get(url, allow_redirects=True)
    fileName = fileNameFromURL(requestor.url)
    directory = '%s/%s' % (outDir, fileName)

    # Exception handling for the HTTPS request
    try:
        requestor.raise_for_status()
    except Exception as urlOof:
        print("Error in accessing URL: %s", urlOof)
        input("Press ENTER to continue...")

    print("Downloading %s" % fileName)

    # Some exception handling for file writing stuff
    try:
        file = open(directory, "wb")
        file.write(requestor.content)
        file.close()
    except IOError as e:
        print("Error writing file %s" % e)
        time.sleep(7)

    else:
        print("Download of %s Complete" % fileName)


# Finds the name of the file based on the url name (Works!)
def fileNameFromURL(url):
    if url.find('/'):
        return url.rsplit('/', 1)[1]
