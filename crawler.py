#-*- coding: UTF-8 -*- 
import urllib2  
import re  

def GetInfo(name):  
   
   
   headers = {  
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'  
     }  
   req = urllib2.Request(  
    url='http://blog.csdn.net/'+name,  
    headers = headers  
    )  
  
   content = urllib2.urlopen(req).read()  
   result = re.findall(r'(?<=<li>).+?(?=</li>)',content)  
   str_result=[]
   for x in xrange(0,7):  
       str_result.append(filter(str.isdigit,result[x]))  
        
   return str_result

 
print GetInfo('gshengod')
