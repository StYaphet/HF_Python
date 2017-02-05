# try: 
#	你写的代码（这段代码有可能会出现错误）
# except:
# 	错误处理代码
        
#########################################################
# version 1
#
# data = open("sketch.txt")
# for each_line in data:
# 	(role, line_spoken) = each_line.split(":",1)
# 	print(role,)
# 	print(" said: ",)
# 	print(line_spoken, )

#########################################################
# version 2

# import os

# if os.path.exists("sketch.txt"):

# 	data = open("sketch.txt")

# 	for each_line in data:
# 		try:
# 			(role, line_spoken) = each_line.split(":",1)
# 			print(role,)
# 			print(" said: ",)
# 			print(line_spoken)
# 		except:
# 			pass
# 	data.close()
# else:
# 	print("The data file is missing")

#########################################################
# version 3

# open() BIF 默认使用的是 r 模式，要打开一个文件完成写，要使用 w 模式（文件已经存在的话就会清除掉之前的内容）
# 如果想要在文件后边追加内容，要使用 a 模式，如果要打开一个文件完成读和写（不清处），需要使用 w+ 
# 如果想打开一个文件完成写，但是这个文件不存在，那么就会先创建这个文件，然后再打开文件完成写
# 完成工作之后，一定要关闭文件，确保所有数据都写至磁盘，这被成文刷新输出

# man = []
# other = []
# try:
# 	data = open("sketch.txt")
# 	for each_line in data:
# 		try:
# 			(role, line_spoken) = each_line.split(":",1)
# 			line_spoken = line_spoken.strip()
# 			if role == "Man":
# 				man.append(line_spoken)
# 			else:
# 				other.append(line_spoken)
# 		except ValueError:
# 			pass
# 	data.close()
# except IOError:
# 	print("The datafile is missing!")
# print(man)
# print(other)	

#########################################################
# version 4

man = []
other = []
try:
	data = open("sketch.txt")
	for each_line in data:
		try:
			(role, line_spoken) = each_line.split(":",1)
			line_spoken = line_spoken.strip()
			if role == "Man":
				man.append(line_spoken)
			else:
				other.append(line_spoken)
		except ValueError:
			pass
	data.close()
except IOError:
	print("The datafile is missing!")

try:
	man_file = open("man_data.txt","w")
	other_file = open("other_data.txt","w")

	# print(man, file = man_file)
	# print(other, file = other_file)
	print>>man_file,man
	print>>other_file,other
	# man_file.write(man)
	# other_file.write(other)

	man_file.close()
	other_file.close()
except IOError:
	print("file error",)















