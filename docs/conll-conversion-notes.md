
### General introduction to "Start-End" format

The propbank annotations included in ".prop" files represent the arguments of each verb as a list of locations within a parse tree.  However, it is a tradition to convert such annotations to
annotations over surface forms, labeling where each particular argument begins and ends.  An example of a CoNLL file (the ```.gold_conll``` files that come from mapping the ```.gold_skel``` files to their corresponding
treebanks) is shown below:

```
filename                        sentence #  token #     word    POS     parse "bit"      frame file      roleset      #1(have.01)            #13 (lighten_up.02)     #5 (use.01)       #7(implement.01)
                                                                                                                                    #2(like.02)        #4 (expose.01)       #6(call.03)  

google/ewt/email/00/enronsent00_01.xml  15    0            I   PRP        (TOP(S(NP*)          -               -      *             *         *        *        (ARG0*)     *    (ARG0*)
google/ewt/email/00/enronsent00_01.xml  15    1         have   VBP              (VP*         have        have.01    (V*)            *         *        *             *      *         *
google/ewt/email/00/enronsent00_01.xml  15    2        price    NN           (NP(NP*           -               -      *             *         *        *             *      *         *
google/ewt/email/00/enronsent00_01.xml  15    3      targets   NNS                 *)          -               -      *             *         *        *             *      *         *
google/ewt/email/00/enronsent00_01.xml  15    4           of    IN              (PP*           -               -      *             *         *        *             *      *         *
google/ewt/email/00/enronsent00_01.xml  15    5        where   WRB     (SBAR(WHADVP*)          -               -      *    (ARGM-LOC*)        *        *             *      *         *
google/ewt/email/00/enronsent00_01.xml  15    6            I   PRP            (S(NP*)          -               -      *        (ARG0*)   (ARG0*)       *             *      *         *
google/ewt/email/00/enronsent00_01.xml  15    7        would    MD              (VP*           -               -      *    (ARGM-MOD*)        *        *             *      *         *
google/ewt/email/00/enronsent00_01.xml  15    8         like    VB              (VP*        liken        like.02      *           (V*)        *        *             *      *         *
google/ewt/email/00/enronsent00_01.xml  15    9           to    TO            (S(VP*           -               -      *        (ARG1*         *        *             *      *         *
google/ewt/email/00/enronsent00_01.xml  15   10      lighten    VB              (VP*      lighten  lighten_up.02      *             *       (V*        *             *      *         *
google/ewt/email/00/enronsent00_01.xml  15   11           up    RP             (PRT*)          -               -      *             *         *)       *             *      *         *
google/ewt/email/00/enronsent00_01.xml  15   12     exposure    NN           (NP(NP*)      expose      expose.01      *             *    (ARG1*      (V*)            *      *         *
google/ewt/email/00/enronsent00_01.xml  15   13           to    IN              (PP*           -               -      *             *         *   (ARG2*             *      *         *
google/ewt/email/00/enronsent00_01.xml  15   14          ENE   NNP   (NP*))))))))))))          -               -      *             *)        *)       *)            *      *         *
google/ewt/email/00/enronsent00_01.xml  15   15          and    CC                 *           -               -      *             *         *        *             *      *         *
google/ewt/email/00/enronsent00_01.xml  15   16         will    MD              (VP*           -               -      *             *         *        *    (ARGM-MOD*)     *         *
google/ewt/email/00/enronsent00_01.xml  15   17          use    VB              (VP*          use         use.01      *             *         *        *           (V*)     *         *
google/ewt/email/00/enronsent00_01.xml  15   18        calls   NNS              (NP*)        call        call.03      *             *         *        *        (ARG1*)   (V*)        *
google/ewt/email/00/enronsent00_01.xml  15   19           to    TO            (S(VP*           -               -      *             *         *        *        (ARG2*      *         *
google/ewt/email/00/enronsent00_01.xml  15   20    implement    VB              (VP*    implement   implement.01      *             *         *        *             *      *       (V*)
google/ewt/email/00/enronsent00_01.xml  15   21          the    DT              (NP*           -               -      *             *         *        *             *      *    (ARG1*
google/ewt/email/00/enronsent00_01.xml  15   22      stategy    NN           *)))))))          -               -      *             *         *        *             *)     *         *)
google/ewt/email/00/enronsent00_01.xml  15   23            .     .                *))          -               -      *             *         *        *             *      *         *
```
The first eight columns are static, listing the filename, sentence ID, token index, words, parts of speech, and "parse bit" (the sample from the Treebank) for each term.  The "frame file" column
lets you know which ".xml" file contains the actual semantic form for the predicate in question (which is not always the same as the predicate: one must reference "lighten.xml" for lighten_up.02).  
The roleset column gives the actual sense used, and that sense provides roleset specific meanings for each of the numbered arguments.  

