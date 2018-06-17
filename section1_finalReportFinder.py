
import os,re,PyPDF2,shutil

reg = re.compile(r'^[ ]*final[ ]*report[s ]*$',re.I)
reg2 = re.compile(r'final[ ]*report[s]?',re.I)
miscReg = re.compile(r'draft[ ]* report|scan[ ]*file[s]*|^POC[s]?$|^misc$|^checklist[s]?$|^[ ]*final[ ]*report[s ]*$',re.I)
mobileReg = re.compile(r'^[ ]*mobile[ ]*[-]+|^mobile$|^retest[ ]*|^retest[s]?$|^draft[ ]*report[s]*|scan[ ]* file|^POC[s]?$|^misc$|^checklist[s]?$',re.I)	#and retest
regg1 = re.compile(r'[\n]*-[\n ]*')
regg2 = re.compile(r'(?<=[a-zA-Z] )\n')
regg3 = re.compile(r'(?<=[a-z])(\n[ ]+\n)+(?=[a-z/\-])')
regg4 = re.compile(r'(?<=[a-zA-Z])\n(?=[a-zA-Z])')
regg5 = re.compile(r'[a-zA-Z -/.0-9()]+(?=[\n ]+)')

root='\\\cacfs1\\CAC Assessments\\'
count=0

fc = open('vulns.txt','r')
vuln1 = fc.read()
fc.close()

'''
vuln1 = input("Enter name of finding(full name or part of it):").strip()
vuln1 = vuln1.upper()
while(vuln1==''):
	print('please enter finding name')
	vuln1 = input("Enter name of finding(full name or part of it):").strip()
'''

client=input('enter client name (Leave blank to search whole cac assessments folder):').strip()
lis = os.listdir(root)
clientString = ' $$'.join(lis)

f=0
while client!='':
	searchClient = '\$\$'+client.upper()
	if re.search(searchClient,clientString.upper())==None:
		print('\t'.join(lis))
		client = input('enter client name (take reference from above):')
	else:
		f=1
		break
else:
	print('Searching entire CAC')

if f==1:
	for l in lis:
		if re.match(client,l,re.I)!=None:
			print('searching for client "'+l+'"')
			root = os.path.join(root,l)
			break
			
year = input("Enter year (leave blank to search every year):").strip()
if re.match(r'201[5678]',year)!=None:
	print('searching for Year:'+year)
else:
	if year!='':
		print('year - '+str(year)+' not present instead..',end=' ')
	year=''
	print('searching for every year...')


fd = open('C:\\Users\\naveenhn\\Desktop\\Good Findings\\Test\\good_findingss.txt','w')
print(root)

for dname, subName, flist in os.walk(root,topdown=True):
	if len(dname.split(os.sep))>10:
		subName[:]=[]
	dirList = [d for d in subName if miscReg.search(d)!=None]
	#print('dirlist'+str(dirList))
	aa=[d for d in dirList if reg.search(d)!=None]
	if len(dirList)>2 and len(aa)!=0:
		subName[:] = aa
	if year!='':
		for ii in subName:	
			if re.match(year+'$',ii)!=None:
				subName[:] = [ii]
	
	subName[:]=[d for d in subName if mobileReg.search(d)==None]
	print('path:'+dname)
	if reg2.search(dname) and year in dname.split(os.sep):
		for i in flist:
			if os.path.splitext(i)[1]=='.pdf':
				fpath = os.path.join(dname,i)
				print('pdf: '+fpath)

				pdfFile=open(fpath,'rb')
				pdfReader = PyPDF2.PdfFileReader(pdfFile)
					
				try:
					pdfObject = pdfReader.getPage(7)
					if 'Status' not in pdfObject.extractText():
						pdfObject = pdfReader.getPage(8)
						if 'Status' not in pdfObject.extractText():
							pdfObject = pdfReader.getPage(9)
							if 'Status' not in pdfObject.extractText():
								pdfObject = pdfReader.getPage(10)
				except:
					#print('problem in opening file\n'+'-'*40+'\n')
					break				
					
				st1 = regg1.sub('-',pdfObject.extractText())
				st1 = regg2.sub('',st1)
				st1 = regg3.sub(' ',st1)
				st2 = regg4.sub('',st1)			
				lst = regg5.findall(st2)		
					
				try:
					c = lst.index('Status')
				except:
					print('no summary here')	
					break
						
				try:
					d = lst.index('3.2')
				except:
					d = len(lst)
					
				f=0
				for i in range(c,d):
					j = lst[i]
					if len(j)>8 and j.upper() not in vuln1: #vuln1 in j.upper():
						fd.write(j+'\n')	
						f=1
				if f==1:
					try:
						fd.write(fpath+'\n'+'-'*40+'\n')
					except:
						fd.write('error in path write\n'+'-'*40+'\n')
					shutil.copy(fpath,'C:\\Users\\naveenhn\\Desktop\\Good Findings\\Test\\')	
					count+=1
					
				pdfFile.close()	
fd.write('\n'+str(count))
print('total:'+str(count))				
fd.close()			
