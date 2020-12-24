from pytube import YouTube
from easy_table import EasyTable

URL = ''


def getLink():
    global URL
    print("\n\n")
    URL = input("YouTube Vedio URL >>> ")
    try:
        vedio = YouTube(URL)
        availableStream = vedio.streams
    except Exception as e:
        print(e)
        print("Can't get vedio from this Url.")
    print("\n\n")
    print("\tLoading...")
    print("\n\n")
    getStreams(availableStream)


def getStreamTag(streamObject, attribute):
    try:
        if attribute == 'itag':
            value = streamObject.itag
        elif attribute == 'mime_type':
            value = streamObject.mime_type
        elif attribute == 'abr':
            value = streamObject.abr
        elif attribute == 'res':
            value = streamObject.resolution
        elif attribute == 'type':
            value = streamObject.type
        elif attribute == 'fps':
            value = streamObject.fps
        else:
            value = ''
    except Exception as e:
        print(e)
        value = "Not Available"
    return str(value)


def getStream(stream):
    stream_info = {}
    stream_info["    ID    "] = getStreamTag(stream, "itag")
    stream_info["   Type   "] = getStreamTag(stream, "type")
    stream_info[" Resolution "] = getStreamTag(stream, "res")
    stream_info["  Format  "] = getStreamTag(stream, "mime_type")
    stream_info["   FPS    "] = getStreamTag(stream, "fps")
    stream_info["   Abr    "] = getStreamTag(stream, "abr")
    return stream_info


def getStreams(availableStream):
    StreamList = []
    availableStream_Itags = []
    for stream in availableStream:
        stream_info = getStream(stream)
        # availableStream_Itags used later to select the file to download
        availableStream_Itags.append(stream_info.get("    ID    ", None))
        StreamList.append(stream_info)
    streamTableDisplay(StreamList)
    choice = chooseStream(availableStream_Itags)
    if choice == "cancel":
        print("Process Cancelled")
        return None
    else:
        downloadVedio(availableStream, choice)


def streamTableDisplay(table_data):
    table = EasyTable("Available Stream Types")
    table.setCorners("/", "\\", "\\", "/")
    table.setOuterStructure("|", "-")
    table.setInnerStructure("|", "-", "+")
    table.setData(table_data)
    print()
    table.displayTable()
    print()


def chooseStream(availableStream_Itags):
    print("Choose Any ID from above Table to Download it\n")
    print("Enter ID to Download (or) Enter 0 to Cancel")
    user_choice = str(input("Enter your Choice >>> "))
    # errror cases
    if user_choice == 0:
        return "cancel"
    if user_choice not in availableStream_Itags:
        print("Invalid Choice, Please enter a Vaid One\n\n")
        chooseStream(availableStream_Itags)
    # success cases
    return user_choice


def downloadVedio(availableStream, itag):
    vedio_ID = URL.split('?v=')[1]  # extract vedio id from URL Query
    print("Downloading...")
    v = availableStream.get_by_itag(itag)
    if v:
        v.download(output_path="../YouTubeVedios/Downloads",
                   filename=f"YouTubeVedio-{vedio_ID}")
    else:
        print("Error, Can't Initiate Download Process")
    print("Download Complete")


getLink()  # only works with YOUTUBE Vedio links Not suitable for PLAYLIST links
test_vedio_link = "https://www.youtube.com/watch?v=l73dA-A0Si4"  # tested OK
