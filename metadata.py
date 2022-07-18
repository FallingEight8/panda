#!/usr/bin/env python3

EventTypes = {
    1:'Malware',
    2:'PUPs (Potentially Unwanted Programs)',
    3:'Blocked Programs',
    4:'Exploits',
    5:'Blocked by Advanced Security',
    6:'Virus',
    7:'Spyware',
    8:'Hacking Tools and PUPs detected by Antivirus',
    9:'Phishing',
    10:'Suspicious',
    11:'Dangerous Actions',
    12:'Tracking Cookies',
    13:'Malware URLs',
    14:'Other security event by Antivirus',
    15:'Intrusion Attempts',
    16:'Blocked Connections',
    17:'Blocked Devices',
    18:'Indicators of Attack'
}

lookups={
'action':{
0:'Allowed',
1:'Moved Quarantine',
2:'Blocked',
3:'Killed',
4:'Ignored',
5:'Cleaned',
6:'Deleted',
7:'Restored',
8:'Allowed By Whitelist',
9:'Write Blocked',
10:'User Pending',
11:'Uninstalled',
13:'After Process Blocked',
14:'Immediately Blocked',
15:'Allowed By User',
16:'Detected Restart Pending',
17:'Allowed By Administrator',
18:'Allowed on GW Installer',
21:'Suspend Process',
1009:'Informed',
1010:'Unquarantine',
1011:'Rename',
1012:'Block URL'},

'attack':
{0:'Allowed',
1:'Moved Quarantine',
2:'Blocked',
3:'Killed',
4:'Ignored',
5:'Cleaned',
6:'Deleted',
7:'Restored',
8:'Allowed By Whitelist',
9:'Write Blocked',
10:'User Pending',
11:'Uninstalled',
13:'After Process Blocked',
14:'Immediately Blocked',
15:'Allowed By User',
16:'Detected Restart Pending',
17:'Allowed By Administrator',
18:'Allowed on GW Installer',
21:'Suspend Process',
1009:'Informed',
1010:'Unquarantine',
1011:'Rename',
1012:'Block URL'},

'event_type':
{0:'Malware',
1:'Exploit',
2:'PUPS',
3:'Blocked Item',
6:'Lock Plus Advanced Security',
7:'Lock Plus Application Control',
8:'Application Control'},

'protection_mode':
{0:'Undefined',
1:'Audit',
2:'Hardening',
3:'Lock'},

'reclassified_to_type':
{0:'Blocked',
1:'Malware',
3:'Pup',
6:'Goodware',
11:'Removed From List'},

'like_lihood_of_being_malicious':
{0:'Low',
1:'Medium',
2:'High',
3:'Very High'},

'discard_motive':
{0:'Unknown',
1:'Other Reason',
2:'File Max Size'},

'lock_plus_rule_id':
{1:'Obfuscated Params Powershell',
2:'User Executed Powershell',
4:'Unknown Scripts',
5:'Locally Built Programs',
6:'Documents With Macros',
7:'Windows Boot Registry',
101:'Forbidden Md5',
102:'Forbidden Program Name'},

'detected_by':
{1:'On Demand Scan',
2:'File Resident',
3:'Mail Resident',
4:'Firewall',
5:'Device Control',
6:'Exchange Mailbox',
7:'Exchange Transport',
8:'Exchange Antispam',
9:'Web Protection',
10:'Exchange Content',
11:'Minerva',
12:'Web Access Control',
13:'Anti-theft',
14:'Anti-tampering',
15:'Personal Information Tracking',
16:'Isolation',
17:'Data Search Control',
18:'Patch Management',
19:'Personal Information Inventory',
20:'Application Control',
21:'Encryption USB',
22:'Authorized Software'},

'device_type':
{0:'Undefined',
1:'Workstation',
2:'Laptop',
3:'Server',
4:'Mobile'},

'platform_id':
{0:'Undefined',
1:'Windows',
2:'Linux',
3:'Mac',
4:'Android',
5:'IOS'},

'malware_category':
{1:'Virus',
2:'Spyware',
3:'HackingPpnd',
4:'Phishing',
5:'Suspicious',
6:'Blocked Operations',
7:'Tracking Cookies',
8:'Malware URL',
9:'Others'},

'malware_type':
{21:'Nereus Heuritic',
22:'Beta Trace Heuritic',
23:'Smart Clean Heuritic',
24:'Cloud Heuritic',
25:'1N',
26:'Behavioral',
31:'Confirmed Goodware',
32:'Not Confirmed Goodware',
33:'Unwanted Goodware',
34:'Ranked',
35:'Digital Signature',
101:'Virus',
102:'Worm',
103:'Trojan',
104:'TrojanPwdeal',
105:'Dialer',
106:'Joke',
107:'Security Risk',
108:'Spyware',
109:'Adware',
110:'Worm Fake Worm',
111:'Tracking Cookie',
112:'Pup',
113:'Hacking Tool',
114:'Vulnerability',
115:'Max Size',
116:'Zip of Death',
117:'Packer of Death',
118:'Hoax',
119:'Phis Fraud',
120:'Rootkit',
121:'Backdoor',
122:'Virus Constructor',
123:'Malicious URL',
201:'Advertising',
202:'Toolbar',
203:'Net Tool',
204:'Advert Popup',
219:'Illegal',
223:'Internet Tools',
227:'Offensive',
236:'Society Education',
241:'Content Filter'},

'network_activity_type':
{1:'IcmpAttack',
2:'UdpPortScan',
3:'HeaderLengths',
4:'UdpFlood',
5:'TcpFlagsCheck',
6:'SmartWins',
7:'IpExplicitPath',
8:'LandAttack',
9:'SmartDns',
10:'IcmpFilterEchoRequest',
11:'OsDetection',
12:'SmartDhcp',
13:'SynFlood',
14:'SmartArp',
15:'TcpPortScan'},

'direction':
{1:'Incoming',
2:'Outgoing',
3:'Incoming and Outgoing',
4:'Internal'},

'protocol':
{1:'Tcp',
2:'Udp',
3:'TcpUdp',
4:'Icmp',
5:'IP',
6:'All'},

'type':
{0:'Undefined',
1:'Removable Storage',
2:'Image Capture',
3:'Optical Storage',
4:'Bluetooth',
5:'Modem',
6:'Mobile'},

'rule_risk':
{0:'Undefined',
1:'Critical',
2:'High',
3:'Medium',
4:'Low',
1000:'Unknown'},

'status':
{0:'Undefined',
1:'Pending',
2:'Filed'}}
