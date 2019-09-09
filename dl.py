from pytube import YouTube
import subprocess

root = ""


class yt_downloader:
    def __init__(self):
        self.file_size = -1
        self.pre = 0

    def download(self, target, outname, ext):
        self.file_size = target.filesize

        print("download start " + "tmp/" + outname + ext)

        s = str(outname).replace("/", " ").replace("\\", " ").replace("*", " ").replace(":", " ") \
            .replace("?", " ").replace("\"", " ").replace("<", " ").replace(">", " ").replace("|", " ")
        target.download("tmp/", filename=s)
        print("download finish " + "tmp/" + s)
        return "tmp\\" + s + ext
        pass

    def merge(self, audio, video, ffmpeg=root + "lib\\bin\\ffmpeg", out=root + "tmp\\out.mp4"):
        c = [ffmpeg, " -i ", "\"" + video + "\"", " -i ", "\"" + audio + "\"", "-c:v", "copy", "-c:a", "aac", "-strict",
             "experimental", "\"" + out + "\""]
        c = ffmpeg + ' -i "' + video + '"' + ' -i "' + audio + '"' + ' -c:v copy -c:a aac -strict experimental "' + out + '"'
        p = subprocess.check_output(c, shell=True)
        pass

    def find(self, url, opt="mp4 best v+a", progressor=None):
        yt = YouTube(url, on_progress_callback=self.outer(progressor))
        title = yt.title
        if opt == "mp4 best v+a":
            return title, [yt.streams.filter(adaptive=True, file_extension="mp4").first(),
                           yt.streams.filter(only_audio=True, file_extension="mp4").first()]
            pass
        elif opt == "mp4 best a":
            return title, [yt.streams.filter(only_audio=True, file_extension="mp4").first()]
            pass
        elif opt == "mp4 best v":
            return title, [yt.streams.filter(adaptive=True, file_extension="mp4").first()]
            pass
        elif opt == "mp4 v+a":
            return title, [yt.streams.filter(progressive=True, file_extension="mp4").first()]
            pass

    def outer(self, progressor=None):
        def plog(stream=None, chunk=None, file_handle=None, remaining=None):
            nonlocal progressor
            # Gets the percentage of the file that has been downloaded.
            percent = int((100 * (self.file_size - remaining)) / self.file_size)
            if percent < 0:
                percent = 0
            elif not int(percent) == int(self.pre):
                if progressor == None:
                    print("{:00.0f}% downloaded".format(percent))
                else:
                    progressor.setprogress(percent)
                    pass
                self.pre = percent

        return plog
        pass
