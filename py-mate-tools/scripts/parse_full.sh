#!/bin/sh

## There are three sets of options that need, may need to, and could be changed.
## (1) deals with input and output. You have to set these (in particular, you need to provide models)
## (2) deals with the jvm parameters and may need to be changed
## (3) deals with the behaviour of the system

## For further information on switches, see the source code, or run
## java -cp srl.jar se.lth.cs.srl.Parse --help

##################################################
## (1) The following needs to be set appropriately
##################################################
#INPUT="/home/anders/corpora/conll09/eng/CoNLL2009-evaluation-English-SRLonly.txt" #evaluation corpus
INPUT=/home/anders/corpora/conll09/chi/CoNLL2009-ST-evaluation-Chinese-SRLonly.txt
LANG="chi"
##TOKENIZER_MODEL="models/eng/EnglishTok.bin.gz" #This is not used here anyway. The input is assumed to be segmented/tokenized already. 
##LEMMATIZER_MODEL="models/chi/lemma-eng.model"
POS_MODEL="models/chi/tag-chn.model"
#MORPH_MODEL="models/ger/morph-ger.model" #Morphological tagger is not applicable to English. Fix the path and uncomment if you are running german.
PARSER_MODEL="models/chi/prs-chn.model"
SRL_MODEL="models/chi/srl-chn.model"
OUTPUT="$LANG.out"

##################################################
## (2) These ones may need to be changed
##################################################
JAVA="java" #Edit this i you want to use a specific JRE.
MEM="4g" #Memory for the JVM, might need to be increased for large corpora.
CP="srl.jar:lib/anna.jar:lib/liblinear-1.51-with-deps.jar:lib/opennlp-tools-1.4.3.jar:lib/maxent-2.5.2.jar:lib/trove.jar:lib/seg.jar"
JVM_ARGS="-cp $CP -Xmx$MEM"

##################################################
## (3) The following changes the behaviour of the system
##################################################
#RERANKER="-reranker" #Uncomment this if you want to use a reranker too. The model is assumed to contain a reranker. While training, the corresponding parameter has to be provided.
#NOPI="-nopi" #Uncomment this if you want to skip the predicate identification step.



##################################################

CMD="$JAVA $JVM_ARGS se.lth.cs.srl.CompletePipeline $LANG $NOPI $RERANKER -tagger $POS_MODEL -parser $PARSER_MODEL -srl $SRL_MODEL -test $INPUT -out $OUTPUT"

if [ "$TOKENIZER_MODEL" != "" ]; then
  CMD="$CMD -token $TOKENIZER_MODEL"
fi

if [ "$LEMMATIZER_MODEL" != "" ]; then
  CMD="$CMD -lemma $LEMMATIZER_MODEL"
fi

if [ "$MORPH_MODEL" != "" ]; then
  CMD="$CMD -morph $MORPH_MODEL"
fi

echo "Executing: $CMD"

$CMD
