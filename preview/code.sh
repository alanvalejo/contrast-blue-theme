#!/bin/bash

datasets=(sensors think-aloud psychologists face logic face-logic face-think-alound logic-think-alound)

## Now loop through the above datasets
for dataset in "${datasets[@]}"
do
	## Execute knn
	for knn in {1..29}
	do
		python knn.py --filenam=${dataset}.dat --output=${dataset}.out -k ${knn}
	done
done
