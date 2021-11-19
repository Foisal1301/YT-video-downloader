import os
try:
	import pytube
except:
	os.system("python3 -m pip install pytube")
	import pytube
	print("\n\n\n")
link = input('Enter your link:')
path = input("Where will it be downloaded(default=blank):")
if path == "":
	path = f"C:\\Users\\{os.getenv('USER',os.getenv('USERNAME','user'))}\\Desktop"
try:
	yt = pytube.YouTube(link)
	yt.streams.get_highest_resolution().download(path)
	input('Successfully downloaded!!\nPress enter to exit....')
except:
	input('Download failed!\nPress enter to exit....')
