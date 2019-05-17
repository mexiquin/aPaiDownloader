import PySimpleGUI as sg
import threading
import pytube
from downloader import Downloader

menu_layout = [
    ['Tools', ['Get ffmpeg', 'Get youtube-dl']],
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
            bgThread = threading.Thread(target=ytDownload(youtube_url, out_dir, usrFormat))
            print("Download Button Pressed!")

    print(values)


'''
ytDownload method for taking input format settings
and using pytube to create youtube file on local
hard drive
'''
def ytDownload(url, outDir, fileFormat):
    pass


if __name__ == '__main__':
    main()
