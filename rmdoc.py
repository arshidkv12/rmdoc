import re
import os 
import sys



def php_rmdoc(file_name):
	doc_command = 0
	fp = open(file_name+'_tmp0_0tmp_', "w")
	print file_name
	for line in open(file_name) :
		
		if line.find('//') != -1:
			line = line.rsplit('//')[0];

		line = re.sub(r"/\*(.+?)\*/","",line )
		
		if line.find('/*') != -1:
			doc_command = 1 

		if doc_command == 1 and line.find('*/') != -1:
			doc_command = 0
			continue

		if doc_command == 1:
			continue

		fp.write(line)
	fp.close()
	

print "Enter php script path:"
folder_name = raw_input()
print "folder :"+folder_name+"\nAre you sure? Y/n:"
flag = raw_input()

if flag == 'y' or flag == 'Y' or flag == 'yes' :
	 
	for root, dirs, files in os.walk(folder_name):
		for file in files:
			if file.find('_tmp0_0tmp_') == -1:
				path_file = os.path.join(root, file)
				php_rmdoc(path_file)
				print path_file

	for root, dirs, files in os.walk(folder_name):
		for file in files:
			path_file = os.path.join(root, file)
			if not path_file.find('_tmp0_0tmp_') != -1:
				os.remove(path_file)
				print 'delete :'+path_file
			else:
				print 'rename :'+path_file
				os.rename(path_file,path_file.replace('_tmp0_0tmp_',''))

	print " === Completed === "
	
else:
	sys.exit()
			

 
