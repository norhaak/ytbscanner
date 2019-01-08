#!/usr/bin/env python

import os
import sys
import re
from subprocess import call
from shutil import move


DOWNLOADED_DIR = "downloaded"
TREATED_DIR = "treated"
BACKUP_DIR = "backup"

conv_audio_cmd = ['ffmpeg', '-i', '', '-acodec', 'libmp3lame', '-ab', '128k', '']
get_audio_cmd = ['youtube-dl', '-f', 'best', '']
get_video_cmd = ['youtube-dl', '-f', 'best', '']


def initConfig():
    app_folders = [DOWNLOADED_DIR, TREATED_DIR, BACKUP_DIR]
    for folder in app_folders:
        if not os.path.isdir(folder):
            os.mkdir(folder)

def getVideoIdFromUrl(video_url):
    video_id = re.search("\?v=(\D*)", video_url).group(1)
    return video_id


def convert(ifile):
    """
    Convert audio file to mp3 format.
    """
    output_dir = os.path.join(os.path.curdir, TREATED_DIR)
    backup_dir = os.path.join(os.path.curdir, BACKUP_DIR)
    ofile = os.path.join(output_dir, ifile[:-3] + "mp3")
    ifile_path = os.path.join(DOWNLOADED_DIR, ifile)
    conv_audio_cmd[2] = ifile_path
    conv_audio_cmd[7] = ofile
    call(conv_audio_cmd)
    move(ifile_path, backup_dir)


def convertAll():
    download_dir = os.path.join(os.path.curdir, DOWNLOADED_DIR)
    files = os.listdir(download_dir)
    ifiles = []
    for f in files:
        if f.endswith('m4a'):
            ifiles.append(f)
    for ifile in ifiles:
        convert(ifile)


def download(video_id, dl_format):
    output_dir = os.path.join(os.path.curdir, DOWNLOADED_DIR)
    if dl_format == 'audio':
        get_audio_cmd[3] = video_id
        cmd = get_audio_cmd
    elif dl_format == 'video':
        get_video_cmd[3] = video_id
        cmd = get_video_cmd
    os.chdir(output_dir)
    try:
        print(cmd)
        call(cmd)
        print('download completed...')
    except:
        print("Something wrong happend...Sorry!")
    



if __name__ == '__main__':
    initConfig()
    video_url = input('youtube video_id: ')
    while video_url not in ('q', 'quit'):
        if video_url == 'convert':
            convertAll()
        else:
            dl_format = input('download format? [audio]: ')
            download(video_url, dl_format)
        video_url = input('youtube video_id: ')
    print('Bye ;). See you next time!')
