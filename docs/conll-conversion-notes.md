Proposed methodology for the conversion: 

### "R-" Reference Arguments

"R-" arguments are arguments that are referencing another argument in the sentence.  This has been almost always been WH-phrases such as "who" or "that".  Note the "R-A1" in the last column
below, which shows the arguments for "wear".  "that" is given an R-A1, showing that it is not the final surface form of A1, but is used in referencing it: 

```
What                	0	0	WP	     (TOP(SBARQ(WHNP*)         	-	-            	            *   	         (A2*)  	            *   
are                 	0	1	VBP	                 (SQ*          	be	be.03       	          (V*)  	            *   	            *   
the                 	0	2	DT	                 (NP*          	-	-            	            *   	         (A1*   	         (A1*   
headpieces          	0	3	NNS	                    *))        	-	-            	            *   	            *)  	            *)  
called              	0	4	VBN	                 (VP*          	call	call.01   	            *   	          (V*)  	            *   
that                	0	5	WDT	               (SBAR*)         	-	-            	            *   	       (C-A1*   	       (R-A1*)  
the                 	0	6	DT	               (S(NP*          	-	-            	            *   	            *   	         (A0*   
Saudi               	0	7	NNP	                    *          	-	-            	            *   	            *   	            *   
Arabians            	0	8	NNPS	                *)         	-	-            	            *   	            *   	            *)  
wear                	0	9	VBP	                 (VP*)))))     	wear	wear.01   	            *   	            *)  	          (V*)  
?                   	0	10	.	                    *))        	-	-            	            *   	            *   	            *   
```
Our official CoNLL conversion scripts currently define an R-* argument as being a treebank location that (A) has a WH-X treebank label, as in WHNP, WHPP, or WHADVP, and 
(B) participates in a LINK-SLC (relative clause) relationship with another argument.  This means that WH-phrases of questions are not R- arguments, as seen in the "What" below:

```
What                	0	0	WDT	     (TOP(SBARQ(WHNP*          	-	-            	            *   	     (AM-GOL*   
body                	0	1	NN	                    *)         	-	-            	            *   	            *   
of                  	0	2	IN	                 (PP*          	-	-            	            *   	            *   
water               	0	3	NN	                 (NP*)))       	-	-            	            *   	            *)  
does                	0	4	VBZ	                 (SQ*          	do	do.01       	          (V*)  	            *   
the                 	0	5	DT	                 (NP*          	-	-            	            *   	         (A1*   
Colorado            	0	6	NNP	                    *          	-	-            	            *   	            *   
River               	0	7	NN	                    *)         	-	-            	            *   	            *)  
flow                	0	8	VB	                 (VP*          	flow	flow.01   	            *   	          (V*)  
into                	0	9	IN	                 (PP*)))       	-	-            	            *   	   (C-AM-GOL*)  
?                   	0	10	.	                    *))        	-	-            	            *   	            * 
```

### "C-" Discontinuous Arguments

Some arguments in Propbank are discontinous spans that all refer to the same argument.  This can happen for a number of reasons.  One is purely discontinous verbs, as in the (C-V*) on "over" in the following:
```
When                	0	0	WRB	   (TOP(SBARQ(WHADVP*)         	-	-            	            *   	     (AM-TMP*)  	            *   
did                 	0	1	VBD	                 (SQ*          	do	do.01       	          (V*)  	            *   	            *   
Israel              	0	2	NNP	                 (NP*)         	-	-            	            *   	         (A1*)  	         (A0*)  
begin               	0	3	VB	                 (VP*          	begin	begin.02 	            *   	          (V*)  	            *   
turning             	0	4	VBG	               (S(VP*          	turn	turn_over.12	        *   	       (C-A1*   	          (V*)  
the                 	0	5	DT	              (NP(NP*          	-	-            	            *   	            *   	         (A1*   
Gaza                	0	6	NNP	                    *          	-	-            	            *   	            *   	            *   
Strip               	0	7	NNP	                    *)         	-	-            	            *   	            *   	            *   
and                 	0	8	CC	                    *          	-	-            	            *   	            *   	            *   
Jericho             	0	9	NNP	                 (NP*))        	-	-            	            *   	            *   	            *)  
over                	0	10	RP	                (PRT*)         	-	-            	            *   	            *   	        (C-V*)  
to                  	0	11	IN	                 (PP*          	-	-            	            *   	            *   	         (A2*   
the                 	0	12	DT	                 (NP*          	-	-            	            *   	            *   	            *   
PLO                 	0	13	NNP	                    *))))))    	-	-            	            *   	            *)  	            *)  
?                   	0	14	.	                    *))        	-	-            	            *   	            *   	            *   

```


