import json, codecs, os, logging, argparse
import skeleton2conll

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('setup')




##########################################
########## An inefficient pile of dictionaries for the slight changes in directory structure, etc. which we see in each release...
############################################
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


def flesh_out_all_skel_files(corpora):
    for a_project in corpora:
        if os.path.exists(corpora[a_project]):
            for any_folder, __, list_of_files in os.walk(localpaths[a_project]):
                for each_file in [x for x in list_of_files if ".gold_skel" in x]:        
                    parse_folder= os.path.normpath(corpora[a_project]+metadata.get(a_project,"")+any_folder.replace(localpaths[a_project],""))
                    for element in modifications[a_project]:
                        parse_folder = parse_folder.replace(element[0], element[1])
                    for each_parse_file in [x for x in os.listdir(parse_folder)]:
                        tempparsefile = each_parse_file
                        if a_project in filemoddict:
                            for term in filemoddict[a_project]:
                                tempparsefile = tempparsefile.replace(term[0],term[1])
                        if each_file.replace(".gold_skel","") in tempparsefile and (tempparsefile.endswith(".parse") or tempparsefile.endswith(".tree")):
                            skeleton2conll.start(parse_folder+"/"+each_parse_file, any_folder+"/"+each_file, any_folder+"/"+each_file.replace(".gold_skel",".gold_conll"), 'utf8', ["-trace","--text"]+flagdict.get(a_project,[]))


if __name__ == "__main__":
    corpora = {}
    boltpackages =json.load(codecs.open("boltreleases.json",'r','utf-8'))

    parser = argparse.ArgumentParser()
    parser.add_argument("--ontonotes", help="Location of extracted ontonotes 5.0", default=False)
    parser.add_argument("--ewt", help="Location of extracted English Web Treebank top directory (LDC2012T13", default=False)
    parser.add_argument("--questionbank", help="Location of extracted questionbank directory", default=False)
    parser.add_argument("--bolt", help="base directory of bolt folders (assuming bolt LDC packages listed in boltreleases.json)", default=False)
    args = parser.parse_args()
    if args.ontonotes:
        corpora["ontonotes"] = args.ontonotes
    if args.ewt:
        corpora["ewt"] = args.ewt
    if args.questionbank:
        corpora["questionbank"] = args.questionbank
    if args.bolt:
        for each_release in boltpackages:
            if os.path.exists(os.path.normpath(args.bolt+'/'+boltpackages[each_release])):
                corpora[each_release] = os.path.normpath(args.bolt+'/'+boltpackages[each_release])
    flesh_out_all_skel_files(corpora)




    