Every column after the eighth is a predicate, in order that they appear in the sentence.  Thus the ninth column is for the "have" auxiliary as token #1, the tenth is for "like.02" which is token #8, 
and so forth. Each column can viewed as a "BIO"-type annotation, where "(ARG1*" marks that that token begins the span of "ARG1", and "*)" marks the end of whatever argument was open at that point in time. 


### "R-" Reference Arguments

"R-" arguments are arguments that are referencing another argument in the sentence.  This has been almost always been WH-phrases such as "who" or "that".  Note the "R-A1" in the penultimate column
below, marking the "which" in ""which" is to gauge learning progress":

```
data/ontonotes/nw/wsj/00/wsj_0045.gold_conll-ontonotes/nw/wsj/00/wsj_0045   11    0              He   PRP   (TOP(S(NP(NP*)       -           -   (ARG0*             *             *           *        *
data/ontonotes/nw/wsj/00/wsj_0045.gold_conll-ontonotes/nw/wsj/00/wsj_0045   11    1             and    CC               *        -           -        *             *             *           *        *
data/ontonotes/nw/wsj/00/wsj_0045.gold_conll-ontonotes/nw/wsj/00/wsj_0045   11    2           other    JJ            (NP*        -           -        *             *             *           *        *
data/ontonotes/nw/wsj/00/wsj_0045.gold_conll-ontonotes/nw/wsj/00/wsj_0045   11    3         critics   NNS              *))       -           -        *)            *             *           *        *
data/ontonotes/nw/wsj/00/wsj_0045.gold_conll-ontonotes/nw/wsj/00/wsj_0045   11    4             say   VBP            (VP*       say     say.01      (V*)            *             *           *        *
data/ontonotes/nw/wsj/00/wsj_0045.gold_conll-ontonotes/nw/wsj/00/wsj_0045   11    5            such    JJ     (SBAR(S(NP*        -           -   (ARG1*        (ARG0*             *           *        *
data/ontonotes/nw/wsj/00/wsj_0045.gold_conll-ontonotes/nw/wsj/00/wsj_0045   11    6        coaching    NN               *        -           -        *             *             *           *        *
data/ontonotes/nw/wsj/00/wsj_0045.gold_conll-ontonotes/nw/wsj/00/wsj_0045   11    7            aids   NNS               *)       -           -        *             *)            *           *        *
data/ontonotes/nw/wsj/00/wsj_0045.gold_conll-ontonotes/nw/wsj/00/wsj_0045   11    8             can    MD            (VP*        -           -        *    (ARGM-MOD*)            *           *        *
data/ontonotes/nw/wsj/00/wsj_0045.gold_conll-ontonotes/nw/wsj/00/wsj_0045   11    9          defeat    VB            (VP*    defeat  defeat.01        *           (V*)            *           *        *
data/ontonotes/nw/wsj/00/wsj_0045.gold_conll-ontonotes/nw/wsj/00/wsj_0045   11   10             the    DT      (NP(NP(NP*        -           -        *        (ARG1*             *      (ARG1*        *
data/ontonotes/nw/wsj/00/wsj_0045.gold_conll-ontonotes/nw/wsj/00/wsj_0045   11   11         purpose    NN               *)       -           -        *             *             *           *        *
data/ontonotes/nw/wsj/00/wsj_0045.gold_conll-ontonotes/nw/wsj/00/wsj_0045   11   12              of    IN            (PP*        -           -        *             *             *           *        *
data/ontonotes/nw/wsj/00/wsj_0045.gold_conll-ontonotes/nw/wsj/00/wsj_0045   11   13    standardized    JJ            (NP*        -           -        *             *    (ARGM-ADJ*)          *        *
data/ontonotes/nw/wsj/00/wsj_0045.gold_conll-ontonotes/nw/wsj/00/wsj_0045   11   14           tests   NNS             *)))     test    test.01        *             *           (V*)          *)       *
data/ontonotes/nw/wsj/00/wsj_0045.gold_conll-ontonotes/nw/wsj/00/wsj_0045   11   15               ,     ,               *        -           -        *             *             *           *        *
data/ontonotes/nw/wsj/00/wsj_0045.gold_conll:ontonotes/nw/wsj/00/wsj_0045   11   16           which   WDT     (SBAR(WHNP*)       -           -        *             *             *    (R-ARG1*)       *
data/ontonotes/nw/wsj/00/wsj_0045.gold_conll-ontonotes/nw/wsj/00/wsj_0045   11   17              is   VBZ          (S(VP*        be      be.01        *             *             *         (V*)       *
data/ontonotes/nw/wsj/00/wsj_0045.gold_conll-ontonotes/nw/wsj/00/wsj_0045   11   18              to    TO          (S(VP*        -           -        *             *             *      (ARG2*        *
data/ontonotes/nw/wsj/00/wsj_0045.gold_conll-ontonotes/nw/wsj/00/wsj_0045   11   19           gauge    VB            (VP*     gauge   gauge.01        *             *             *           *      (V*)
data/ontonotes/nw/wsj/00/wsj_0045.gold_conll-ontonotes/nw/wsj/00/wsj_0045   11   20        learning    NN            (NP*        -           -        *             *             *           *   (ARG1*
data/ontonotes/nw/wsj/00/wsj_0045.gold_conll-ontonotes/nw/wsj/00/wsj_0045   11   21        progress    NN   *)))))))))))))       -           -        *)            *)            *           *)       *)
data/ontonotes/nw/wsj/00/wsj_0045.gold_conll-ontonotes/nw/wsj/00/wsj_0045   11   22               .     .              *))       -           -        *             *             *           *        *
```

