from pytube import Playlist
pl = Playlist("https://www.youtube.com/playlist?list=PL9X_7mTn8zvWg9cVSt2T8hjzUnyHK4wdz")
for video in pl.videos:
    video.streams.get_highest_resolution().download()