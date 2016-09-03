# The Propbank Annotations
This is the repository for the new *unified* Propbank annotations.  Unified frames generalize over different parts of speech, covering verbal, nominal, adjectival and light verb annotations.  We have 
retrofit a few of the core datasets annotated with this Propbank data -- the GALE Ontonotes propbank data, the BOLT data, and two corpora funded with gifts from Google -- and are releasing it all with 
consitent set of Propbank frames and a consistent conversion to a CoNLL-style format. 

This annotation is a *tentative release*, and some small issues will be subject to change. 


### What is the data?

This repository contains two stand-off formats for Propbank data, standard Propbank pointers and stand-off "skel" files, with each token replaced with ```[WORD]```.  To use the data, you will have to acquire the corresponding Treebank releases from the LDC
and run a conversion script (included) to replace those ```[WORD]``` instances with the real text. 

The data is comes from a variety of sources:
- data/ontonotes/: [Ontonotes Release 5.0 (LDC2013T19)](https://catalog.ldc.upenn.edu/ldc2013t19), which s 
- data/google/ewt/ : [The English Web Treebank(LDC2012T13)](https://catalog.ldc.upenn.edu/ldc2012t13), developed by the LDC with funding from Google
- data/google/questionbank/ : [The Google Questionbank corpus(LDC2012R121)](https://catalog.ldc.upenn.edu/LDC2012R121), the corpus from [Judge et al 2006](http://www.computing.dcu.ie/~jjudge/pubs/judge06acl.pdf) with LDC revisions to the Treebank funded by Google.
- data/bolt/df/ : The BOLT Discussion Forum corpora that were Propbanked  are currently released in seven different parts, and should be downloaded as [Part 1(LDC2012E92)](https://catalog.ldc.upenn.edu/LDC2012E92), [Part 2(LDC2012E97)](https://catalog.ldc.upenn.edu/LDC2012E97), [Part 3(LDC2012E114)](https://catalog.ldc.upenn.edu/LDC2012E114), [Part 4(LDC2013E17)](https://catalog.ldc.upenn.edu/LDC2013E17), [Part 5(LDC2013E40)](https://catalog.ldc.upenn.edu/LDC2013E40), [Part 7(LDC2013E76)](https://catalog.ldc.upenn.edu/LDC2013E76) and [Part 6(LDC2013E102)](https://catalog.ldc.upenn.edu/LDC2013E102).
- data/bolt/sms/ : The BOLT SMS English corpora that were Propbanked are currently released as five parts, as [Part 1 (LDC2013E127)](https://catalog.ldc.upenn.edu/LDC2013E127), [Part 2(LDC2014E03)](https://catalog.ldc.upenn.edu/LDC2014E03), [Part 3 (LDC2014E44)](https://catalog.ldc.upenn.edu/LDC2014E44), [Part 4 (LDC2014E78)](https://catalog.ldc.upenn.edu/LDC2014E78), [Part 5 (LDC2014E107)](https://catalog.ldc.upenn.edu/LDC2014E107), 
- data/bolt/cts/ : The BOLT CTS corpora that were Propbanked are currently released in three different parts, as [Part 1 (LDC2015E15)](https://catalog.ldc.upenn.edu/LDC2015E15), [Part 2 (LDC2015E25)](https://catalog.ldc.upenn.edu/LDC2015E25), and [Part 3(LDC2015E30)]((https://catalog.ldc.upenn.edu/LDC2015E30))

For all questions regarding acquiring the data, consult the [LDC](https://www.ldc.upenn.edu/)

### What's different with this "unified" data?

Older versions of Propbank split up predicates into verbal, nominal and (in more recent corpora) adjectival forms.  "Unified" propbank brings those together; "create" and "creation" now link to the same sense, for example.  For more
details, see the [Description of Unification Changes](https://github.com/propbank/propbank-documentation/blob/master/other-documentation/Description-of-PB3-changes.md).  The frame files used for this can be acquired [here](https://github.com/propbank/propbank-frames/), with searchable and more readable versions located [here](http://verbs.colorado.edu/propbank/framesets-english-aliases/):


### Are there train/dev/test splits?


*Please use pre-existing splits to make sure your results are valid*.  We'll try to keep as much information as possible in docs/evaluation to make this as easy as possible.

 
### How does this relate to the AMR inventory?

With the exception of AMR's special "-91" frames (like "have-org-role-91"), AMR annotation uses the same set of Propbank frames used here.  The AMR frames exclude certain Propbank rolesets when it can decompose them (for example,
Propbank "unhappy.01" is treated as Propbank "happy.01" combined with a ```:polarity -``` argument), but such cases are relatively rare. 

### Setup

Go to /docs/scripts and use the little script ```map_all_to_conll.py```.  This script takes direct flags for the locations of the ontonotes, English Web Treebank and Question Bank (```--ontonotes```, ```---ewt```,
and ```--questionbank```) and an argument ```--bolt``` pointing at a folder containing the 15 BOLT treebanks.  It should prepare .gold_conll files in place for every Treebank that you can provide; 10120 files and 3,699,171 words total, if you have all releases. 


