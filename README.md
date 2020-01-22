# The Propbank Annotations
This is the repository for the new *unified* Propbank annotations.  Unified frames generalize over different parts of speech, covering verbal, nominal, adjectival and light verb annotations.  

This release updates the annotations for Ontonotes data and the English Web Treebank.  An additional 160,000 predicates of data has been annotated in the BOLT corpora, and will be made public when LDC releases BOLT to the general catalog. This will also host other English Propbank annotations whenever we are able to post them.


### What is the data?

This repository contains two stand-off formats for Propbank data, standard Propbank ".prop" pointers (with stand-off annotations pointing to locations in the parse tree) and ".gold_skel" files, with each token replaced with ```[WORD]```.  To use the data, you will have to acquire the corresponding Treebank releases from the LDC
and run a conversion script (included) to replace those ```[WORD]``` instances with the real text, producing files similar to the CoNLL 2004/2005 SRL format.

The data we can currently release is from two sources:
- data/ontonotes/: [Ontonotes Release 5.0 (LDC2013T19)](https://catalog.ldc.upenn.edu/LDC2013T19)
- data/google/ewt/ : [The English Web Treebank(LDC2012T13)](https://catalog.ldc.upenn.edu/LDC2012T13), developed by the LDC with funding from Google

There are retrofitted datasets awaiting release for the [The Google Questionbank corpus(LDC2012R121)](https://catalog.ldc.upenn.edu/LDC2012R121) and the [BOLT English corpora](http://www.darpa.mil/program/broad-operational-language-translation).  We will post those here as soon as we can. 

### Setup

Go to /docs/scripts and use the little script ```map_all_to_conll.py```.  This script takes direct flags for the locations of the ontonotes, English Web Treebank and Question Bank (```--ontonotes```, ```---ewt```). 

### Frequency Asked Questions: 

##### What's different with this "Unified" data?

Older versions of Propbank split up predicates into verbal, nominal and (in more recent corpora) adjectival forms.  "Unified" propbank brings those together; "create" and "creation" now link to the same sense, for example.  For more
details, see the [Description of Unification Changes](https://github.com/propbank/propbank-documentation/blob/master/other-documentation/Description-of-PB3-changes.md).  The frame files used for this can be acquired [here](https://github.com/propbank/propbank-frames/), with searchable and more readable versions located [here](http://verbs.colorado.edu/propbank/framesets-english-aliases/):

 
##### How does this relate to the AMR inventory?

With the exception of AMR's special "-91" frames (like "have-org-role-91"), AMR annotation uses the same set of Propbank frames used here.  The AMR annotation has not yet adopted all Propbank frames, often because of the different treatment of compositionality in AMR (for example,
Propbank "unhappy.01" is treated  as ```happy.01 :polarity -``` within AMR), but any roleset that exists in AMR will exist in our annotations and will use the same sense and numbered argument distinctions in both projects. 

##### How does this relate to prior Ontonotes releases?

We don't include any other data related to the Ontonotes project, such as coreference annotations.  For those using other Ontonotes resources, it is important to know that our current release *does not* remove disfluencies (labeled in Treebank with "EDITED" nodes) from the surface forms.  [Prior Ontonotes CoNLL-formatted conversions](https://github.com/ontonotes/conll-formatted-ontonotes-5.0) *did* remove those tokens from the data, and that difference may need to be dealt with if your are comparing the two resources. We are very open to feedback regarding this shift, if it causes too much trouble for users of the data. 

##### What frame files do these annotations correspond to? 

The current release corresponds to release "3.1" from https://github.com/propbank/propbank-frames/releases . 

##### Are the .prop files included here the original annotations? How was this retrofitting done? 

The .prop files included in these releases have been adjudicated, quality-controlled, and passed through [a post-processing script](https://github.com/propbank/propbank-documentation/blob/master/postprocessing-documentation/propbank-postprocessing-description.md)). Although specific details of Propbank annotation over the years have changed, we've corrected these files to behave as if they were all annotated in the same way with the same annotators.

Much of the data was also annotated before "Unification" of the frame files, and therefore required retrofitting. Mapping files were manually constructed during this process that mapped different rolesets into the new unified rolesets, which labels which numbered arguments mapped onto the numbered arguments in the new unification files, and which sense and role mappings were ambiguous.  All ambiguous mappings were manually corrected by Propbank annotators, using double annotation and adjudication. 

##### What is the coverage like on nouns and adjectives?

Generally, Propbank annotated every verb in every sentence, every noun in our inventory at the time of annotation, and -- in recent corpora such as English Web Treebank, Questionbank and the BOLT corpora -- every adjective that was the predicate of a copular verb. Only more recent corpora -- such as the English Web Trebank or the BOLT CTS or SMS data -- will have full coverage over both adjectives and all nouns in the frame inventory. 

Prior releases also lacked any annotation over most auxiliary verbs, which may have led to imbalances in roleset distributions, or may have led users to (incorrectly) assume that all unannotated verbs can be assumed to be auxiliaries. We have instead included the annotations of auxiliary verbs such as have.01, be.03, do.01, and even get.03 (passive 'got'), which were automatically given auxiliary senses if and only if the gold Treebank annotations marked them unambiguously as auxiliaries; all edge cases were manually disambiguated.

##### Are there train/dev/test splits?

Files listing the train/dev/test splits are listed in the docs/evaluation folder.  For EWT, we used the splits listed by the [Universal Dependencies project](https://github.com/UniversalDependencies/UD_English).  Note that this data, while retrofits of prior data, uses different assumptions from prior Propbank releases, and therefore SRL results will not be directly comparable against scores reported on CoNLL 2012 data. 

##### One file is showing sentence offset issues (this is the "the empty parse" document)

A single sentence -- sentence 12 in ```ontonotes/nw/p2.5_c2e/00/p2.5_c2e_0034```  -- has no surface tokens.  The official released parse is simply ```(TOP (S (NP-SBJ (-NONE- *PRO*))))```.  This should not pose any issue if you are using the provided ".gold_skel" files.  However, if you do your own mapping from ".prop" files to surface forms, this may violate otherwise reasonable assumptions about the data, as that non-existent sentence does count as a sentence for the purpose of sentence indices.  

##### I'm working with data related to Propbank 1 (Semlink, Factbank, etc.), and some WSJ files are not in Propbank!

580 files used in the Propbank 1 annotations were not carried over into the Ontonotes release -- specifically files related to financial subdomain. [Here](https://github.com/propbank/propbank-documentation/blob/master/other-documentation/missing-from-ontonotes.txt) is a list of the omitted files. 

