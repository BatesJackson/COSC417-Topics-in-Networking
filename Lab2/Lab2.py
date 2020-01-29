# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 08:19:07 2020

@author: bates
"""

ipList = open("iplist.txt", "r")
"""
for ip in ipList:
    print(ip)
"""

import os
import re
import ipwhois

for ip in ipList:
    writeFile = open("asnoutput.txt", "a")
    writeFile.write("\n---------------------------------------------------------\n")
    #writeFile.write("Target IP: " + ip)
    #print('starting: ', ip)
    myData = os.popen('tracert ' + ip).read()
    print(myData)
    route = re.findall('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', myData)[1:]
    print(route)
    for i in route:
        #print(i)      
        try:
            myIp = ipwhois.net.Net(i)
            myObj = ipwhois.asn.IPASN(myIp)
            results = myObj.lookup()
            print(results)
            
            outputData = [i, results['asn'], results['asn_description']]
            writeFile.write(str(outputData) + "\n")
        except:
            print("Non-Lookupable IP address.")
    writeFile.close()
    
        
    
    

    
    