#!/usr/bin/python
import argparse
import sys

def main():
	parser = argparse.ArgumentParser(description='Parse Downloaded text File')
	parser.add_argument('-i', '--inputFile', help='input file to be parsed into output file')
	args = parser.parse_args()

	if not args.inputFile:
		print('You must provide a file name')
		sys.exit()
	inputFile = args.inputFile
	l = []

	with open(inputFile, 'r') as f:
		for i in f:
			i = i.rstrip('\r\n')
			s = i[4:]
			sList = s.split('<')
			l.append(sList[0])

	llen = len(l)
	ct = 1 # for cty use 2
	d = dict()
	while ct < llen:
		vIntLow = ct - 1 # for cty use -2
		vIntHigh = ct + 2
		k = l[ct]
		v = l[vIntLow:vIntHigh]
		# uncomment the following lines for cty		
		# tmp = v[0]
		# tmpSplit = tmp.split(',')
		# v[0] = tmpSplit[0]
		d[k] = v
		ct += 3 # for cty use 4

	for k,v in d.items():
		o = ','.join(v)
		print(str(k) + ',' + str(o))


if __name__ == "__main__":
	main()


if __name__ == "__main__":
	main()
