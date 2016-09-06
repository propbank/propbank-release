# The Propbank Annotations
This is the repository for the new *unified* Propbank annotations.  Unified frames generalize over different parts of speech, covering verbal, nominal, adjectival and light verb annotations.  

This release updates the annotations for Ontonotes data, the English Web Treebank, Question Bank, and all corpora released under the BOLT project.  This should be considered a *preliminary*, *beta* release of this data; please contact us before reporting results on the data. 


### What is the data?

This repository contains two stand-off formats for Propbank data, standard Propbank pointers and stand-off "skel" files, with each token replaced with ```[WORD]```.  To use the data, you will have to acquire the corresponding Treebank releases from the LDC
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
Propbank "unhappy.01" is treated  ```happy.01 :polarity -``` within AMR), but any roleset that exists in AMR should exist in our annotations and make the sme sense and numbered argument distinctions. 

### How does this relate to prior Ontonotes releases?

We don't include any other data related to the Ontonotes project, and users are invited to make those links themselves.  A specific caveat regarding the current form of the  data is important in this regard: our current release *does not* remove parts of the surface trees that were labeled in Treebank with "EDITED" nodes.  Prior Ontonotes CoNLL conversions did remove those tokens from their releases, and therefore you may need to handle that difference when handling the data. 

### What frame files do these annotations correspond to? 

These correspond to release "3.1" from https://github.com/propbank/propbank-frames/releases .  

### Were all predicates annotated? 

Generally, Propbank annotation dealt with every verb in every sentence, every noun that was in the inventory at the time of annotation, and -- in recent corpora such as English Web Treebank, Questionbank and the BOLT corpora -- every adjective that was the predicate of a copular verb.  Some portions of the data -- specifically, the wb/sel folders within ontonotes -- also did not gain full coverage of all verbs.  If one wants to train a system for predicate detection, we invite them to use more recent Google and BOLT datasets to do so.  

We have also included in this release the semi-gold annotations of auxiliary verbs such as have.01, be.03, and get.03 (passive 'got').  These were automatically labeled if and only if the gold syntax annotations treated them unambigiously as auxiliaries, and all edge cases were manually annotated. 

### Are there train/dev/test splits?

*Please use pre-existing splits to make sure your results are valid*.  We'll try to keep as much information as possible in docs/evaluation to make this as easy as possible.  Most of these corpora have well-established train/dev/splits that should be followed. 
