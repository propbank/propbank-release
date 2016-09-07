# The Propbank Annotations
This is the repository for the new *unified* Propbank annotations.  Unified frames generalize over different parts of speech, covering verbal, nominal, adjectival and light verb annotations.  

This release updates the annotations for Ontonotes data, the English Web Treebank, Question Bank, and all corpora released under the BOLT project.  This should be considered a *preliminary*, *beta* release of this data; please contact us before reporting results on the data. 


### What is the data?

This repository contains two stand-off formats for Propbank data, standard Propbank pointers and stand-off "gold_skel" files, with each token replaced with ```[WORD]```.  To use the data, you will have to acquire the corresponding Treebank releases from the LDC
and run a conversion script (included) to replace those ```[WORD]``` instances with the real text. 

The data is comes from a variety of sources:
- data/ontonotes/: [Ontonotes Release 5.0 (LDC2013T19)](https://catalog.ldc.upenn.edu/ldc2013t19)
- data/google/ewt/ : [The English Web Treebank(LDC2012T13)](https://catalog.ldc.upenn.edu/ldc2012t13), developed by the LDC with funding from Google
- data/google/questionbank/ : [The Google Questionbank corpus(LDC2012R121)](https://catalog.ldc.upenn.edu/LDC2012R121), the corpus from [Judge et al 2006](http://www.computing.dcu.ie/~jjudge/pubs/judge06acl.pdf) with LDC revisions to the Treebank funded by Google.

The various BOLT corpora might be only available to certain LDC members, and are distributed through many small packages:

- data/bolt/df/ : Corpora covering English discussion forum text.   Treebanks are available as:
  - [Part 1(LDC2012E92)](https://catalog.ldc.upenn.edu/LDC2012E92)
  - [Part 2(LDC2012E97)](https://catalog.ldc.upenn.edu/LDC2012E97)
  - [Part 3(LDC2012E114)](https://catalog.ldc.upenn.edu/LDC2012E114)
  - [Part 4(LDC2013E17)](https://catalog.ldc.upenn.edu/LDC2013E17)
  - [Part 5(LDC2013E40)](https://catalog.ldc.upenn.edu/LDC2013E40)
  - [Part 6(LDC2013E102)](https://catalog.ldc.upenn.edu/LDC2013E102)
  - [Part 7(LDC2013E76)](https://catalog.ldc.upenn.edu/LDC2013E76)
- data/bolt/sms/ : The BOLT SMS English corpora, available as:
  - [Part 1 (LDC2013E127)](https://catalog.ldc.upenn.edu/LDC2013E127)
  - [Part 2(LDC2014E03)](https://catalog.ldc.upenn.edu/LDC2014E03)
  - [Part 3 (LDC2014E44)](https://catalog.ldc.upenn.edu/LDC2014E44)
  - [Part 4 (LDC2014E78)](https://catalog.ldc.upenn.edu/LDC2014E78)
  - [Part 5 (LDC2014E107)](https://catalog.ldc.upenn.edu/LDC2014E107), 
- data/bolt/cts/ : The BOLT CTS (conversational telephone speech) corpora):
  - [Part 1 (LDC2015E15)](https://catalog.ldc.upenn.edu/LDC2015E15)
  - [Part 2 (LDC2015E25)](https://catalog.ldc.upenn.edu/LDC2015E25)
  - [Part 3(LDC2015E30)]((https://catalog.ldc.upenn.edu/LDC2015E30))

For all questions regarding acquiring the data, consult the [LDC](https://www.ldc.upenn.edu/)


### Setup

Go to /docs/scripts and use the little script ```map_all_to_conll.py```.  This script takes direct flags for the locations of the ontonotes, English Web Treebank and Question Bank (```--ontonotes```, ```---ewt```,
and ```--questionbank```). A fourth argument, ```--bolt```, should point to a folder containing all BOLT treebanks that one has.  If one has all the released treebanks, this should result in 10120 .gold_conll files and 3,699,171 words total. 


### What's different with this "Unified" data?

Older versions of Propbank split up predicates into verbal, nominal and (in more recent corpora) adjectival forms.  "Unified" propbank brings those together; "create" and "creation" now link to the same sense, for example.  For more
details, see the [Description of Unification Changes](https://github.com/propbank/propbank-documentation/blob/master/other-documentation/Description-of-PB3-changes.md).  The frame files used for this can be acquired [here](https://github.com/propbank/propbank-frames/), with searchable and more readable versions located [here](http://verbs.colorado.edu/propbank/framesets-english-aliases/):

 
### How does this relate to the AMR inventory?

With the exception of AMR's special "-91" frames (like "have-org-role-91"), AMR annotation uses the same set of Propbank frames used here.  The AMR annotation has not yet adopted all Propbank frames, often because of the different treatment of compositionality in AMR (for example,
Propbank "unhappy.01" is treated  as ```happy.01 :polarity -``` within AMR), but any roleset that exists in AMR will exist in our annotations and will use the same sense and numbered argument distinctions in both projects. 

### How does this relate to prior Ontonotes releases?

We don't include any other data related to the Ontonotes project, such as coreference annotations.  For those using other Ontonotes resources, it is important to know that our current release *does not* remove disfluencies (labeled in Treebank with "EDITED" nodes) from the surface forms.  [Prior Ontonotes CoNLL-formatted conversions](https://github.com/ontonotes/conll-formatted-ontonotes-5.0) *did* remove those tokens from the data, and that difference may need to be dealt with if your are comparing the two resources. We are very open to feedback regarding this shift, if it causes too much trouble for users of the data. 

### What frame files do these annotations correspond to? 

The current release corresponds to release "3.1" from https://github.com/propbank/propbank-frames/releases . 

### Are the .prop files included here the original annotations? How was this retrofitting done? 

The .prop files included in these releases have been adjudicated, quality-controlled, and passed through [a post-processing script](https://github.com/propbank/propbank-documentation/blob/master/postprocessing-documentation/propbank-postprocessing-description.md)). Although specific details of Propbank annotation over the years have changed, we've corrected these files to behave as if they were all annotated in the same way with the same annotators.

Much of the data was also annotated before "Unification" of the frame files, and therefore required retrofitting. Mapping files were manually constructed during this process that mapped different rolesets into the new unified rolesets, which labels which numbered arguments mapped onto the numbered arguments in the new unification files, and which sense and role mappings were ambiguous.  All ambiguous mappings were manually corrected by Propbank annotators, using double annotation and adjudication. 

### I'm seeing nouns and adjectives without annotations

Generally, Propbank annotated every verb in every sentence, every noun in our inventory at the time of annotation, and -- in recent corpora such as English Web Treebank, Questionbank and the BOLT corpora -- every adjective that was the predicate of a copular verb. Only more recent corpora -- such as the English Web Trebank or the BOLT CTS or SMS data -- will have full coverage over both adjectives and all nouns in the frame inventory. 

Prior releases also lacked any annotation over most auxiliary verbs, which may have led to imbalances in roleset distributions, or may have led users to (incorrectly) assume that all unannotated verbs can be assumed to be auxiliaries. We have instead included the annotations of auxiliary verbs such as have.01, be.03, do.01, and even get.03 (passive 'got'), which were automatically given auxiliary senses if and only if the gold Treebank annotations marked them unambiguously as auxiliaries; all edge cases were manually disambiguated.

### Are there train/dev/test splits?

*Please use pre-existing splits to make sure your results are valid*.  We'll try to keep as much information as possible in docs/evaluation to make this as easy as possible.  Most of these corpora have well-established train/dev/splits that should be followed. 
