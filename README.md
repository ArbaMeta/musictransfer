# Musictransfer
This should help to transfer music from spotify to google music.

## Usage
- Go to Spotify and select all songs you want to copy (`cmd + a` or `ctrl + a`) and copy to clipboard (`cmd + c` or `ctrl + c`)
- Paste everything to `spotify.txt`
- Open terminal and `cd` into directory
- Run `python3 app.py`
- On the first run, it will ask you to input your email and password. These would be saved to credentials.json on your computer
- You will be presented with three options after all songs are found:
    - `Add` - would add all songs to your tracks
    - `Album name` - actually should be `Playlist name`, just type a name of Playlits you want to be created, for example 'Classical'. All songs would be added to this playlist.
    - `Quit` or `quit` - stops the sript making no changes to your Google Music
- Remember to change the `spotify.txt` next time

This script is not perfect, as sometimes not songs are added for reason unkown to me.

Hope this would help someone.

## Requirements
- Python3
- [gmusicapi](https://github.com/simon-weber/gmusicapi) `pip install gmusicapi`
- [tqdm](https://pypi.python.org/pypi/tqdm) `pip install tqdm`
- Mac (needed fpr gmusicapi)
    - Use [Homebrew](http://brew.sh/) to install [libav (avconv)](http://braumeister.org/formula/libav) or [ffmpeg](http://braumeister.org/formula/ffmpeg)
- Windows (needed fpr gmusicapi)
    - Download pre-built binaries of [avconv](http://win32.libav.org/releases/) or [ffmpeg](http://ffmpeg.zeranoe.com/builds/) and [edit your path](http://www.computerhope.com/issues/ch000549.htm) to include the directory that contains avconv.exe/ffmpeg.exe

Had to switch to Google Music, because Spotify is not available in my country