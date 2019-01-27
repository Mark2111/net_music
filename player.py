#!/usr/bin/python2
import os, sys, urllib



def create_playlist(server):
	os.system("./create_playlist.sh {0}".format(server))

def custom_des(link):
	new_var = ""
	for ch in link:
		if ch == "+":
			new_var += " "
			continue
		new_var += ch
	return new_var

def playlist():
	print "~~~Playlist~~~\n\n"
	with open('output.txt') as fp:
		i = 1
		for line in fp:
			sys.stdout.write(str(i) + "   " + custom_des(urllib.unquote(line)))
			i += 1



def play(server, song):
	with open('output.txt') as file:
		lines = file.readlines()
	os.system("ffplay -nodisp -autoexit -loglevel quiet {0}/{1}".format(server, lines[song-1]))




def main():
	server = raw_input("Server address:   ")
	create_playlist(server)
	
	while True:
		playlist()
		print ""
		x = raw_input("Enter song number:   ")
		if x == "":
			quit()
		play(server, int(x))

if __name__ == "__main__":
	main()