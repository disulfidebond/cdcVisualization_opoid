### Steps Taken

1) First, get the data.  

* This proved annoyingly difficult.  The data was available in various forms at [Wonder](https://wonder.cdc.gov), however if you just wanted the data, or more accurately the data used in the cdc Opoid charts, either I was missing something very obvious, or you were out of luck.

* But not to worry, this should do the trick:


       # run in Bash
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

2) To parse the files, I used python:


       #!/usr/bin/python

       l = []
       with open('testoutput.txt', 'r') as f:
       for i in f:
           i = i.rstrip('\r\n')
           s = i[4:]
           sList = s.split('<')
           l.append(sList[0])

       llen = len(l)
       ct = 2
       d = dict()
       while ct < llen:
           vIntLow = ct - 2
            vIntHigh = ct + 2
            k = l[ct]
            v = l[vIntLow:vIntHigh]
            d[k] = v
            ct += 4

       for k,v in d.items():
           o = ','.join(v)
            print(str(k) + ',' + str(o))
       