Our conversion scripts currently define an R-* argument as being a treebank location that has a WH-X treebank label ( as in WHNP, WHPP, or WHADVP) which ALSO participates in a LINK-SLC (relative clause) 
relationship with another argument.  This means that WH-phrases used in questions are not R- arguments, even when they have other discontinuous elements, as in the "ARG2" in the last column below:

```
data/ontonotes/nw/xinhua/02/chtb_0269.gold_conll:ontonotes/nw/xinhua/02/chtb_0269   3    0              Then     RB   (TOP(SBARQ(ADVP*)            -                -        *             *
data/ontonotes/nw/xinhua/02/chtb_0269.gold_conll-ontonotes/nw/xinhua/02/chtb_0269   3    1                 ,      ,                  *             -                -        *             *
data/ontonotes/nw/xinhua/02/chtb_0269.gold_conll-ontonotes/nw/xinhua/02/chtb_0269   3    2              what     WP             (WHNP*)            -                -        *        (ARG2*)
data/ontonotes/nw/xinhua/02/chtb_0269.gold_conll-ontonotes/nw/xinhua/02/chtb_0269   3    3              will     MD               (SQ*             -                -        *    (ARGM-MOD*)
data/ontonotes/nw/xinhua/02/chtb_0269.gold_conll-ontonotes/nw/xinhua/02/chtb_0269   3    4               the     DT               (NP*             -                -        *        (ARG1*
data/ontonotes/nw/xinhua/02/chtb_0269.gold_conll-ontonotes/nw/xinhua/02/chtb_0269   3    5             three     CD              (NML*             -                -        *             *
data/ontonotes/nw/xinhua/02/chtb_0269.gold_conll-ontonotes/nw/xinhua/02/chtb_0269   3    6                -    HYPH                  *             -                -        *             *
data/ontonotes/nw/xinhua/02/chtb_0269.gold_conll-ontonotes/nw/xinhua/02/chtb_0269   3    7             level     NN                  *)            -                -        *             *
data/ontonotes/nw/xinhua/02/chtb_0269.gold_conll-ontonotes/nw/xinhua/02/chtb_0269   3    8           Chinese     JJ                  *             -                -        *             *
data/ontonotes/nw/xinhua/02/chtb_0269.gold_conll-ontonotes/nw/xinhua/02/chtb_0269   3    9      restructured    VBN                  *    restructure  restructure.01      (V*)            *
data/ontonotes/nw/xinhua/02/chtb_0269.gold_conll-ontonotes/nw/xinhua/02/chtb_0269   3   10    administrative     JJ                  *             -                -   (ARG1*             *
data/ontonotes/nw/xinhua/02/chtb_0269.gold_conll-ontonotes/nw/xinhua/02/chtb_0269   3   11            system     NN                  *)            -                -        *)            *)
data/ontonotes/nw/xinhua/02/chtb_0269.gold_conll-ontonotes/nw/xinhua/02/chtb_0269   3   12                be     VB               (VP*             be           be.01        *           (V*)
data/ontonotes/nw/xinhua/02/chtb_0269.gold_conll-ontonotes/nw/xinhua/02/chtb_0269   3   13              like     IN             (PP*)))            -                -        *      (C-ARG2*)
data/ontonotes/nw/xinhua/02/chtb_0269.gold_conll-ontonotes/nw/xinhua/02/chtb_0269   3   14                 ?      .                 *))            -                -        *             *

```

### "C-" Discontinuous Arguments

