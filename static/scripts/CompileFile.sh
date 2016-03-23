DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PARENT_DIR="$(dirname "$DIR")"
FOLDER="mysite/static/Lilypond-Files"
COMPILE_PATH="$DIR/$FOLDER"

FILENAME="Sheet.ly"	#Lilypond file that should be compiled
LILYPOND_COMPILE_FILE_PATH="/Applications/LilyPond.app/Contents/Resources/bin/lilypond "
LP_PARENT_PATH="/Applications/LilyPond.app/Contents/Resources/bin"

echo $DIR
echo $PARENT_DIR
echo $COMPILE_PATH

cd "$COMPILE_PATH"
#pwd

#run lilypond with file as input
~/bin/lilypond $FILENAME
#~/bin/lilypond -dbackend=eps -dno-gs-load-fonts -dinclude-eps-fonts --png $FILENAME