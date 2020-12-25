from pytube import YouTube  # pip install pytube
from easy_table import EasyTable  # pip install easy_table

URL = ''


def downloadVedio(availableStream, itag):
    global URL
    # extract vedio id from URL Query to create unique filename.
    vedio_ID = URL.split('?v=')[1]
    filename = f"YouTubeVedio-{vedio_ID}"
    output_path = "../YouTubeVedios/Downloads"
    print("Downloading...")
    v = availableStream.get_by_itag(itag)  # load the stream selected by user
    if v:
        # check and download, if the stream is available
        v.download(output_path=output_path,
                   filename=filename)
        return True  # if downloaded successfully.
    return False  # defaults to false


def streamTableDisplay(table_data):
    table = EasyTable("Available Stream Types")
    table.setCorners("/", "\\", "\\", "/")
    table.setOuterStructure("|", "-")
    table.setInnerStructure("|", "-", "+")
    table.setData(table_data)  # setting a table object with given fields.
    print()
    table.displayTable()  # display the table for user.
    print()


def chooseStream(availableStream_Itags):
    # user choice for which stream to be downloaded.
    print("Choose Any ID from above Table to Download it\n")
    print("Enter ID to Download (or) Enter 0 to Cancel")
    user_choice = input("Enter your Choice >>> ")
    # errror cases
    if str(user_choice) == '0':
        return "cancel"
    if user_choice not in availableStream_Itags:
        print("Invalid Choice, Please enter a Vaid One\n\n")
        return chooseStream(availableStream_Itags)
    # success cases
    return user_choice


def getStreamTag(streamObject, attribute):
    # get the value for the key in stream object, if can't get mark as un available.
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
    # serialize the stream object and took only required fields.
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
        # construct available streams in a list of dictionaries to generate table display.
    streamTableDisplay(StreamList)
    choice = chooseStream(availableStream_Itags)
    if choice == "cancel":
        print("Process Cancelled")
    else:
        is_vedio_Downloaded = downloadVedio(availableStream, choice)
        if is_vedio_Downloaded:
            print("Download Complete")
        else:
            print("Error, Can't Initiate Download Process")


def getLink():
    global URL
    print("\n\n")
    URL = input("YouTube Vedio URL >>> ")
    try:
        vedio = YouTube(URL)
        availableStream = vedio.streams
        # extract stream object from the vedio object to download in file stream
    except Exception as e:
        print("Error!")
        print(e)
        print("Can't get vedio from this Url.")
    print("\n\n")
    print("\tLoading...")
    print("\n\n")
    getStreams(availableStream)


# only works with YOUTUBE Vedio links Not suitable for PLAYLIST links
if __name__ == "__main__":
    getLink()