Some arguments in Propbank are discontinous spans that all refer to the same argument.  This can happen for a number of reasons.  
One reason for this is verb-particle constructions, which give us discontinous C-V arguments such as the one for "top it off" below:
```
data/ontonotes/nw/wsj/23/wsj_2373.gold_conll-
data/ontonotes/nw/wsj/23/wsj_2373.gold_conll-ontonotes/nw/wsj/23/wsj_2373   5    0           To    TO  (TOP(S(S(VP*         -            -         *   (ARGM-ADV*        *
data/ontonotes/nw/wsj/23/wsj_2373.gold_conll-ontonotes/nw/wsj/23/wsj_2373   5    1          top    VB          (VP*        top      top.01       (V*)           *        *
data/ontonotes/nw/wsj/23/wsj_2373.gold_conll-ontonotes/nw/wsj/23/wsj_2373   5    2           it   PRP          (NP*)        -            -    (ARG1*)           *        *
data/ontonotes/nw/wsj/23/wsj_2373.gold_conll:ontonotes/nw/wsj/23/wsj_2373   5    3          off    RP      (PRT*))))        -            -     (C-V*)           *)       *
data/ontonotes/nw/wsj/23/wsj_2373.gold_conll-ontonotes/nw/wsj/23/wsj_2373   5    4            ,     ,             *         -            -         *            *        *
data/ontonotes/nw/wsj/23/wsj_2373.gold_conll-ontonotes/nw/wsj/23/wsj_2373   5    5          you   PRP          (NP*)        -            -    (ARG0*)      (ARG0*)       *
data/ontonotes/nw/wsj/23/wsj_2373.gold_conll-ontonotes/nw/wsj/23/wsj_2373   5    6    captioned   VBD          (VP*    caption  caption.01         *          (V*)       *
data/ontonotes/nw/wsj/23/wsj_2373.gold_conll-ontonotes/nw/wsj/23/wsj_2373   5    7          the    DT       (NP(NP*         -            -         *       (ARG1*   (ARG0*
data/ontonotes/nw/wsj/23/wsj_2373.gold_conll-ontonotes/nw/wsj/23/wsj_2373   5    8        graph    NN             *)        -            -         *            *        *)
data/ontonotes/nw/wsj/23/wsj_2373.gold_conll-ontonotes/nw/wsj/23/wsj_2373   5    9      showing   VBG          (VP*       show     show.01         *            *      (V*)
data/ontonotes/nw/wsj/23/wsj_2373.gold_conll-ontonotes/nw/wsj/23/wsj_2373   5   10          the    DT       (NP(NP*         -            -         *            *   (ARG1*
data/ontonotes/nw/wsj/23/wsj_2373.gold_conll-ontonotes/nw/wsj/23/wsj_2373   5   11      average    JJ             *         -            -         *            *        *
data/ontonotes/nw/wsj/23/wsj_2373.gold_conll-ontonotes/nw/wsj/23/wsj_2373   5   12       number    NN             *)        -            -         *            *        *
data/ontonotes/nw/wsj/23/wsj_2373.gold_conll-ontonotes/nw/wsj/23/wsj_2373   5   13           of    IN          (PP*         -            -         *            *        *
data/ontonotes/nw/wsj/23/wsj_2373.gold_conll-ontonotes/nw/wsj/23/wsj_2373   5   14       months   NNS         (NP*))        -            -         *            *        *
data/ontonotes/nw/wsj/23/wsj_2373.gold_conll-ontonotes/nw/wsj/23/wsj_2373   5   15           in    IN          (PP*         -            -         *            *        *
data/ontonotes/nw/wsj/23/wsj_2373.gold_conll-ontonotes/nw/wsj/23/wsj_2373   5   16            a    DT          (NP*         -            -         *            *        *
data/ontonotes/nw/wsj/23/wsj_2373.gold_conll-ontonotes/nw/wsj/23/wsj_2373   5   17          job    NN             *         -            -         *            *        *
data/ontonotes/nw/wsj/23/wsj_2373.gold_conll-ontonotes/nw/wsj/23/wsj_2373   5   18       search    NN         *)))))        -            -         *            *)       *)
data/ontonotes/nw/wsj/23/wsj_2373.gold_conll-ontonotes/nw/wsj/23/wsj_2373   5   19           as    IN          (PP*         -            -         *       (ARG2*        *
data/ontonotes/nw/wsj/23/wsj_2373.gold_conll-ontonotes/nw/wsj/23/wsj_2373   5   20           ``    ``             *         -            -         *            *        *
data/ontonotes/nw/wsj/23/wsj_2373.gold_conll-ontonotes/nw/wsj/23/wsj_2373   5   21         Time    NN          (NP*         -            -         *            *        *
data/ontonotes/nw/wsj/23/wsj_2373.gold_conll-ontonotes/nw/wsj/23/wsj_2373   5   22          Off    RP           *)))        -            -         *            *)       *
data/ontonotes/nw/wsj/23/wsj_2373.gold_conll-ontonotes/nw/wsj/23/wsj_2373   5   23            .     .             *         -            -         *            *        *
data/ontonotes/nw/wsj/23/wsj_2373.gold_conll-ontonotes/nw/wsj/23/wsj_2373   5   24           ''    ''            *))        -            -         *            *        *

```


