def printLol(aList, indent=False, level=0, filePath=sys.stdout):
	for item in aList:
		if isinstance(item,list):
			printLol(item, indent, level+1, filePath)
		else:
			if indent:
				for eachTabStop in range(level):
					print>>"\t",filePath
			print>>item,filePath