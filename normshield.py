import requests
import yaml
import os

inteltype = ['INTEL_DOMAIN']
path = os.environ["WORKDIR"]
with open(path + "/enrichment_plugins/normshield/dnifconfig.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

#have to register ip at https://services.normshield.com/service-register
#normshield_domain

def import_domain_intel():
    try:
        source = cfg['enrichment_plugin']['NORMSHIELD_DOMAIN_SOURCE']
        response = requests.get(source, stream=True)
    except Exception, e:
        print 'Api Request Error %s' % e
    try:
        lines = []
        for line in response.iter_lines():
            if not line.startswith("#"):
                tmp_dict = {}
                tmp_dict["EvtType"] = "DOMAIN"
                tmp_dict["EvtName"] = line.strip()
                tmp_dict2 = {}
                tmp_dict2["IntelRef"] = ["NORMSHIELD"]
                tmp_dict2["IntelRefURL"] = [source]
                tmp_dict2["ThreatType"] = ["blacklist"]
                tmp_dict["AddFields"] = tmp_dict2
                lines.append(tmp_dict)
    except:
        lines = []
    return lines, 'INTEL_DOMAIN'