Another instance where we see discontinuous arguments is with prepositional stranding occurrences, as in the "about" below:
```
ontonotes/bc/cnn/00/cnn_0002   16   0              Uh    UH   (TOP(S(INTJ*)     -         -    (ARGM-DIS*)     *           *
ontonotes/bc/cnn/00/cnn_0002   16   1            this    DT           (NP*)     -         -        (ARG1*)     *           *
ontonotes/bc/cnn/00/cnn_0002   16   2              is   VBZ           (VP*      be    be.01           (V*)     *           *
ontonotes/bc/cnn/00/cnn_0002   16   3    Jacksborough   NNP     (NP(NP(NP*)     -         -        (ARG2*      *      (ARG1*
ontonotes/bc/cnn/00/cnn_0002   16   4       Tennessee   NNP          (NP*))     -         -             *      *           *)
ontonotes/bc/cnn/00/cnn_0002   16   5              we   PRP    (SBAR(S(NP*)     -         -             *      *      (ARG0*)
ontonotes/bc/cnn/00/cnn_0002   16   6             're   VBP           (VP*      be    be.03             *    (V*)          *
ontonotes/bc/cnn/00/cnn_0002   16   7         talking   VBG           (VP*    talk  talk.01             *      *         (V*)
ontonotes/bc/cnn/00/cnn_0002   16   8           about    IN     (PP*)))))))     -         -             *)     *    (C-ARG1*)
ontonotes/bc/cnn/00/cnn_0002   16   9              /.     .             *))     -         -             *      *           *
```

We also see discontinuous spans with subject raising, it-extraposition, right-node-raising, and a variety of other constructions where a particular semantic argument is realized in
different parts of the annotation.  Some of these are annotated by Propbank annotators as being the same argument, and others of these are traces which were annotated in Treebank 
annotation. For example, the two examples of "begin.01" below both have ARG1 (the thing begun) distributed before and after the verb: "Three new issues ...trading on the New York Stock Exchange"
and "one ... trading on the Nasday / national Market System":

```
data/ontonotes/nw/wsj/06/wsj_0607.gold_conll-ontonotes/nw/wsj/06/wsj_0607   0    0       Three    CD  (TOP(S(S(NP*       -          -        (ARG1*        (ARG1*            *            *
data/ontonotes/nw/wsj/06/wsj_0607.gold_conll-ontonotes/nw/wsj/06/wsj_0607   0    1         new    JJ             *       -          -             *             *            *            *
data/ontonotes/nw/wsj/06/wsj_0607.gold_conll-ontonotes/nw/wsj/06/wsj_0607   0    2      issues   NNS             *)      -          -             *)            *)           *            *
data/ontonotes/nw/wsj/06/wsj_0607.gold_conll-ontonotes/nw/wsj/06/wsj_0607   0    3       begin   VBP          (VP*    begin  begin.01           (V*)            *            *            *
data/ontonotes/nw/wsj/06/wsj_0607.gold_conll:ontonotes/nw/wsj/06/wsj_0607   0    4     trading   VBG        (S(VP*    trade  trade.01      (C-ARG1*           (V*)           *            *
data/ontonotes/nw/wsj/06/wsj_0607.gold_conll-ontonotes/nw/wsj/06/wsj_0607   0    5          on    IN          (PP*       -          -             *    (ARGM-LOC*            *            *
data/ontonotes/nw/wsj/06/wsj_0607.gold_conll-ontonotes/nw/wsj/06/wsj_0607   0    6         the    DT          (NP*       -          -             *             *            *            *
data/ontonotes/nw/wsj/06/wsj_0607.gold_conll-ontonotes/nw/wsj/06/wsj_0607   0    7         New   NNP         (NML*       -          -             *             *            *            *
data/ontonotes/nw/wsj/06/wsj_0607.gold_conll-ontonotes/nw/wsj/06/wsj_0607   0    8        York   NNP             *)      -          -             *             *            *            *
data/ontonotes/nw/wsj/06/wsj_0607.gold_conll-ontonotes/nw/wsj/06/wsj_0607   0    9       Stock   NNP             *       -          -             *             *            *            *
data/ontonotes/nw/wsj/06/wsj_0607.gold_conll-ontonotes/nw/wsj/06/wsj_0607   0   10    Exchange   NNP          *))))      -          -             *)            *)           *            *
data/ontonotes/nw/wsj/06/wsj_0607.gold_conll-ontonotes/nw/wsj/06/wsj_0607   0   11       today    NN        (NP*)))      -          -    (ARGM-TMP*)   (ARGM-TMP*)           *            *
data/ontonotes/nw/wsj/06/wsj_0607.gold_conll-ontonotes/nw/wsj/06/wsj_0607   0   12           ,     ,             *       -          -             *             *            *            *
data/ontonotes/nw/wsj/06/wsj_0607.gold_conll-ontonotes/nw/wsj/06/wsj_0607   0   13         and    CC             *       -          -             *             *            *            *
data/ontonotes/nw/wsj/06/wsj_0607.gold_conll-ontonotes/nw/wsj/06/wsj_0607   0   14         one    CD        (S(NP*)      -          -             *             *       (ARG1*)      (ARG0*)
data/ontonotes/nw/wsj/06/wsj_0607.gold_conll-ontonotes/nw/wsj/06/wsj_0607   0   15       began   VBD          (VP*    begin  begin.01             *             *          (V*)           *
data/ontonotes/nw/wsj/06/wsj_0607.gold_conll:ontonotes/nw/wsj/06/wsj_0607   0   16     trading   VBG        (S(VP*    trade  trade.01             *             *     (C-ARG1*          (V*)
data/ontonotes/nw/wsj/06/wsj_0607.gold_conll-ontonotes/nw/wsj/06/wsj_0607   0   17          on    IN          (PP*       -          -             *             *            *   (ARGM-LOC*
data/ontonotes/nw/wsj/06/wsj_0607.gold_conll-ontonotes/nw/wsj/06/wsj_0607   0   18         the    DT          (NP*       -          -             *             *            *            *
data/ontonotes/nw/wsj/06/wsj_0607.gold_conll-ontonotes/nw/wsj/06/wsj_0607   0   19      Nasdaq   NNP     (NML(NML*)      -          -             *             *            *            *
data/ontonotes/nw/wsj/06/wsj_0607.gold_conll-ontonotes/nw/wsj/06/wsj_0607   0   20           /   SYM             *       -          -             *             *            *            *
data/ontonotes/nw/wsj/06/wsj_0607.gold_conll-ontonotes/nw/wsj/06/wsj_0607   0   21    National   NNP         (NML*       -          -             *             *            *            *
data/ontonotes/nw/wsj/06/wsj_0607.gold_conll-ontonotes/nw/wsj/06/wsj_0607   0   22      Market   NNP            *))      -          -             *             *            *            *
data/ontonotes/nw/wsj/06/wsj_0607.gold_conll-ontonotes/nw/wsj/06/wsj_0607   0   23      System   NNP          *))))      -          -             *             *            *)           *)
data/ontonotes/nw/wsj/06/wsj_0607.gold_conll-ontonotes/nw/wsj/06/wsj_0607   0   24        last    JJ          (NP*       -          -             *             *   (ARGM-TMP*   (ARGM-TMP*
data/ontonotes/nw/wsj/06/wsj_0607.gold_conll-ontonotes/nw/wsj/06/wsj_0607   0   25        week    NN           *)))      -          -             *             *            *)           *)
data/ontonotes/nw/wsj/06/wsj_0607.gold_conll-ontonotes/nw/wsj/06/wsj_0607   0   26           .     .            *))      -          -             *             *            *            *
```
Our official CoNLL conversion scripts will define a ```C-*``` argument as being applied to *every non-reference surface span after the leftmost span for that argument*, regardless of how that surface form was arrived at.  


