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
    b=${p%.py}
    if [ ! $b == ${b%datafiles} ]
    then
        continue
    fi
    if [ ! $b == ${b#test} ]
    then
        continue
    fi
    arg=algs4.`echo ${b} | tr / .`
    res=`pydoc3 -w $arg | grep -v '^wrote'`
    if [ ! -z "$res" ]
    then
        echo $arg $res
    fi
    
    #    pydoc3 -w algs4.`echo ${b} | tr / .` > /dev/null
done

cd ../..
#rsync -va  itu_dest/ ssh.itu.dk:public_html/
