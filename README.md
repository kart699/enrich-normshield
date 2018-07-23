## NormShield   
  https://services.normshield.com/domain/fraudulent/text/

### Overview
 NormShield provides comprehensive Security-as-a-Service solutions focused on cyber threat intelligence, vulnerability management.
 
 Note 
  NormShield.com Verified Phishing Domain List  (c) 2017 NormShield.com  some rights reserved. details http://creativecommons.org/licenses/by-nc-sa/4.0/
  use on your own risk. no warranties implied. this list contains verified phishing domains.
  you must not sell or re-distribute this domain list
#### NormShield Phishing Domain feeds
Following domains are verified and marked as phishing domains by NormShield.
These domains are checked with according to several items such as content, ssl, domain name registrar, domain age

### Using the NormShield feed API
 The NormShield feed API is found on github at
 
 https://github.com/dnif/enrich-normshield

#### Pre-requisite for normshield feed API
Have to register ip at https://services.normshield.com/service-register
  
Outbound access required to request normshield feed API

| Protocol   | Source IP  | Source Port  | Direction	 | Destination Domain | Destination Port  |  
|:------------- |:-------------|:-------------|:-------------|:-------------|:-------------|  
| TCP | AD,A10 | Any | Egress	| github.com | 443 |
| TCP | AD,A10 | Any | Egress	| services.normshield.com | 443 | 

#### Getting started with normshield feed API

1. #####    Login to your AD, A10 containers  
   ACCESS DNIF CONTAINER VIA SSH : [Click To Know How](https://dnif.it/docs/guides/tutorials/access-dnif-container-via-ssh.html)
2. #####    Move to the ‘/dnif/<Deployment-key/enrichment_plugins’ folder path.
```
$cd /dnif/CnxxxxxxxxxxxxV8/enrichment_plugins/
```
3. #####   Clone using the following command  
```  
git clone https://github.com/dnif/enrich-normshield.git normshield
```
### API feed output structure
  | Fields        | Description  |
| ------------- |:-------------:|
| EvtType      | A Domain |
| EvtName      | The IOC      |
| IntelRef | Feed Name      |
| IntelRefURL | Feed URL      |
| ThreatType | DNIF Feed Identification Name |      

An example of API feed output
```
{'EvtType': 'DOMAIN',
'EvtName': 'kredikartisorgulamasistemi.com',
'AddFields': {
'IntelRef': ['NORMSHIELD'],
'IntelRefURL': ['https://services.normshield.com/domain/fraudulent/text/'],
'ThreatType': ['blacklist'] }}
```
