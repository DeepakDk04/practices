from pytube import YouTube
from easy_table import EasyTable


def getLink():
    print("\n\n")
    url = input("YouTube Vedio URL >>> ")
    try:
        vedio = YouTube(url)
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
    return value


def getStreams(availableStream):
    StreamList = []
    for stream in availableStream:
        stream_info = {}
        stream_info["    ID    "] = getStreamTag(stream, "itag")
        stream_info["   Type   "] = getStreamTag(stream, "type")
        stream_info[" Resolution "] = getStreamTag(stream, "res")
        stream_info["  Format  "] = getStreamTag(stream, "mime_type")
        stream_info["   FPS    "] = getStreamTag(stream, "fps")
        stream_info["   Abr    "] = getStreamTag(stream, "abr")
        StreamList.append(stream_info)
    streamTableDisplay(StreamList)


def streamTableDisplay(table_data):
    table = EasyTable("Available Stream Types")
    table.setCorners("/", "\\", "\\", "/")
    table.setOuterStructure("|", "-")
    table.setInnerStructure("|", "-", "+")
    table.setData(table_data)
    print()
    table.displayTable()
    print()


# v = availableStream.get_by_itag(22)
# print("process started...")
# print()
# v.download(output_path="../YouTubeVedios/Downloads", filename="vedioFile")

# print("Download complete")


getLink()
