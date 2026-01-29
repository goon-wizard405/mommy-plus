#!/bin/bash



CONF='normal'
LEVEL='0'

# usage : $0 level [conf]
if [ $# -gt 0 ]; then
	LEVEL=$1
fi
if [ $# -gt 1 ]; then
	CONF=$2
fi

cp ~/.config/mommy/$CONF.config.sh ~/.config/mommy/config.sh

aliases=(
	curl
	gcc
	cbmc
)
for i in "${aliases[@]}"; do
	unalias "$i" 2>/dev/null
done


if [ $LEVEL -eq 0 ]; then
	# no mommy
	if [[ -v PRE_MOMMY_PS1 ]]; then
		PS1=$PRE_MOMMY_PS1
	fi
	unset PRE_MOMMY_PS1
	if [ ! -z ${PRE_MOMMY_PROMPT_COMMAND+x} ]; then
		PROMPT_COMMAND=$PRE_MOMMY_PROMPT_COMMAND
	fi
	unset PRE_MOMMY_PROMPT_COMMAND
elif [ $LEVEL -eq 1 ]; then
	# set commands get upgraded
	if [[ ! -v PRE_MOMMY_PS1 ]]; then
		PRE_MOMMY_PS1=$PS1
		PS1="<3 $PS1"
	fi
	alias curl="mommy curl --fail-with-body"
	alias gcc="mommy gcc"
	alias cbmc="mommy cbmc"
	if [ ! -z ${PRE_MOMMY_PROMPT_COMMAND+x} ]; then
		PROMPT_COMMAND=$PRE_MOMMY_PROMPT_COMMAND
	fi
	unset PRE_MOMMY_PROMPT_COMMAND
elif [ $LEVEL -eq 2 ]; then
	# no compliments, but encouragement
	if [[ ! -v PRE_MOMMY_PS1 ]]; then
		PRE_MOMMY_PS1=$PS1
		PS1="<3 $PS1"
	fi
	echo 'MOMMY_COMPLIMENTS_ENABLED=0' >> ~/.config/mommy/config.sh
	if [ -z ${PRE_MOMMY_PROMPT_COMMAND+x} ]; then
		PRE_MOMMY_PROMPT_COMMAND=$PROMPT_COMMAND
		PROMPT_COMMAND="mommy -1 -s \$?; $PROMPT_COMMAND"
	fi
else
	# compliments and encouragement
	if [[ ! -v PRE_MOMMY_PS1 ]]; then
		PRE_MOMMY_PS1=$PS1
		PS1="<3 $PS1"
	fi
	if [ -z ${PRE_MOMMY_PROMPT_COMMAND+x} ]; then
		PRE_MOMMY_PROMPT_COMMAND=$PROMPT_COMMAND
		PROMPT_COMMAND="mommy -1 -s \$?; $PROMPT_COMMAND"
	fi
fi

