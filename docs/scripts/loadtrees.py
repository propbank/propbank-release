import json, codecs, os, logging
import skeleton2conll
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('setup')
33

j =json.load(codecs.open("localtreepaths.json",'r','utf-8'))

localpaths = {}
localpaths['ontonotes'] = os.path.abspath('../../data/ontonotes/')
localpaths['ewt'] = os.path.abspath("../../data/google/ewt/")
localpaths['questionbank'] = os.path.abspath("../../data/google/questionbank/")

metadata = {'ontonotes':'data/files/data/english/annotations/', "ewt":"data/", "questionbank":'data/'}
modifications = {'ontonotes':[], "ewt":[("/00",'/penntree')], "questionbank":[('questionbank/00','')]}	
filemoddict = {"questionbank":[('QB-revised','QB-revised.v1')]}
flagdict = {"questionbank":["--topless"],"ewt":["--topless"], "ontonotes":[]}


localpaths['bolt-cts-3'], localpaths['bolt-cts-2'], localpaths['bolt-cts-1'] = os.path.abspath("../../data/bolt/CTS/CTS/03"), os.path.abspath("../../data/bolt/CTS/CTS/02"), os.path.abspath("../../data/bolt/CTS/CTS/01")
modifications["bolt-cts-3"], modifications["bolt-cts-2"], modifications["bolt-cts-1"] = [("CTS/CTS/03","")], [("CTS/CTS/02","")], [("CTS/CTS/01","")]
metadata['bolt-cts-3'],metadata['bolt-cts-2'],metadata['bolt-cts-1'] = ['/data/translation-alternates-included/penntree/','/data/translation-alternates-included/penntree/','/data/translation-alternates-included/penntree/']
flagdict['bolt-cts-3'],flagdict['bolt-cts-2'],flagdict['bolt-cts-1'] = ['--topless'], ['--topless'],['--topless']

localpaths['bolt-sms-4'], localpaths['bolt-sms-3'], localpaths['bolt-sms-2'], localpaths['bolt-sms-1'] = os.path.abspath("../../data/bolt/SMS/SMS/04"),os.path.abspath("../../data/bolt/SMS/SMS/03"), os.path.abspath("../../data/bolt/SMS/SMS/02"), os.path.abspath("../../data/bolt/SMS/SMS/01")
modifications["bolt-sms-4"], modifications["bolt-sms-3"], modifications["bolt-sms-2"], modifications["bolt-sms-1"] = [("SMS/SMS/04","")], [("SMS/SMS/03","")], [("SMS/SMS/02","")], [("SMS/SMS/01","")]
metadata['bolt-sms-4'], metadata['bolt-sms-3'], metadata['bolt-sms-2'], metadata['bolt-sms-1'] = ['/data/translation-alternates-included/penntree/','/data/translation-alternates-included/penntree/','/data/penntree/','/data/penntree/']
flagdict['bolt-sms-4'],flagdict['bolt-sms-3'],flagdict['bolt-sms-2'],flagdict['bolt-sms-1'] = ['--topless'], ['--topless'],['--topless'],['--topless']

#### I can't figure out where LDC released the SMS part 5 treebank package, but you can get the data from the source folder in BOLT propbank SMS 5
localpaths['bolt-sms-5'], modifications['bolt-sms-5'], metadata['bolt-sms-5'], flagdict['bolt-sms-5'] = os.path.abspath("../../data/bolt/SMS/SMS/05"), [("SMS/SMS/05","")], '/data/source/', ['--topless']

localpaths['bolt-df-7'], localpaths['bolt-df-6'], localpaths['bolt-df-5'], localpaths['bolt-df-4'], localpaths['bolt-df-3'], localpaths['bolt-df-2'], localpaths['bolt-df-1'] = os.path.abspath("../../data/bolt/DF/DF/07"),os.path.abspath("../../data/bolt/DF/DF/06"),os.path.abspath("../../data/bolt/DF/DF/05"),os.path.abspath("../../data/bolt/DF/DF/04"),os.path.abspath("../../data/bolt/DF/DF/03"), os.path.abspath("../../data/bolt/DF/DF/02"), os.path.abspath("../../data/bolt/DF/DF/01")
modifications["bolt-df-7"], modifications["bolt-df-6"], modifications["bolt-df-5"],modifications["bolt-df-4"], modifications["bolt-df-3"], modifications["bolt-df-2"], modifications["bolt-df-1"] = [("DF/DF/07","")], [("DF/DF/06","")], [("DF/DF/05","")],[("DF/DF/04","")], [("DF/DF/03","")], [("DF/DF/02","")], [("DF/DF/01","")]
metadata['bolt-df-7'], metadata['bolt-df-6'], metadata['bolt-df-5'], metadata['bolt-df-4'], metadata['bolt-df-3'], metadata['bolt-df-2'], metadata['bolt-df-1'] = ['/data/translation-alternates-removed/penntree/','/data/translation-alternates-included/penntree/','/data/penntree/','/data/penntree/','/data/penntree/','/data/penntree/','/data/penntree/']
flagdict['bolt-df-7'],flagdict['bolt-df-6'],flagdict['bolt-df-5'],flagdict['bolt-df-4'],flagdict['bolt-df-3'],flagdict['bolt-df-2'],flagdict['bolt-df-1'] = ['--topless'], ['--topless'],['--topless'],['--topless'], ['--topless'],['--topless'],['--topless']





for a_project in j:

	if os.path.exists(j[a_project]):
		#if a_project in ["ontonotes", 'ewt', 'questionbank']:
		#	continue
		#elif "-sms" in a_project or '-cts' in a_project:
		#	continue
		for any_folder, __, list_of_files in os.walk(localpaths[a_project]):
			#print any_folder
			print any_folder
			for each_file in [x for x in list_of_files if ".gold_skel" in x]:		
				#print(each_file)
				j[a_project]
				parse_folder= os.path.normpath(j[a_project]+metadata.get(a_project,"")+any_folder.replace(localpaths[a_project],""))

				for element in modifications[a_project]:
					
					parse_folder = parse_folder.replace(element[0], element[1])
				#print parse_folder, os.path.exists(parse_folder)
				for each_parse_file in [x for x in os.listdir(parse_folder)]:
					
					tempparsefile = each_parse_file
					if a_project in filemoddict:
						for term in filemoddict[a_project]:
							tempparsefile = tempparsefile.replace(term[0],term[1])
					#print tempparsefile, each_file, each_file.replace(".gold_skel","") in tempparsefile
					if each_file.replace(".gold_skel","") in tempparsefile and (tempparsefile.endswith(".parse") or tempparsefile.endswith(".tree")):
						print each_file, each_parse_file
						#
						print a_project, any_folder.replace(localpaths[a_project],""), each_file, each_parse_file
						#print os.path.exists(parse_folder+"/"+each_parse_file) and os.path.exists(any_folder+"/"+each_file)
						skeleton2conll.start(parse_folder+"/"+each_parse_file, any_folder+"/"+each_file, any_folder+"/"+each_file.replace(".gold_skel",".gold_conll"), 'utf8', ["-trace","--text"]+flagdict.get(a_project,[]))
