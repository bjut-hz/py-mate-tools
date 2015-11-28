#!/bin/sh

## There are three sets of options that need, may need to, and could be changed.
## (1) deals with input and output. You have to set these (in particular, you need to provide models)
## (2) deals with the jvm parameters and may need to be changed
## (3) deals with the behaviour of the system

##################################################
## (1) The following needs to be set appropriately
##################################################
Lang="eng"
MODELDIR=`dirname $0`/../../models/eng/
#TOKENIZER_MODEL=${MODELDIR}/en-token.bin #If tokenizer is blank, it will use some default (Stanford for English, Exner for Swedish, and whitespace otherwise)
#TOKENIZER_MODEL="models/chi/stanford-chinese-segmenter-2008-05-21/data"  #Use this for chinese.
LEMMATIZER_MODEL=${MODELDIR}/CoNLL2009-ST-English-ALL.anna-3.3.lemmatizer.model
POS_MODEL=${MODELDIR}/CoNLL2009-ST-English-ALL.anna-3.3.postagger.model
#MORPH_MODEL=${MODELDIR}/  #No morph model for English.
PARSER_MODEL=${MODELDIR}/CoNLL2009-ST-English-ALL.anna-3.3.parser.model

PORT=8073 #The port to listen on

##################################################
## (2) These ones may need to be changed
##################################################
JAVA="java" #Edit this i you want to use a specific java binary.
MEM="4g" #Memory for the JVM, might need to be increased for large corpora.
DIST_ROOT=`dirname $0`/..
CP=${DIST_ROOT}/srl.jar
for jar in ${DIST_ROOT}/lib/*.jar; do
#    echo $jar
    CP=${CP}:$jar
done
#exit 0;
JVM_ARGS="-Djava.awt.headless=true -cp $CP -Xmx$MEM"
# The java.awt.headless property is needed to render the images of dependency graphs if the server is executed remotely (and there is no GUI stuff involved anyway)

##################################################
## (3) The following changes the behaviour of the system
##################################################
#RERANKER="-reranker" #Uncomment this if you want to use a reranker too. The model is assumed to contain a reranker. While training, the corresponding parameter has to be provided.

CMD="$JAVA $JVM_ARGS se.lth.cs.srl.http.AnnaHttpPipeline $Lang $RERANKER -tagger $POS_MODEL -parser $PARSER_MODEL -port $PORT"

if [ "$TOKENIZER_MODEL" != "" ]; then
    CMD=${CMD}" -token $TOKENIZER_MODEL"
fi

if [ "$LEMMATIZER_MODEL" != "" ]; then
  CMD="$CMD -lemma $LEMMATIZER_MODEL"
fi

if [ "$MORPH_MODEL" != "" ]; then
  CMD="$CMD -morph $MORPH_MODEL"
fi

echo "Executing: $CMD"
$CMD
