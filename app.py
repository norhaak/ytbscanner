#!/usr/bin/env python

import os
import sys
from subprocess import call
from shutil import move


DOWNLOADED_DIR = "downloaded"
TREATED_DIR = "treated"
BACKUP_DIR = "backup"

conv_audio_cmd = ['ffmpeg', '-i', '', '-acodec', 'libmp3lame', '-ab', '128k', '']
get_audio_cmd = ['youtube-dl', '-f', '140', '']
get_video_cmd = ['youtube-dl', '-f', '18']


def convert(ifile):
    output_dir = os.path.join(os.path.curdir, TREATED_DIR)
    backup_dir = os.path.join(os.path.curdir, BACKUP_DIR)
    ofile = os.path.join(output_dir, ifile[:-3] + "mp3")
    conv_audio_cmd[2] = ifile
    conv_audio_cmd[7] = ofile
    call(conv_audio_cmd)
    move(ifile, backup_dir)


def convertAll():
    files = os.listdir(DOWNLOADED_DIR)
    ifiles = []
    for f in files:
        if f.endswith('m4a'):
            ifiles.append(f)
    for ifile in ifiles:
        convert(ifile)


def download(video_id, video_format):
    output_dir = os.path.join(os.path.curdir, DOWNLOADED_DIR)
    get_audio_cmd[3] = video_id
    print(get_audio_cmd)
    os.chdir(output_dir)
    call(get_audio_cmd)
    print('download completed...')



if __name__ == '__main__':
    video_id = input('youtube video_id: ')
    while video_id not in ('q', 'quit'):
        download(video_id, 'audio')
        video_id = input('youtube video_id: ')
    print('Bye ;). See next time!')
