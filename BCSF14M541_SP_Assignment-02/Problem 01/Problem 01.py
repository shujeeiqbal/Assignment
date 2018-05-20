"""
Shujee Iqbal
BCSF14M541
System Programming
Task 1: Downloads and merges last 26 clips of quran recitation of every recieter in the given link.
"""

from bs4 import BeautifulSoup
import requests
import os
from datetime import datetime
from glob import iglob
import shutil
import urllib.request

f = open("log.txt","w+")

def getSource(urlstr):
	return requests.get(urlstr)


def get_all_links(URL):	
	req = getSource(URL)
	links = []
	
	if req.status_code == 200:
		parser_obj = BeautifulSoup(req.content, "html.parser")
		tags_list = parser_obj.find_all("a")
		for tag in tags_list[1:]:
			links.append(tag["href"])
	else:
		print("Some error occured.")
		exit()
				
	return links


def download_audio_files(qari_name, url_list):
        i = 0
        PATH = r'quran/%s' % qari_name
        if not os.path.exists(PATH):
                os.makedirs(PATH)
        for audio_url in url_list[-26:]:
                i+=1
                print("{2} Downloading surah {0}. ({1}/26)".format(audio_url.split('.')[0], i, datetime.now()))
                f.write("{2} Downloading surah {0}. ({1}/26)\n".format(audio_url.split('.')[0], i, datetime.now()))
                urllib.request.urlretrieve("https://download.quranicaudio.com/quran/{0}/{1}".format(qari_name, audio_url), "quran/{0}/{1}".format(qari_name, audio_url))


def merge_audio_files(qari_name):
	destination = open('quran/{0}/merging'.format(qari_name), 'wb')
	for filename in iglob(os.path.join('quran/{0}/'.format(qari_name), '*.mp3')):
		shutil.copyfileobj(open(filename, 'rb'), destination)
	destination.close()
	os.rename('quran/{0}/merging'.format(qari_name), 'quran/{0}/mergedrecitation.mp3'.format(qari_name))


def main():
	URL = "https://download.quranicaudio.com/quran/"
	i = 0

	print("{0} Getting reciter list...".format(datetime.now()))
	f.write("{0} Getting reciter list...\n".format(datetime.now()))
	qari_list = get_all_links(URL)
	print("{1} Number of reciters: {0}".format(len(qari_list), datetime.now()))
	f.write("{1} Number of reciters: {0}\n".format(len(qari_list), datetime.now()))
	print("......................")
	f.write("......................\n")
	
	for qari in qari_list:
		i+=1
		print('{2} Processing reciter no. {0}, reciter: {1}'.format(i,qari[:-1], datetime.now()))
		f.write('{2} Processing reciter no. {0}, reciter: {1}\n'.format(i,qari[:-1], datetime.now()))
		print(('{0} Getting surah list...'.format(datetime.now())))
		f.write('{0} Getting surah list...\n'.format(datetime.now()))		
		surah_list = get_all_links("https://download.quranicaudio.com/quran/%s" % qari)		
		print("{1} Number of surah found: {0}".format(len(surah_list), datetime.now()))
		f.write("{1} Number of surah found: {0}\n".format(len(surah_list), datetime.now()))
		qari = qari[:-1]
		download_audio_files(qari, surah_list)
		print("{0} Downloading complete. Now merging files.".format(datetime.now()))
		f.write("{0} Downloading complete. Now merging files.\n".format(datetime.now()))
		merge_audio_files(qari)
		print("{0} Merging complete.".format(datetime.now()))
		f.write("{0} Merging complete.\n".format(datetime.now()))
		print("......................")
		f.write("......................\n")


if __name__ == "__main__":
    main()
