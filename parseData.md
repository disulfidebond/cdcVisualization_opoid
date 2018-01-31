### Steps Taken

1) First, get the data.  

* This proved annoyingly difficult.  The data was available in various forms at [Wonder](https://wonder.cdc.gov), however if you just wanted the data, or more accurately the data used in the cdc Opoid charts, either I was missing something very obvious, or you were out of luck.

* But not to worry, this should do the trick:


       # run in Bash
       # Be warned that GNU bash may not corretly pull the files, I was unable to fully figure out why.  
       # BSD bash did not have this problem
       for i in {6..16} ; do
         if ((i>9)) ; then
           CSTRING=$(echo "https://www.cdc.gov/drugoverdose/maps/rxcounty200${i}.html") ;
           PARSENAME=$(echo ${CSTRING} | rev | cut -d/ -f1 | rev) ; curl -O ${CSTRING} ;
           perl -ne 'next unless /<td>/; print' ${PARSENAME} > ${PARSENAME}.values.txt ;
         else:
           CSTRING=$(echo "https://www.cdc.gov/drugoverdose/maps/rxcounty20${i}.html") ; 
           PARSENAME=$(echo ${CSTRING} | rev | cut -d/ -f1 | rev) ; curl -O ${CSTRING} ; 
           perl -ne 'next unless /<td>/; print' ${PARSENAME} > ${PARSENAME}.values.txt ;
         fi
       let RANDVAL=$RANDOM%4 ; 
       sleep $RANDVAL ; 
       done

2) To clean and parse the files, I used python:

       try:
	    type(sys.argv[1])
       except IndexError:
	    print('Error, please add an input File')
	    sys.exit()
       if len(sys.argv) > 2:
           print('Warning, only one can be used.  Proceeding with the first listed file: ')
	    print(str(sys.argv[1]))
           
       inputFile = sys.argv[1]
       l = []
       with open(inputFile, 'r') as f:
       for i in f:
           i = i.rstrip('\r\n')
           s = i[4:]
           sList = s.split('<')
           l.append(sList[0])
       llen = len(l)
       for itm in l:
           print(itm)
 

  [A better and more robust example is here](https://github.com/disulfidebond/cdcVisualization_opoid/blob/master/cleanCDCdata.py).

3) Before going any further, we needed to establish the variables, the contrasts for the variables, and the experimental hypotheses:

    * y<sub>1</sub> = # of opoid prescriptions in rural areas
    
    * y<sub>2</sub> = # of opoid prescriptions in urban areas
    
    * x = time
    
    * H<sub>0</sub> : there is no difference in the number of opoid prescriptions in rural and urban areas    
    
    * H<sub>A</sub> : there is a difference in the number of opoid prescriptions in rural and urban areas
    

    
    
    
