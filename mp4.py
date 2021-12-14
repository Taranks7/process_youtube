#save youtube videos as mp4 videos from playlist called stimuli 
#https://youtube.com/playlist?list=PLvW5tKvokkeTIL1Au2lZTYI7glqQ9E672
import pytube

#download single video
#url = input('Enter video url: ')
#filename = input('Enter filename: ')
#video = pytube.YouTube(url)
#stream = video.streams.get_highest_resolution()
#print('Downloading video...')
#stream.download(filename=filename)
#print('Finshed Download')

#download multiple videos
video_list = []
print ('Hey!')
print ('')
print ('We re going to download some videos for you')
print ('you can either list the video url(s) or download videos from a youtube playlist')
print ('you can only download 1 youtube playlist at a time')
print ('')
print ('')
print ('Enter video url(s) below (Enter e to exit once you re done or want to move on)')
while True: 
    url = input('')
    if url == 'e':
        break
    video_list.append(url)
for x, video in enumerate(video_list):
    v = pytube.YouTube(video)
    stream = v.streams.get_highest_resolution()
    print(f'Downloading video {x+1}...')
    stream.download('source_videos')
    print('Done')
print('Completed ' +str(len(video_list))+ ' Downloads')

#download playlist
url = input('Enter playlist url: ')
playlist = pytube.Playlist(url)
for url in playlist:
    video = pytube.YouTube(url)
    stream = video.streams.get_highest_resolution()
    print('Downloading video...')
    stream.download('source_videos')
print('Finished')