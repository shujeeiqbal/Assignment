#! /bin/bash

is_lower()
{
	echo "${1,,}"
}

is_root()
{
	if [ `whoami` = "root" ]; then
		return 0
	else
		return 1
	fi
}

is_user_exists()
{
	user=`cat /etc/passwd | grep $USER`
	if [ $user = " " ]; then
		return 1
	else
		return 0
	fi
}

read -p "Enter string: " input

is_lower $input

if is_root; then
	echo true
else
	echo false
fi

if is_user_exists; then
	echo true
else
	echo false
fi


