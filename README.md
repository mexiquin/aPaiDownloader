# Welcome to aPai!

aPai is a little project I started in order to help my Mom download karaoke songs from YouTube

## Building the Executable
The .exe is included in the _dist_ folder, but if you need to build this yourself, here's how: 

### Requirements
* You will need python installed (version 3.7 preferrably)
* With python installed, you will need to install _pyinstaller_
```bash
pip install pyinstaller
```

To build the .exe file, all you need to do is type this command into a terminal:
```bash
pyinstaller --onefile --windowed apai_interface.py
```

This should compile all dependencies into the singular .exe file inside your newly created _dist_ folder. 

This process is subject to change, but I will be sure to update this file as those changes arise.
