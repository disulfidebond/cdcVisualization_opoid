#!/usr/bin/python


statesDict = dict()
with open('listOfStates.txt', 'r') as f:
	for i in f:
		i = i.rstrip('\r\n')
		iSplit = i.split(',')
		statesDict[iSplit[0]] = iSplit[1]

uList = []
uDict = dict()
with open('urbanList.txt.csv', 'r') as f1:
	for i in f1:
		i = i.rstrip('\r\n')
		iSplit = i.split(',')
		uDictKey = ','.join(iSplit[0:2])
		if uDictKey not in uDict:
			uDict[uDictKey] = 1
			uList.append(iSplit)
		else:
			continue
		

for itm in uList:
	convKey = itm[1]
	if convKey in statesDict:
		convValue = statesDict[convKey]
		itm[1] = (convValue,convKey)
	else:
		itm[1] = (convKey,convKey)

# 16079,Shoshone,ID,16079,94.1
lParse = []
with open('rxcounty2006.html.values.txt.parsed.txt', 'r') as f3:
	for i in f3:
		i = i.rstrip('\r\n')
		lParse.append(i)
pResult = []
for p in lParse:
	pCheck = p.split(',')
	pCheck.append('')
	pCheckVal = pCheck[1]
	pCheckMod = pCheckVal + ' County,' + pCheck[2]
	for pUrban in uList:
		pUrbanCheck = pUrban[0] + ',' + pUrban[1][0]
		if pCheckMod == pUrbanCheck:
			pCheck[-1] = 'urban'
	if not pCheck[-1]:
		pCheck[-1] = 'rural'
	pResult.append(pCheck)

for r in pResult:
	o = r[0] + ',' + r[1] + ',' + r[2] + ',' + r[3] + ',' + r[4] + ',' + r[5]
	print(o)