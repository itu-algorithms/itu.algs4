DIR=~/WorkSpace/bads-code/AlgorithmsInPython/algs4/
DEST=/home/rikj/WorkSpace/riko/html_templ_tum/itu_dest/AlgorithmsInPython

DIR=algs4
DEST=DOC
mkdir DOC

FILES=`cd $DIR; find . -type d -or -name \*.py`

cd $DEST

for f in $FILES
do
    p=${f#./}
#    echo $p
    pydoc3 -w algs4.`echo ${p%.py} | tr / .` 2>&1 | grep -v '^wrote'
done

cd ../..
#rsync -va  itu_dest/ ssh.itu.dk:public_html/
