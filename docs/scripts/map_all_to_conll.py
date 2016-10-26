import json, codecs, os, logging, argparse
import skeleton2conll

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('setup')







def flesh_out_all_skel_files(corpora, pathconfigurations):
    ##########################################
    ####### Goes through every corpus (treating each BOLT release as its own corpus), and passes evertyhing through skeleton2conll.py)
    ############################################

    localpaths, modifications, metadata, flagdict, filemoddict = pathconfigurations['localpaths'], pathconfigurations['modifications'], pathconfigurations['metadata'], pathconfigurations['flagdict'], pathconfigurations['filemoddict']

    for a_project in corpora:
        if os.path.exists(corpora[a_project]):
            logging.info("building gold_conll files for project "+a_project)
            for any_folder, __, list_of_files in os.walk(localpaths[a_project]):
                
                for each_file in [x for x in list_of_files if ".gold_skel" in x]:        
                    conversion_found= False
                    parse_folder= os.path.normpath(corpora[a_project]+metadata.get(a_project,"")+any_folder.replace(localpaths[a_project],""))
                    if a_project in modifications:
                        parse_folder = parse_folder.replace(modifications[a_project][0], modifications[a_project][1])
                    for each_parse_file in [x for x in os.listdir(parse_folder)]:
                        tempparsefile = each_parse_file
                        if a_project in filemoddict:
                            for term in filemoddict[a_project]:
                                tempparsefile = tempparsefile.replace(term[0],term[1])
                        if each_file.replace(".gold_skel","") in tempparsefile and (tempparsefile.endswith(".parse") or tempparsefile.endswith(".tree")):
                            skeleton2conll.start(parse_folder+"/"+each_parse_file, any_folder+"/"+each_file, any_folder+"/"+each_file.replace(".gold_skel",".gold_conll"), 'utf8', ["-trace","--text"]+flagdict.get(a_project,[]))
                            conversion_found= True
                    if not conversion_found:
                        logging.info(each_file+" couldn't find its corresponding parse file in "+parse_folder)
        else:
            logging.info(a_project+" doesn't seem to be at "+corpora[a_project])

def check_locations(corpora, pathconfigurations):
    ##########################################
    ####### Check if all locations work as expected
    ############################################

    localpaths, modifications, metadata, flagdict, filemoddict = pathconfigurations['localpaths'], pathconfigurations['modifications'], pathconfigurations['metadata'], pathconfigurations['flagdict'], pathconfigurations['filemoddict']
    for a_project in corpora:
        if not os.path.exists(corpora[a_project]):
            logging.error(a_project+" doesn't seem to be at "+corpora[a_project])
        elif not os.path.exists(corpora[a_project]+metadata[a_project]):
            logging.error(a_project+": couldn't find tree files at "+corpora[a_project]+metadata[a_project])
        else:
            logging.info(a_project+" seems to be present")




if __name__ == "__main__":
    corpora = {}
    pathconfigurations = json.load(codecs.open("configurations.json",'r','utf-8'))
    parser = argparse.ArgumentParser()
    parser.add_argument("--ontonotes", help="Location of extracted ontonotes 5.0", default=False)
    parser.add_argument("--ewt", help="Location of extracted English Web Treebank top directory (LDC2012T13", default=False)
    parser.add_argument("--test", help="just display paths and confirm packages", default="False")
    args = parser.parse_args()
    if args.ontonotes:
        corpora["ontonotes"] = args.ontonotes
    if args.ewt:
        corpora["ewt"] = args.ewt
    if args.test.lower() == "true":
        check_locations(corpora, pathconfigurations)
    else:
        flesh_out_all_skel_files(corpora, pathconfigurations)

