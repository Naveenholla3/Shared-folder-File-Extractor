import os,re,PyPDF2,shutil

reg = re.compile(r'final[ ]*report',re.I)			#Final Report folder
#reg1 = re.compile(r'mobile[ ]*|^mobile$|checklist[ ]*|draft[ ]* report|scan[ ]* file|POC'',re.I)	#if u want retest folder (exclude mobile)
reg1 = re.compile(r'mobile[ ]*[-]+|^mobile$|retest[ ]*|checklist[ ]*|draft[ ]* report|scan[ ]* file|POC',re.I)	#mobile+retest folders exclude
#root='\\\cacfs1\\CAC Assessments\\Experian\\'
#root = 'C:\\Users\\naveenhn\\Desktop\\Assessments\\INTUIT\\DAST - S\\'
root = 'C:\\Users\\naveenhn\\Desktop\\Assessments\\'

fd = open('C:\\Users\\naveenhn\\Desktop\\Good Findings\\Experian\\good_findingss.txt','w')

#################################################### common vulnerabilities
vulns = ["Stored Cross-Site Scripting (XSS)","Reflected Cross-Site Scripting (XSS)","Formula Injection","Session Identifier Passed In Query String",
"Clickjacking (aka UI Redressing)","Cross-Site Request Forgery (CSRF)","Password Change Does Not Require Current Password","Weak Password Policy","HTTP TRACE Method Enabled",
"Server Path Disclosure Pattern Found","Password in HTTP Response","Secure Cookie Attribute Not Set","Apache MultiViews Attack",
"Autocomplete HTML Attribute Not Disabled for Sensitive Fields","Session Fixation","Vulnerable Server Version","TLSv1.0 Supported",
"Hidden Directory Detected","Verbose Server Banner","Directory Listing Enabled","HttpOnly Cookie Attribute Not Set","Overly Permissive CORS Allow Origin Policy",
"Missing Content-Security-Policy Header","Missing X-XSS-Protection Header","Inadequate Account Lockout Policy","Unmasked NPI Data","Vulnerable Third-Party Libraries in Use",
"Open URL Redirect","Unrestricted File Upload","No Account Lockout Policy","Open URL Redirect","Weak SSL/TLS Configuration","HTTPS Not Enforced","Password Reset Username Enumeration",
"Microsoft FrontPage Configuration Information Leakage","Cacheable HTTPS Content","The Application Treats GET and POST Requests Identically","Application Test Pages Discovered",
"Verbose Error Messages (with Stack Trace)","SSL/TLS Client-Initiated Renegotiation","Excessive Session Timeout Duration","Session Not Invalidated After Logout",
"Self-Signed X.509 Certificate (SSL/TLS)","HTTP Strict Transport Security (HSTS) Not Implemented","The Application Treats GET and POST Requests",
"Permanent Cookie Contains Sensitive Information","Missing X-Content-Type-Options Header","HTTPS Not Enabled","TRACE HTTP Method Enabled","Cacheable HTTP Content","Robots.txt File Web Site Structure Exposure",
"ASP.NET Debugging Enabled","Unencrypted Viewstate","Broadly Scoped Session Cookie Domain","Broadly Scoped Session Cookie Path","Vulnerable Software Version","Flash Parameter allowScriptAccess Set to Always",
"Verbose Error Messages","Login Page Username Enumeration","The Application Treats GET and POST Requests Identically","No Logout Functionality","Excessive Session Timeout Duration",
"X.509 Certificate with Wrong Hostname (SSL/TLS)","Clickjacking","TLS/SSL Client Initiated Renegotiation","Weak SSL Ciphers","Cacheable SSL Pages","SSL Certificate About to Expire",
"Query String Parameter in HTTPS Request","Session Identifier Set Prior To Authentication","X.509 Certificate About to Expire (SSL/TLS)","Application Error","/Software","Critical ",
"Cross Site Request Forgery (CSRF)","TLS/SSL Not Enforced","Query String Parameter in SSL Request","Username Enumeration through Password Reset","X.509 Certificate Expired (SSL/TLS)",
"Database Error Pattern Found","TLS/SSL Not Enabled","Missing X-XSS-Protection Headers","Missing X-Content-Type Options Header","Application","Infrastructure","Informational"]
####################################################
vuln1 = (" ".join(vulns)).upper()
for dname, subName, flist in os.walk(root,topdown=True):
	subName[:]=[d for d in subName if reg1.search(d)==None]
	print('path: '+dname)
#	print('flist'+str(flist))
	if reg.search(dname):
		for i in flist:
			if os.path.splitext(i)[1]=='.pdf':
				fpath = os.path.join(dname,i)
				print('pdf: '+fpath)

				fff=open(fpath,'rb')
				pdfReader = PyPDF2.PdfFileReader(fff)
					
				try:	
					pdfObject = pdfReader.getPage(8)
				except:
					print('problem in opening file')
					print('==========-----------------==================----------------------==================-----------------')
					break

				st = pdfObject.extractText()
					
				if 'Status' not in st:
					pdfObject = pdfReader.getPage(9)
					if 'Status' not in pdfObject.extractText():
						pdfObject = pdfReader.getPage(10)
					
				st = pdfObject.extractText()
					
				st1 = re.sub(r'[\n]*-[\n ]*','-',st)					# replacing \n-\n with -

				st2 = re.sub(r'(?<=[a-z])\n(?=[a-z])','',st1)			# replacing (sometext) \n (sometext) with nothing

				lst = re.findall(r'[a-zA-Z -/.0-9()]+(?=[\n ]+)',st2)		# finding all strings with a-zA-Z[space]-/.0-9
					
				try:
					c = lst.index('Status')
				except:
					print('no summary here')
					fd.write(fpath+'\n----------------------------------------------------------------------\n')
					shutil.copy(fpath,'C:\\Users\\naveenhn\\Desktop\\Good Findings\\Experian\\')	
					break
						
				try:
					d = lst.index('3.2')
				except:
					d = len(lst)
					
				f=0
				for i in range(c,d):
					j = lst[i]
					#print('1',end=' ')
					if len(j)>8 and j.upper() not in vuln1:
						fd.write(j+'\n')
							
						f=1
				if f==1:
					try:
						fd.write(fpath+'\n----------------------------------------------------------------------\n')
					except:
						fd.write('error in path write\n-------------------------------------------------------------------\n')
					shutil.copy(fpath,'C:\\Users\\naveenhn\\Desktop\\Good Findings\\Experian\\')	
				
				fff.close()		
fd.close()
