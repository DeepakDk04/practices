from pytube import YouTube  # pip install pytube
from pytube.exceptions import LiveStreamError, RecordingUnavailable, VideoPrivate, VideoUnavailable
from easy_table import EasyTable  # pip install easy_table

URL = ''


def vedioDownload(streams, path, vedio_ID):
    # get the stream as high resolution vedio available.
    vedio = streams.get_highest_resolution()
    if vedio:
        print("Downloading...")
        vedio.download(output_path=path,
                       filename=f"youtubeVedio-{vedio_ID}")
        print("Download Complete")
    else:
        print("Error!, Can't initiate the download")


def audioDownload(streams, path, vedio_ID):
    # get the stream as high bit rate audio available.
    audio = streams.get_audio_only(subtype='mp4')
    if audio:
        print("Downloading...")
        audio.download(output_path=path,
                       filename=f"youtubeAudio-{vedio_ID}")
        print("Download Complete")
    else:
        print("Error!, Can't initiate the download")


def getUserChoice(streams, vedio_ID):
    path = "../YouTubeVedios/Downloads"
    print("\n\n")
    print("Want To Download High Quality  Vedio or Audio ?")
    print("1. Vedio\n2. Audio Only\n3. Cancel")
    choice = input("Enter Choice >>> ")
    if str(choice) == '3':
        print("Process Cancelled")
    else:
        if str(choice) == '1':
            vedioDownload(streams, path, vedio_ID)
        elif str(choice) == '2':
            audioDownload(streams, path, vedio_ID)
        else:
            print("Invalid Choice, Retry")
            getUserChoice(streams, vedio_ID)


def getVedioLink():
    global URL
    URL = input("\n\nYouTube Vedio URL >>> ")
    video_id = URL.split('?v=')[1]  # extract vedio id from URL Query.
    print("Loading...")
    try:
        vedioObject = YouTube(URL)  # convert vedio to vedio object.
        streams = vedioObject.streams  # convert vedio object to stream object.
        getUserChoice(streams, video_id)
    # known exceptions
    except LiveStreamError(video_id):
        print("Can't get Vedio")
        print("Video is a live stream.")
    except RecordingUnavailable(video_id):
        print("Can't get Vedio")
        print("Vedio Recording is Not Available")
    except VideoPrivate(video_id):
        print("Can't get Vedio")
        print("Vedio Recording is Not Available to Public, Vedio is Private")
    except VideoUnavailable(video_id):
        print("Can't get Vedio")
        print("Vedio is Not Available")
    # unknown exceptions
    except Exception as e:
        print(e)
        print("Error! Can't get vedio from this Url.")


if __name__ == "__main__":
    getVedioLink()  # only works with YOUTUBE Vedio links Not suitable for PLAYLIST links
