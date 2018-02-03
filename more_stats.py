#!/usr/bin/python
from scipy import stats

# import file
# import state list as dict

countOfRuralHighCounties = 0
countOfRuralCounties = 0
countOfUrbanCounties = 0
countOfUrbanHighCounties = 0
for k,v in d.items(): # separate by year
  line = v
   if line[5] == 'rural':
    countOfUrbanCounties += 1
    floatVal = float(line[4]) # add try...except to exclude null values
    if floatVal > 81.9:
      countOfUrbanHighCounties += 1
    else:
      continue
  else:
    countOfRuralCounties += 1
      floatVal = float(line[4])
      if floatVal > 81.9:
        countOfRuralHighCounties += 1
      else:
        continue
tTestList[0].append(countOfRuralHighCounties)
tTestList[1].append(countOfUrbanHighCounties)

res = stats.ttest_ind(ttestList[0],ttestList[1], equal_var=False)
