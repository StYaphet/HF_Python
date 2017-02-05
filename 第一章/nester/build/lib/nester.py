def printLol(aList, indent=False, level=0):
	for item in aList:
		if isinstance(item,list):
			printLol(item, indent, level+1)
		else:
			if indent:
				for eachTabStop in range(level):
					print("\t")
			print(item)