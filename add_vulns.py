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

#"Cross-Site WebSocket Hijacking"]
####################################################
fd = open('vulns.txt','w')
fd.write(" ".join(vulns).upper())
fd.close()



'''
"Stored Cross-Site Scripting (XSS)","Reflected Cross-Site Scripting (XSS)","Formula Injection","Session Identifier Passed In Query String",
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
"Database Error Pattern Found","TLS/SSL Not Enabled","Missing X-XSS-Protection Headers","Missing X-Content-Type Options Header","Application","Infrastructure","Informational"
'''