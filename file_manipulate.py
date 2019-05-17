import os, shutil
from send2trash import send2trash
from zipfile import ZipFile


def toTrash(fileDir):
    send2trash(fileDir)


def extractZip(zipDir, toDir):
    zip_ref = ZipFile(zipDir, 'r')
    zip_ref.extractall(toDir)
    zip_ref.close()


def moveFile(fileDir, toDir):
    shutil.move(fileDir, toDir)
