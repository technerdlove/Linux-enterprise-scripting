#!/bin/bash

sudo yum -y install git
git clone https://github.com/viridityforever/NTI300-assignments/
git clone https://github.com/nic-instruction/NTI-300/

echo "A clone of the NTI300-assignments repository is now sitting in this dir, along with a copy of this script"
echo "For a git command line cheat sheet check out https://services.github.kit/downloads/github-git-cheat-sheet.pdf"
echo "Basic commands:
	git pull		# will get you repo updates
	git add			# will add files in your dir
	git add <dirname>/*	# will add files under a new dir
	git commit -m		# will commit your code to your changes
	git push		# will push your code to a repository
	git pull		# will pull down new repository updates"
