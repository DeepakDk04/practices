from pytube import YouTube
from easy_table import EasyTable


def getLink():
    url = input("YouTube Vedio URL >>> ")
    try:
        vedio = YouTube(url)
        availableStream = vedio.streams
    except Exception as e:
        print(e)
    getStreams(availableStream)

def getStreamTag(stream,attribute):
    try:
        value = stream.attribute
    except Exception:
        value = "Not Available"
    return value

def getStreams(availableStream):
    StreamList = []
    for stream in availableStream:
        print("Whole Stream ", stream)
        stream_info = {}
        stream_info["   Itag   "] = getStreamTag(stream,"itag")
        stream_info[" MimeType "] = getStreamTag(stream,"mime_type")
        stream_info["   Abr    "] = getStreamTag(stream,"abr")
        stream_info["   Res    "] = getStreamTag(stream,"res")
        stream_info[" Progressive "] = getStreamTag(stream,"progressive")
        stream_info["   Type   "] = getStreamTag(stream,"type")
        stream_info["   Fps    "] = getStreamTag(stream,"fps")
        print("Taken Stream ", stream_info)
        StreamList.append(stream_info)
    streamTableDisplay(StreamList)
    # vedio_Stream_Info_Title = ["itag", "mimetype", "abr", "type", "fps"]
    # vedio_Stream_Info = [vedio_Stream_Info_Title]

    # for stream in availableStream:
    #     stream_Info = [stream.itag, stream.mime_type,
    #                 stream.abr, stream.type, stream.fps]
    #     vedio_Stream_Info.append(stream_Info)
    # add table format here using table library --pip install easy-table let user choose fps

    # print()
    # print("itag", stream.itag)
    # print("mimetype", stream.mime_type)
    # print("abr", stream.abr)
    # # print(stream.progressive)
    # print("type", stream.type)
    # print("fps", stream.fps)
    # print()
    # print(stream.res)
    # for option in vedio_Stream_Info:
    #     print(option)


# table_data should be list of key value pairs  [
#     {"id": 1, "name": "Tim", "age": 33},
#     {"id": 2, "name": "Bob", "age": 28},
#     {"id": 3, "name": "John", "age": 41}
#   ]

def streamTableDisplay(table_data):
    table = EasyTable("Available Stream Types")
    table.setCorners("/", "\\", "\\", "/")
    table.setOuterStructure("|", "-")
    table.setInnerStructure("|", "-", "+")
    table.setData(table_data)
    print()
    table.displayTable()


# v = availableStream.get_by_itag(22)
# print("process started...")
# print()
# v.download(output_path="../YouTubeVedios/Downloads", filename="vedioFile")

# print("Download complete")


getLink()