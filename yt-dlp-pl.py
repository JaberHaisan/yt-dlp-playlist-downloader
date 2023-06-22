import yt_dlp
import os

# Create a new directory for songs if it doesn't exist
# and move to it.
os.makedirs("Songs", exist_ok=True)
os.chdir(r".\Songs")

leave = False
while not leave:
	link = input("Youtube playlist link: ")
	playlist_items = input("Enter playlist items to be downloaded: ")

	ydl_opts = {
		"writesubtitles": True,
		"playlist_items": playlist_items,
		"ignoreerrors": True,
		"subtitleslangs": ['en', '-live_chat']
	}	
	with yt_dlp.YoutubeDL(ydl_opts) as ydl:
		ydl.download([link])
	
	print("\n\nDownload Completed for playlist.")
	uin = input("Do you want to continue? (y/n): ").lower()
	if uin == "n":
		leave = True
	
