import os,re

reg = re.compile(r'e[ -_]*benefit',re.I)
reg1 = re.compile(r'checklist[ ]*|draft[ ]* report|scan[ ]* file|POC',re.I)	#mobile+retest folders exclude
root='\\\cacfs1\\CAC Assessments\\AIA\\'
fd = open('C:\\Users\\naveenhn\\Desktop\\Good Findings\\ebenefit.txt','w')

for dname, subName, flist in os.walk(root,topdown=True):
	f=0
	for d in subName:
		if reg1.search(d)!=None:
			f=1
	if f==1:
		subName[:]=[]
	print('path: '+dname)
	if reg.search(dname):
		subName[:]=[]
		fd.write(dname+'\n')		
fd.close()