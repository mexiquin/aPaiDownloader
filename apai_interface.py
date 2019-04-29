import PySimpleGUI as sg

menu_layout = [
    ['Tools', ['Get ffmpeg', 'Get youtube-dl']],
    ['Help', ['Update aPai (beta)', 'About']]
]

window_layout = [
    [sg.Menu(menu_layout, )],
    [sg.Text("Welcome to aPai!", font=("helvetica", 25))],
    [sg.Frame(title="Options", layout=[
        [sg.Txt("YouTube URL:"), sg.Input(size=(40, 1), tooltip="Paste your youtube URL into this box", font=("helvetica", 12))],
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
        format = values[2]
        out_dir = values[3]

        if event == 'Quit':
            break
        elif event == 'About':
            sg.Popup("About aPai Downloader", 'Version 1.0', 'A simple program for downloading youtube videos in '
                                                             'whichever popular format you want')

    print(values)


if __name__ == '__main__':
    main()