Another occurs with prepositional stranding, as in the (C-AM-LOC at) in the following::
```
What                	0	0	WP	     (TOP(SBARQ(WHNP*)         	-	-            	         (A2*)  	            *   
is                  	0	1	VBZ	                 (SQ*          	be	be.01       	          (V*)  	            *   
the                 	0	2	DT	                 (NP*          	-	-            	         (A1*   	            *   
name                	0	3	NN	                    *)         	-	-            	            *   	            *   
of                  	0	4	IN	                 (PP*          	-	-            	            *   	            *   
the                 	0	5	DT	              (NP(NP*          	-	-            	            *   	     (AM-LOC*   
ballpark            	0	6	NN	                    *)         	-	-            	            *   	            *)  
that                	0	7	WDT	          (SBAR(WHNP*)         	-	-            	            *   	   (R-AM-LOC*)  
the                 	0	8	DT	               (S(NP*          	-	-            	            *   	         (A0*   
Milwaukee           	0	9	NNP	                    *          	-	-            	            *   	            *   
Brewers             	0	10	NNS	                    *)         	-	-            	            *   	            *)  
play                	0	11	VBP	                 (VP*          	play	play.01   	            *   	          (V*)  
at                  	0	12	IN	                 (PP*)))))))   	-	-            	            *)  	   (C-AM-LOC*)  
?                   	0	13	.	                    *))        	-	-            	            *   	            *   
```

This is also seen when arguments are split because of syntactic behaviors, such as topicalization, right-node raising, or other issues. For example, "what is expected" for expect.01 is all under
the "A1" argument, even though that argument is often represented with two constituents:

```
How                 	0	0	WRB	     (TOP(SBARQ(WHNP*          	-	-            	            *   	            *   	         (A2*   
much                	0	1	JJ	                    *)         	-	-            	            *   	            *   	            *)  
are                 	0	2	VBZ	                 (SQ*          	be	be.03       	          (V*)  	            *   	            *   
the                 	0	3	DT	                 (NP*          	-	-            	            *   	         (A1*   	         (A1*   
international       	0	4	JJ	                    *          	-	-            	            *   	            *   	            *   
space               	0	5	NN	                    *          	-	-            	            *   	            *   	            *   
stations            	0	6	NNS	                    *)         	-	-            	            *   	            *)  	            *)  
expected            	0	7	VBN	                 (VP*          	expect	expect.01	            *   	          (V*)  	            *   
to                  	0	8	TO	               (S(VP*          	-	-            	            *   	       (C-A1*   	            *   
cost                	0	9	VB	                 (VP*)))))     	cost	cost.01   	            *   	            *)  	          (V*)  
?                   	0	10	.	                    *))        	-	-            	            *   	            *   	            *   
```
Our official CoNLL conversion scripts will define a ```C-*``` argument as being applied to *every non-reference surface span after the leftmost span for that argument*, regardless of how that surface form was arrived at.  


### DSP arguments 

