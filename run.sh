#!/bin/bash

NUM_TEST_FILES=10
RED=`tput setaf 1`
GREEN=`tput setaf 2`
RESET=`tput sgr 0`

for (( x=1; x <= $NUM_TEST_FILES; x++ ))
  do
    echo "Running with $x.mini..."
    python3 src/Compiler.py $x.mini
    if (($? == 0))
      then
      	echo "${GREEN} SUCESS.${RESET}"
      else
	echo "${RED} FAILED${RESET}"
    fi
done

echo "Running ret.mini WITH ERRORS..."
python3 src/Compiler.py ret-error.mini
if (($? == 0))
  then
    echo "${GREEN} SUCESS.${RESET}"
  else
    echo "${RED} FAILED${RESET}"
fi

echo "Running ret.mini WITHOUT ERRORS..."
python3 src/Compiler.py ret.mini
if (($? == 0))
  then
    echo "${GREEN} SUCESS.${RESET}"
  else
    echo "${RED} FAILED${RESET}"
fi
