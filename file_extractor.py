import os,re,PyPDF2,shutil

reg = re.compile(r'final[ ]*report',re.I)			#Final Report folder
#reg1 = re.compile(r'mobile[ ]*|^mobile$|checklist[ ]*|draft[ ]* report|scan[ ]* file|POC'',re.I)	#if u want retest folder (exclude mobile)
reg1 = re.compile(r'mobile[ ]*[-]+|^mobile$|retest[ ]*|draft[ ]* report|scan[ ]* file|POC',re.I)	#mobile+retest folders exclude
root='\\\cacfs1\\CAC Assessments\\Deloitte\\2018\\'
#root = 'C:\\Users\\naveenhn\\Desktop\\Assessments\\INTUIT\\DAST - S\\'
#root = 'C:\\Users\\naveenhn\\Desktop\\Assessments\\'

fd = open('C:\\Users\\naveenhn\\Desktop\\Good Findings\\good_findingss.txt','w')

f1 = open('vulns.txt','r')
vuln1 = f1.read()
f1.close()

for dname, subName, flist in os.walk(root,topdown=True):
	subName[:]=[d for d in subName if reg1.search(d)==None]
	print('path: '+dname)
	if reg.search(dname):
		for i in flist:
			if os.path.splitext(i)[1]=='.pdf':
				fpath = os.path.join(dname,i)
				print('pdf: '+fpath)

				pdfFile=open(fpath,'rb')
				pdfReader = PyPDF2.PdfFileReader(pdfFile)
					
				try:	
					pdfObject = pdfReader.getPage(8)
					if 'Status' not in pdfObject.extractText():
						pdfObject = pdfReader.getPage(9)
						if 'Status' not in pdfObject.extractText():
							pdfObject = pdfReader.getPage(10)
				except:
					print('problem in opening file\n'+'-'*40+'\n')
					break				
					
				st1 = re.sub(r'[\n]*-[\n ]*','-',pdfObject.extractText())
				st1 = re.sub(r'(?<=[a-zA-Z] )\n','',st1)
				st1 = re.sub(r'(?<=[a-z])(\n[ ]+\n)+(?=[a-z])',' ',st1)
				st2 = re.sub(r'(?<=[a-zA-Z])\n(?=[a-zA-Z])','',st1)			
				lst = re.findall(r'[a-zA-Z -/.0-9()]+(?=[\n ]+)',st2)		
					
				try:
					c = lst.index('Status')
				except:
					print('no summary here')
					fd.write(fpath+'\n'+'-'*40+'\n')
					shutil.copy(fpath,'C:\\Users\\naveenhn\\Desktop\\Good Findings\\Deloitte1\\')	
					break
						
				try:
					d = lst.index('3.2')
				except:
					d = len(lst)
					
				f=0
				for i in range(c,d):
					j = lst[i]
					if len(j)>8 and j.upper() in vuln1:
						fd.write(j+'\n')	
						f=1
				if f==1:
					try:
						fd.write(fpath+'\n'+'-'*40+'\n')
					except:
						fd.write('error in path write\n'+'-'*40+'\n')
					shutil.copy(fpath,'C:\\Users\\naveenhn\\Desktop\\Good Findings\\Deloitte1\\')	
				
				pdfFile.close()		
fd.close()