### ARGX-DSP arguments 

Phrases in some genres have embedded phrases such as ", he said, ", where the "thing said" argument is essentially the entire sentence other than that phrase.  These are specially dealt with both by the Treebank
and during our own post-processing.  Because of the nature of these terms, this "thing that was said" argument is labeled with a "-DSP" flag, and the Propbank pointer is allowed to have other arguments
nested within it.  Since nested arguments are not allowed within the CoNLL arguments, we annotate an ARGX-DSP argument as applying to every span that is not marked by any other argument, as seen below:

```
data/ontonotes/nw/wsj/23/wsj_2328.gold_conll:ontonotes/nw/wsj/23/wsj_2328   2    0     Financial   NNP     (TOP(S(NP*           -              -       (ARG0*     (ARG1-DSP*        *        *
data/ontonotes/nw/wsj/23/wsj_2328.gold_conll-ontonotes/nw/wsj/23/wsj_2328   2    1         Corp.   NNP              *)          -              -            *)             *        *        *
data/ontonotes/nw/wsj/23/wsj_2328.gold_conll-ontonotes/nw/wsj/23/wsj_2328   2    2     purchased   VBD           (VP*     purchase   purchase.01          (V*)             *        *        *
data/ontonotes/nw/wsj/23/wsj_2328.gold_conll-ontonotes/nw/wsj/23/wsj_2328   2    3           the    DT           (NP*           -              -       (ARG1*              *        *        *
data/ontonotes/nw/wsj/23/wsj_2328.gold_conll-ontonotes/nw/wsj/23/wsj_2328   2    4         bonds   NNS              *)          -              -            *)             *        *        *
data/ontonotes/nw/wsj/23/wsj_2328.gold_conll-ontonotes/nw/wsj/23/wsj_2328   2    5             ,     ,          (PRN*           -              -            *              *)       *        *
data/ontonotes/nw/wsj/23/wsj_2328.gold_conll-ontonotes/nw/wsj/23/wsj_2328   2    6           the    DT         (S(NP*           -              -            *         (ARG0*        *        *
data/ontonotes/nw/wsj/23/wsj_2328.gold_conll-ontonotes/nw/wsj/23/wsj_2328   2    7          suit    NN              *)          -              -            *              *)       *        *
data/ontonotes/nw/wsj/23/wsj_2328.gold_conll-ontonotes/nw/wsj/23/wsj_2328   2    8       alleged   VBD          (VP*))      allege     allege.01            *            (V*)       *        *
data/ontonotes/nw/wsj/23/wsj_2328.gold_conll:ontonotes/nw/wsj/23/wsj_2328   2    9             ,     ,              *)          -              -            *   (C-ARG1-DSP*        *        *
data/ontonotes/nw/wsj/23/wsj_2328.gold_conll-ontonotes/nw/wsj/23/wsj_2328   2   10         after    IN         (SBAR*           -              -   (ARGM-TMP*              *        *        *
data/ontonotes/nw/wsj/23/wsj_2328.gold_conll-ontonotes/nw/wsj/23/wsj_2328   2   11           Mr.   NNP      (S(NP(NP*           -              -            *              *   (ARG0*        *
data/ontonotes/nw/wsj/23/wsj_2328.gold_conll-ontonotes/nw/wsj/23/wsj_2328   2   12        Boesky   NNP              *)          -              -            *              *        *        *
data/ontonotes/nw/wsj/23/wsj_2328.gold_conll-ontonotes/nw/wsj/23/wsj_2328   2   13           and    CC              *           -              -            *              *        *        *
data/ontonotes/nw/wsj/23/wsj_2328.gold_conll-ontonotes/nw/wsj/23/wsj_2328   2   14        Drexel   NNP          (NP*))          -              -            *              *        *)       *
data/ontonotes/nw/wsj/23/wsj_2328.gold_conll-ontonotes/nw/wsj/23/wsj_2328   2   15    negotiated   VBD           (VP*    negotiate  negotiate.01            *              *      (V*)       *
data/ontonotes/nw/wsj/23/wsj_2328.gold_conll-ontonotes/nw/wsj/23/wsj_2328   2   16            an    DT           (NP*           -              -            *              *   (ARG2*        *
data/ontonotes/nw/wsj/23/wsj_2328.gold_conll-ontonotes/nw/wsj/23/wsj_2328   2   17     agreement    NN              *           -              -            *              *        *        *
data/ontonotes/nw/wsj/23/wsj_2328.gold_conll-ontonotes/nw/wsj/23/wsj_2328   2   18           for    IN         (SBAR*           -              -            *              *        *        *
data/ontonotes/nw/wsj/23/wsj_2328.gold_conll-ontonotes/nw/wsj/23/wsj_2328   2   19      Vagabond   NNP         (S(NP*           -              -            *              *        *   (ARG0*
data/ontonotes/nw/wsj/23/wsj_2328.gold_conll-ontonotes/nw/wsj/23/wsj_2328   2   20        Hotels   NNP              *)          -              -            *              *        *        *)
data/ontonotes/nw/wsj/23/wsj_2328.gold_conll-ontonotes/nw/wsj/23/wsj_2328   2   21            to    TO           (VP*           -              -            *              *        *        *
data/ontonotes/nw/wsj/23/wsj_2328.gold_conll-ontonotes/nw/wsj/23/wsj_2328   2   22      purchase    VB           (VP*     purchase   purchase.01            *              *        *      (V*)
data/ontonotes/nw/wsj/23/wsj_2328.gold_conll-ontonotes/nw/wsj/23/wsj_2328   2   23             a    DT        (NP(NP*           -              -            *              *        *   (ARG1*
data/ontonotes/nw/wsj/23/wsj_2328.gold_conll-ontonotes/nw/wsj/23/wsj_2328   2   24           51     CD          (NML*           -              -            *              *        *        *
data/ontonotes/nw/wsj/23/wsj_2328.gold_conll-ontonotes/nw/wsj/23/wsj_2328   2   25             %    NN              *)          -              -            *              *        *        *
data/ontonotes/nw/wsj/23/wsj_2328.gold_conll-ontonotes/nw/wsj/23/wsj_2328   2   26         stake    NN              *)          -              -            *              *        *        *
data/ontonotes/nw/wsj/23/wsj_2328.gold_conll-ontonotes/nw/wsj/23/wsj_2328   2   27            in    IN           (PP*           -              -            *              *        *        *
data/ontonotes/nw/wsj/23/wsj_2328.gold_conll-ontonotes/nw/wsj/23/wsj_2328   2   28           the    DT           (NP*           -              -            *              *        *        *
data/ontonotes/nw/wsj/23/wsj_2328.gold_conll-ontonotes/nw/wsj/23/wsj_2328   2   29        thrift    NN            *)))          -              -            *              *        *        *)
data/ontonotes/nw/wsj/23/wsj_2328.gold_conll-ontonotes/nw/wsj/23/wsj_2328   2   30           for    IN           (PP*           -              -            *              *        *   (ARG3*
data/ontonotes/nw/wsj/23/wsj_2328.gold_conll-ontonotes/nw/wsj/23/wsj_2328   2   31         about    RB        (NP(QP*           -              -            *              *        *        *
data/ontonotes/nw/wsj/23/wsj_2328.gold_conll-ontonotes/nw/wsj/23/wsj_2328   2   32             $     $              *           -              -            *              *        *        *
data/ontonotes/nw/wsj/23/wsj_2328.gold_conll-ontonotes/nw/wsj/23/wsj_2328   2   33           34     CD              *           -              -            *              *        *        *
data/ontonotes/nw/wsj/23/wsj_2328.gold_conll-ontonotes/nw/wsj/23/wsj_2328   2   34       million    CD   *))))))))))))          -              -            *)             *        *)       *)
data/ontonotes/nw/wsj/23/wsj_2328.gold_conll-ontonotes/nw/wsj/23/wsj_2328   2   35             .     .             *))          -              -            *              *)       *        *
```


