from pytube import YouTube


url = "https://www.youtube.com/watch?v=LcF6ut-1M94"
# def onProcess():
#     print("Processed--")

# def onComplete():
#     print("Completed--")

# vedio = YouTube(url,on_complete_callback=onComplete(),on_progress_callback=onProcess())
vedio = YouTube(url)
availableStream = vedio.streams



vedio_Stream_Info_Title = ["itag","mimetype","abr","type","fps"]
vedio_Stream_Info = [vedio_Stream_Info_Title]

for stream in availableStream:
    stream_Info = [stream.itag,stream.mime_type,stream.abr,stream.type,stream.fps]
    vedio_Stream_Info.append(stream_Info)
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
for option in vedio_Stream_Info:
    print(option)

v = availableStream.get_by_itag(22)
print("process started...")
print()
v.download(output_path="../YouTubeVedios/Downloads", filename="vedioFile")

print("Download complete")