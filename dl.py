from pytube import YouTube, Stream
import subprocess
import os

root = ""


def start(url: str, onprog=None):
    try:
        yt = YouTube(url)
        vlist = yt.streams.filter(subtype='mp4', only_video=True).order_by('resolution').desc()
        alist = yt.streams.filter(subtype='mp4', only_audio=True).order_by('bitrate').desc()
    except KeyError:
        return "unavailable"

    print(vlist)
    print(alist)

    if alist.__len__()==0 or vlist==0:
        return "unavailable a or v"

    yt.register_on_progress_callback(onprog)

    original_name = yt.player_config_args['title']
    if original_name == 'YouTube':
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(yt.watch_html, 'lxml')
        original_name = soup.findAll("meta", attrs={'name': 'title'}, recursive=True)[0]['content']

    original_name: str
    original_name = original_name.replace(":", '').replace(".", '').replace("-", '')
    print(original_name)

    tmp = str(abs(original_name.__hash__()))

    print("audio:")
    alist[0].download("tmp\\", filename=tmp + 'a')
    print("video:")
    vlist[0].download("tmp\\", filename=tmp + 'v')

    try:
        merge("tmp\\" + tmp + 'a.mp4', "tmp\\" + tmp + 'v.mp4', out=root + "tmp\\" + tmp + ".mp4")
        os.remove("tmp\\" + tmp + 'a.mp4')
        os.remove("tmp\\" + tmp + 'v.mp4')
        os.replace("tmp\\" + tmp + ".mp4", "tmp\\" + original_name + ".mp4")
    except Exception:
        return "invalid file"

    return "done"


def merge(audio, video, ffmpeg=root + "lib\\bin\\ffmpeg", out=root + "tmp\\out.mp4"):
    c = [ffmpeg, " -i ", "\"" + video + "\"", " -i ", "\"" + audio + "\"", "-c:v", "copy", "-c:a", "aac", "-strict",
         "experimental", "\"" + out + "\""]
    c = ffmpeg + ' -i "' + video + '"' + ' -i "' + audio + '"' + ' -c:v copy -c:a aac -strict experimental "' + out + '"'
    p = subprocess.check_output(c, shell=True)
    pass



