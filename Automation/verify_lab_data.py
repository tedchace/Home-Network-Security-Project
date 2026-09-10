from pathlib import Path
import xml.etree.ElementTree as ET
import importlib.util, csv, json, collections, hashlib
base=Path(__file__).resolve().parents[1]
out=base/'evidence/07-python/private/reproduced'; out.mkdir(parents=True,exist_ok=True)
spec=importlib.util.spec_from_file_location('submitted',base/'Automation/network_security_report.py')
mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
summary={}; assets={}
for label in ['main_pre','main_post','guest_post']:
 p=base/'evidence/04-nmap/private'/f'nmap_{label}_segmentation.xml'; root=ET.parse(p).getroot()
 hosts=root.findall('host'); states=collections.Counter(x.get('state') for h in hosts for x in h.findall('ports/port/state'))
 records=[]
 for h in hosts:
  ip=h.find("address[@addrtype='ipv4']"); mac=h.find("address[@addrtype='mac']"); hn=h.find('hostnames/hostname')
  records.append({'ip':ip.get('addr') if ip is not None else '', 'mac':mac.get('addr') if mac is not None else '', 'hostname':hn.get('name') if hn is not None else '', 'status':h.find('status').attrib, 'open':[(p.get('portid'),p.get('protocol'),p.find('service').get('name','') if p.find('service') is not None else '') for p in h.findall('ports/port') if p.find('state').get('state')=='open']})
 assets[label]=mod.parse_nmap_xml(p)
 assert [(a['ip_address'],[(s['port'],s['protocol'],s['service']) for s in a['open_services']]) for a in assets[label]]==[(r['ip'],r['open']) for r in records]
 keys=[a['mac_address'] or a['hostname'] or a['ip_address'] for a in assets[label]]
 assert len(keys)==len(set(keys)) and all(keys)
 mod.export_asset_inventory(assets[label],out/f'{label}.csv')
 summary[label]={'args':root.get('args'),'start':root.get('startstr'),'scaninfo':[x.attrib for x in root.findall('scaninfo')],'finished':root.find('runstats/finished').attrib,'runhosts':root.find('runstats/hosts').attrib,'hosts':len(hosts),'port_states':dict(states),'classified':sum(p[0] in {'21','23','445','3389','5800','5900'} for r in records for p in r['open']),'records':records}
 if label.startswith('main'):
  original=base/'evidence/07-python/private/original-reports'/f'asset_inventory_{label[5:]}_segmentation.csv'
  with original.open(newline='',encoding='utf-8-sig') as f, (out/f'{label}.csv').open(newline='',encoding='utf-8-sig') as g:
   assert list(csv.DictReader(f))==list(csv.DictReader(g)),label
comparison=mod.compare_network_states(assets['main_pre'],assets['main_post'])
mod.generate_security_report(assets['main_pre'],assets['main_post'],comparison,out/'security_report.md')
original=(base/'evidence/07-python/private/original-reports/security_report.md').read_text(encoding='utf-8-sig')
generated=(out/'security_report.md').read_text(encoding='utf-8-sig')
assert collections.Counter(original.splitlines())==collections.Counter(generated.splitlines()), 'Report content mismatch beyond ordering'
summary['checks']={'csv_records_match':True,'report_lines_match_ignoring_order':True,'script_matches_independent_xml_extraction':True,'identity_keys_unique':True}
(out/'verification.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
print('Verified CSV records, report line content, parser agreement and unique identity keys.')