### Overlapping arguments 

Other overlapping arguments occaisionally occur in the data in ways that *should* be overlapping. In order to maintain the general assumption that arguments cannot be nested in these annotations, 
these annotations keep only one argument (the last argument mentioned in the corresponding pointer entry).  One example of this kind of simplification is the "C-ARG4" below,  which theoretically should be 
both part of the ARG3 (2.9 % of respondents) and the ARG4 (3.7% of respondents).  Such constructions are quite low frequency:
```
data/ontonotes/nw/wsj/01/wsj_0141.gold_conll-ontonotes/nw/wsj/01/wsj_0141   22    0             In    IN  (TOP(S(PP*       -          -      *    (ARGM-TMP*
data/ontonotes/nw/wsj/01/wsj_0141.gold_conll-ontonotes/nw/wsj/01/wsj_0141   22    1          1989     CD       (NP*))      -          -      *             *)
data/ontonotes/nw/wsj/01/wsj_0141.gold_conll-ontonotes/nw/wsj/01/wsj_0141   22    2              ,     ,           *       -          -      *             *
data/ontonotes/nw/wsj/01/wsj_0141.gold_conll-ontonotes/nw/wsj/01/wsj_0141   22    3           home    NN    (NP(NML*       -          -      *        (ARG1*
data/ontonotes/nw/wsj/01/wsj_0141.gold_conll-ontonotes/nw/wsj/01/wsj_0141   22    4       purchase    NN           *)      -          -      *             *
data/ontonotes/nw/wsj/01/wsj_0141.gold_conll-ontonotes/nw/wsj/01/wsj_0141   22    5          plans   NNS           *)      -          -      *             *)
data/ontonotes/nw/wsj/01/wsj_0141.gold_conll-ontonotes/nw/wsj/01/wsj_0141   22    6           have   VBP        (VP*     have   have.01    (V*)            *
data/ontonotes/nw/wsj/01/wsj_0141.gold_conll-ontonotes/nw/wsj/01/wsj_0141   22    7         ranged   VBN        (VP*    range  range.01      *           (V*)
data/ontonotes/nw/wsj/01/wsj_0141.gold_conll-ontonotes/nw/wsj/01/wsj_0141   22    8        monthly    RB      (ADVP*)      -          -      *    (ARGM-TMP*)
data/ontonotes/nw/wsj/01/wsj_0141.gold_conll-ontonotes/nw/wsj/01/wsj_0141   22    9           from    IN     (PP(PP*       -          -      *        (ARG3*
data/ontonotes/nw/wsj/01/wsj_0141.gold_conll-ontonotes/nw/wsj/01/wsj_0141   22   10           2.9     CD     (NP(NP*       -          -      *             *
data/ontonotes/nw/wsj/01/wsj_0141.gold_conll-ontonotes/nw/wsj/01/wsj_0141   22   11              %    NN         *)))      -          -      *             *)
data/ontonotes/nw/wsj/01/wsj_0141.gold_conll-ontonotes/nw/wsj/01/wsj_0141   22   12             to    IN        (PP*       -          -      *        (ARG4*
data/ontonotes/nw/wsj/01/wsj_0141.gold_conll-ontonotes/nw/wsj/01/wsj_0141   22   13           3.7     CD     (NP(NP*       -          -      *             *
data/ontonotes/nw/wsj/01/wsj_0141.gold_conll-ontonotes/nw/wsj/01/wsj_0141   22   14              %    NN         *)))      -          -      *             *)
data/ontonotes/nw/wsj/01/wsj_0141.gold_conll:ontonotes/nw/wsj/01/wsj_0141   22   15             of    IN        (PP*       -          -      *      (C-ARG4*
data/ontonotes/nw/wsj/01/wsj_0141.gold_conll-ontonotes/nw/wsj/01/wsj_0141   22   16    respondents   NNS    (NP*)))))      -          -      *             *)
data/ontonotes/nw/wsj/01/wsj_0141.gold_conll-ontonotes/nw/wsj/01/wsj_0141   22   17              .     .          *))      -          -      *             *
```
