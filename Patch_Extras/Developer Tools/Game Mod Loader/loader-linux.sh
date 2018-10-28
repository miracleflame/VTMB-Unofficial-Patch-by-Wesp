#!/bin/bash

PREFIXES="$HOME/.local/share/wineprefixes"
mkdir -p "$PREFIXES"
export WINEARCH=win32
export WINEPREFIX="$PREFIXES/Vampire the Masquerade - Bloodlines"

# cd to the script’s directory
GAME_PATH=$(dirname "$(readlink -f "$0")")
cd "$GAME_PATH"

# go to parent directory, as long as no file Vampire.exe exists in current directory 
while ([ ! -f "./Vampire.exe" ] && [ ! -f "./vampire.exe" ]);
do
	if  [[ "$PWD" == "/" ]]; then
		if [ -t 1 ]; then
			echo "This already is the root directory; giving up to find Vampire.exe. This script must be placed in the Bloodlines directory or one of its subdirectories to work." 1>&2
		else
			zenity --error --text "The script’s directory and none of its parent directories contains Vampire.exe. This script must be placed in the Bloodlines directory or one of its subdirectories to work."
		fi
		exit 1
	fi
	echo "Vampire.exe not found in directory. Checking parent directory."
	cd ..
done

echo "Vampire.exe found. Assuming that this is the Bloodlines directory."

#use \n for array seperator - this will break on filenames with \n
IFS="	
"
#find all directories which have a child directory named python and put their basenames in a array
PMODS=( $(find . -maxdepth 1 -type d -exec [ -d "{}/python" ] \; -exec basename "{}" \; ) )

if [ -t 1 ]; then #from terminal
	if [ ${#PMODS[@]} -eq 0 ]; then
		echo "No mod directories detected (do you have this script in the Bloodlines directory?)" 1>&2
		exit 1
	fi
	
	#only 1 dir, normal game or total conversion and no cmd line arguments, go on automatically
	if [ ${#PMODS[@]} -eq 1 -a $# -eq 0 ]; then 
		wine vampire.exe -game "${PMODS[0]}" &
	elif [ $# -eq 1 ]; then #one argument
		#verify if it matches a dir
		mod_not_found=true
		for mod in "${PMODS[@]}"
		do
	  		if [ "$mod" == "$1" ]; then
				mod_not_found=false
			fi
		done
		if $mod_not_found; then
			echo "Single argument must match one of:" 1>&2
			printf "%s\n" "${PMODS[@]}" 1>&2
			exit 1
		fi
		wine vampire.exe -game "$1" &
	else #more than one argument or zero
		echo "Enter number to load mod:"
		select opt in "${PMODS[@]}" "Quit"; do
			if ! [ "$REPLY" -eq "$REPLY" ] 2> /dev/null; then
				echo "Invalid mod number. Try another one."
				continue
			fi
			if (( "$REPLY" >= 1 && "$REPLY" <= ${#PMODS[@]} )); then
				wine vampire.exe -game "$opt" &
			elif (( "$REPLY" == ${#PMODS[@]}+1 )); then
				exit 0
			else
				echo "Invalid mod number. Try another one."
				continue
			fi
			break
		done
	fi
else #from file manager
	if [ ${#PMODS[@]} -eq 0 ]; then
		zenity --error --text "No mod directories detected (do you have this script in the Bloodlines directory?)"
		exit 1
	fi
	
	#only 1 dir, normal game or total conversion
	if [ ${#PMODS[@]} -eq 1 ]; then
		wine vampire.exe -game "${PMODS[0]}" &
	else
		#ask the user which one
		SEL=$(zenity --list --column "mod" --title "Select mod" --text="More than one possible mod, select Vampire or ok for the original game:" "${PMODS[@]}")
		#user didn't cancel
		if [ $? -eq 0 ]; then
			#user pressed ok with nothing selected
			if [ -z "$SEL" ]; then
				wine vampire.exe &
			else
				wine vampire.exe -game "$SEL" &
			fi
		fi
	fi
fi