Phrases in some genres have embedded phrases such as ", he said, ", are viewed as having the "thing said" point to the entire phrase.  These arguments often attach to the entire phrase, and therefore other arguments could be nested within the ARG1-DSP or ARG2-DSP argument.  Instead of presenting these as nested arguments, these arguments are represented using a number of C- phrases in all non-argument elements:
```
nw/wsj/04/wsj_0477.parse 0 0  The        DT   (TOP(S(NP(NP*        -    -  - - -   (A1-DSP*      (A1*     *         *  - 
nw/wsj/04/wsj_0477.parse 0 1  problem    NN               *)       -    -  - - -          *         *     *         *  - 
nw/wsj/04/wsj_0477.parse 0 2  here       RB          (ADVP*))      -    -  - - -          *         *)    *         *  - 
nw/wsj/04/wsj_0477.parse 0 3  ,          ,            (PRN*        -    -  - - -          *)        *     *         *  - 
nw/wsj/04/wsj_0477.parse 0 4  analysts   NNS         (S(NP*)       -    -  - - -       (A0*)        *     *         *  - 
nw/wsj/04/wsj_0477.parse 0 5  say        VBP           (VP*))      say  01 - - -        (V*)        *     *         *  - 
nw/wsj/04/wsj_0477.parse 0 6  ,          ,                *)       -    -  - - - (C-A1-DSP*         *     *         *  - 
nw/wsj/04/wsj_0477.parse 0 7  is         VBZ           (VP*        be   01 - - -          *       (V*)    *         *  - 
nw/wsj/04/wsj_0477.parse 0 8  that       IN          (SBAR*        -    -  - - -          *      (A2*     *         *  - 
nw/wsj/04/wsj_0477.parse 0 9  if         IN        (S(SBAR*        -    -  - - -          *         *     *  (AM-ADV*  - 
nw/wsj/04/wsj_0477.parse 0 10 Paribas    NNP         (S(NP*)       -    -  - - -          *         *  (A0*)        *  - 
nw/wsj/04/wsj_0477.parse 0 11 wins       VBZ           (VP*        win  01 - - -          *         *   (V*)        *  - 
nw/wsj/04/wsj_0477.parse 0 12 its        PRP$          (NP*        -    -  - - -          *         *  (A1*         *  - 
nw/wsj/04/wsj_0477.parse 0 13 66.7       CD               *        -    -  - - -          *         *     *         *  - 
nw/wsj/04/wsj_0477.parse 0 14 %          NN               *))))    -    -  - - -          *         *     *)        *) - 
nw/wsj/04/wsj_0477.parse 0 15 ,          ,                *        -    -  - - -          *         *     *         *  - 
nw/wsj/04/wsj_0477.parse 0 16 remaining  JJ            (NP*        -    -  - - -          *         *     *      (A1*  - 
nw/wsj/04/wsj_0477.parse 0 17 Navigation NNP          (NML*        -    -  - - -          *         *     *         *  - 
nw/wsj/04/wsj_0477.parse 0 18 Mixte      NNP              *)       -    -  - - -          *         *     *         *  - 
nw/wsj/04/wsj_0477.parse 0 19 shares     NNS              *)       -    -  - - -          *         *     *         *) - 
nw/wsj/04/wsj_0477.parse 0 20 will       MD            (VP*        -    -  - - -          *         *     *  (AM-MOD*) - 
nw/wsj/04/wsj_0477.parse 0 21 fall       VB            (VP*        fall 01 - - -          *         *     *       (V*) - 
nw/wsj/04/wsj_0477.parse 0 22 in         IN            (PP*        -    -  - - -          *         *     *  (AM-MNR*  - 
nw/wsj/04/wsj_0477.parse 0 23 value      NN            (NP*))))))) -    -  - - -          *         *)    *         *) - 
nw/wsj/04/wsj_0477.parse 0 24 .          .                *))      -    -  - - -          *)        *     *         *  - 
```

### Overlapping arguments 

Other overlapping arguments have currently been left in the data when present -- these occur very rarely, and we intend to eventually do quick re-annotation of these to correctly remove the overlaps.
