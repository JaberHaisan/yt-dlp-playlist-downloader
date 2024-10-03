import yt_dlp
import os

# help(yt_dlp.YoutubeDL) for option details

download_archive_file = r"F:\Youtube-dl\downloaded_songs.txt"

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
		"subtitleslangs": ['en', '-live_chat'],
		"format_sort": ["ext:mp4:m4a",],
		"download_archive": download_archive_file,
		"force_write_archive": True,
		'postprocessors': [{
				'key': 'FFmpegVideoConvertor',
				'preferedformat': 'mp4'  
			}],
	}	
	with yt_dlp.YoutubeDL(ydl_opts) as ydl:
		ydl.download([link])
	
	print("\n\nDownload Completed for playlist.")
	uin = input("Do you want to continue? (y/n): ").lower()
	if uin == "n":
		leave = True
	
