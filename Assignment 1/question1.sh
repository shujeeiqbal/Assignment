for file in `ls`
do

	if [ -f $file ]
	then
		extension=` echo $file | cut -d'.' -f2`
		
		if [ -d $extension ]
		then
		
			mv $file $extension
		
		else
		
			mkdir $extension
			mv $file $extension
		fi	
	fi
	
done
