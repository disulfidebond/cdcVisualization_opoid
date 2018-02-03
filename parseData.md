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
    
4) Next, the data for the counties needed to be sorted and classified.

  * Since classifying rural and urban was outside the scope of this experiment, a simplified approach was employed.
  
  * A listing of the [500 largest cities](https://www.cdc.gov/500cities/pdf/500-cities-listed-by-state.pdf) in the US from the US Census bureau was used; this included all 50 states.  Counties were mapped as urban using this as a guide with the following criteria: 
    
    
    * Any county with a listed city was marked as urban
    
    * If a city spanned multiple counties, all were marked as urban.
    
    * If a city was independent, or had no county attached to it (example: Baltimore, MD and Washington, DC), then the city was included instead of the county, and was then attempted to be matched against the county listing as urban.
  
  * The cities were mapped back to the counties using [a few customized scripts](https://github.com/disulfidebond/cdcVisualization_opoid/blob/master/a_few_customized_scripts.txt) and a [python script](https://github.com/disulfidebond/cdcVisualization_opoid/blob/master/createParsedList.py), which created a list of rural and urban datapoints, and mapped the year back to the county.  If a county had no information for the prescription rate, it was scored with a "0".
    
  * This list was then used to plot urban versus rural, and contrast time across states.
  
    * For the first comparison, if the prescription rate for a county was > 82, it was scored a "1".  Then, a student's t-test was performed for rural vs. urban in a state to assess the difference of rural and urban settings in high opoid prescription rates.  The results are in table 1.
    
    * For the next comparison, the prescription rates of rural areas was plotted with respect to the time in years to visualize trends in how prescriptions for opoids increased or decreased with respect to time (see Figure 1).  This was repeated for urban areas (see Figure 2).  The correlation coefficients are shown.
    
4) Visualizing the prescription rates and other statistics will only show a portion of the problem, due to its inherent complexity.  For instance, the aforementioned calculations do not account for decreases or increases in income, economic fluctuations, and access to healthcare.  A better approach, therefore, would be to utiliza Machine Learning to more accurately study the problem at hand.

    * To begin, a Random Forest Classifier was trained using the rural and urban data, then assessed for its ability to accurately predict rural and urban counties from the existing data.
    
    * Next, additional data from the [Kaiser foundation](https://www.kff.org/other/state-indicator/total-population/?currentTimeframe=0&sortModel=%7B%22colId%22:%22Location%22,%22sort%22:%22asc%22%7D), which showed healthcare coverage in states, was added to the dataset, as was economic outlook data from the Bureau of Labor Statistics.
    
    
 
  
    
    
    
