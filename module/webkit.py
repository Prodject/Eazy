##
## webkit modules
##
## written by @ciku370
##

webkit_dict = {'traceroute':'mtr',
'nping':'nping',
'dns_lookup':'dnslookup',
'reverse_dns':'reversedns',
'host_search':'hostsearch',
'shared_dns':'findshareddns',
'zone_test':'zonetransfer',
'whois':'whois',
'reverse_ip':'reverseiplookup',
'port':'nmap',
'subnet':'subnetcalc',
'http_headers':'httpheaders',
'pagelinks':'pagelinks'}

import requests
import json
from re        import search
from urllib2   import (
     urlopen,
     URLError
)
from core.misc import printf

def hackertarget(i,t):
    printf(requests.get('https://api.hackertarget.com/'+i+'/?q='+t).text)

def mx(t):
    r = requests.get('https://dns-api.org/MX/' + t)
    a = json.loads(r.text)
    printf(' domain name for MX records')
    for i in a:
        printf(' %s'%str(i['value']))
def domage(t):
    r = requests.get('https://input.payapi.io/v1/api/fraud/domain/age/' + t)
    a = json.loads(r.text)
    try:
        printf(' %s'%a['message'])
    except KeyError:
        printf('[!] incorrect Input')
def cms(t):
    r = requests.get('https://whatcms.org/APIEndpoint?key=745aaac9fc2d1acc0e20330469b1db3979be347b5542b3b5b790b42d10cb68cac78c2f&url=' + t)
    a = json.loads(r.text)
    if a['result']['msg'] == 'Success':
       for i in a['result']:
          printf(' %s: %s'%(str(i),str(a['result'][i])))
    else:
       printf('[!] %s'%str(a['result']['msg']))
def subdo(t):
    subdomains = []
    req = requests.get("https://crt.sh/?q=%.{d}&output=json".format(d=t))
    if req.status_code == 200 and req.text != '':
        json_data = json.loads('[{}]'.format(req.text.replace('}{', '},{')))
        for (key,value) in enumerate(json_data):
                subdomains.append(value['name_value'])
        sub = sorted(set(subdomains))
        for subdomain in sub:
                printf(' %s'%subdomain)
    else:
        printf("[!] Information not available!")
def honey(ip):
    honey = "https://api.shodan.io/labs/honeyscore/" + ip + "?key=C23OXE0bVMrul2YeqcL7zxb6jZ4pj2by"
    try:
        phoney = urlopen(honey).read().decode('utf-8')
    except URLError:
        phoney = None
        printf('[!] No information available for that IP!')
    if phoney:
        print('[+] Honeypot Probabilty: {probability}'.format(probability=float(phoney) * 10))
def geoip(web):
    r = requests.get('https://tools.keycdn.com/geo.json?host=' + web)
    a = json.loads(r.text)
    for i in a['data']['geo']:
        printf(' %s: %s'%(str(i).replace('_',' '),str(a['data']['geo'][i])))
