#!/bin/bash
this_folder=$(pwd)

mkdir -P treetagger
mkdir -P treetagger/models
wget http://www.cis.uni-muenchen.de/~schmid/tools/TreeTagger/data/tree-tagger-linux-3.2.tar.gz -P treetagger
wget http://www.cis.uni-muenchen.de/~schmid/tools/TreeTagger/data/install-tagger.sh treetagger -P treetagger
wget http://bfm.ens-lyon.fr/IMG/zip/fro.zip treetagger
cd treetagger 
chmod +x install-tagger.sh
./install-tagger.sh

cd ../
rm treetagger/*.gz
unzip fro.zip -d treetagger/models
rm fro.zip
echo "TREE_TAGGER_PATH=\"$this_folder/treetagger/bin/tree-tagger\"" >> flask_ttarethusa/constants.py
echo "TREE_TAGGER_MODEL=\"$this_folder/treetagger/models\"" >> flask_ttarethusa/constants.py