#!/usr/bin/env python

import os
import sys
from subprocess import call
from shutil import move

cmd = ['ffmpeg', '-i', '', '-acodec', 'libmp3lame', '-ab', '128k', '']

if __name__ == '__main__':
    files = os.listdir()
    ifiles = []
    for f in files:
        if f.endswith('m4a'):
            ifiles.append(f)
    for ifile in ifiles:
        output_dir = os.path.join(os.path.curdir, 'mario')
        backup_dir = os.path.join(os.path.curdir, 'treated')
        ofile = os.path.join(output_dir, ifile[:-3] + "mp3")
        cmd[2] = ifile
        cmd[7] = ofile
        call(cmd)
        move(ifile, backup_dir)
