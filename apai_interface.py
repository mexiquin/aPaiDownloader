import math
import PySimpleGUI as sg
from pytube import YouTube
from downloader import Downloader

menu_layout = [
    ['Help', ['Update aPai (beta)', 'About']]
]

window_layout = [
    [sg.Menu(menu_layout, )],
    [sg.Text("Welcome to aPai!", font=("helvetica", 25))],
    [sg.Frame(title="Options", layout=[
        [sg.Txt("YouTube URL:"),
         sg.Input(size=(40, 1), tooltip="Paste your youtube URL into this box", font=("helvetica", 12))],
        [sg.Txt("Format Selection:"), sg.Drop(["Default", "Audio", "Video"], font=("Helvetica", 12))],
        [sg.Txt("File Destination:"), sg.InputText(font=("helvetica", 12)), sg.FolderBrowse()]
    ])],
    [sg.Submit(button_text="Download"), sg.Quit()]
]


def main():
    window = sg.Window("aPai Downloader").Layout(window_layout)

    while True:
        event, values = window.Read()

        menu_event = values[0]
        youtube_url = values[1]
        usrFormat = values[2]
        out_dir = values[3]

        if event == 'Quit':
            break
        elif event == 'About':
            sg.Popup("About aPai Downloader", 'Version 1.0',
                     'A simple program for downloading youtube videos in whichever popular format you want')
        elif event == 'Download':
            ytDownload(youtube_url, out_dir, usrFormat)

    print(values)


'''
ytDownload method for taking input format settings
and using pytube to create youtube file on local
hard drive
'''
def ytDownload(url, outDir, fileFormat):
    yt = YouTube(url, on_progress_callback=progressCheck)
    global videosize
    if 'Default' in fileFormat:
        videosize = yt.streams.filter(progressive=True, file_extension = 'mp4').first().filesize
        yt.streams.filter(progressive=True).first().download(outDir)
    if 'Audio' in fileFormat:
        videosize = yt.streams.filter(only_audio=True).first().filesize
        yt.streams.filter(only_audio=True).first().download(outDir)
    if 'Video' in fileFormat:
        videosize = yt.streams.filter(adaptive=True).first().filesize
        yt.streams.filter(adaptive=True).first().download(outDir)

def progressCheck(stream = None, chunk = None, file_handle = None, remaining = None):
    percent = math.floor(100*((videosize - remaining)/videosize))
    sg.OneLineProgressMeter('Download Progress',percent, 100, 'key', 'Your video is downloading! :)')

if __name__ == '__main__':
    main()
