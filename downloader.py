import time
import requests
import pytube
import os


class Downloader:

    def __init__(self, url, out_dir=os.getcwd()):
        self.url = url
        self.outDir = out_dir

    def yt_or_other(self):
        if "youtube.com/watch" in self.url:
            self.video_downloader()
        else:
            self.download_to_dir()

    def set_url(self, url):
        self.url = url

    def set_out_dir(self, out_dir):
        self.outDir = out_dir

    def get_url(self):
        return self.url

    def get_out_dir(self):
        return self.outDir

    def download_to_dir(self):
        requester = requests.get(self.url, allow_redirects=True)
        file_name = self.file_name_from_url(requester.url)
        directory = '%s/%s' % (self.outDir, file_name)

        # Exception handling for the HTTPS request
        try:
            requester.raise_for_status()
        except Exception as urlOof:
            print("Error in accessing URL: %s", urlOof)
            input("Press ENTER to continue...")

        print("Downloading %s" % file_name)

        # Some exception handling for file writing stuff
        try:
            file = open(directory, "wb")
            file.write(requester.content)
            file.close()
        except IOError as e:
            print("Error writing file %s" % e)
            time.sleep(7)

        else:
            print("Download of %s Complete" % file_name)

    # Finds the name of the file based on the url name (Works!)
    def file_name_from_url(self):
        if self.url.find('/'):
            return self.url.rsplit('/', 1)[1]

    def video_downloader(self):
        pass

    def audio_helper(self):
        pass

    def video_helper(self):
        pass

    def start(self):
        self.yt_or_other()