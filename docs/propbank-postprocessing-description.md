This document purely explains the difference between what is manually annotated in Propbank and what is produced as "post-processed" Propbank pointers.


### Extedning Local scopes to follow all treebank coreference

We assume that an annotator is annotating the argument that is within the scope of the predicate.  In many cases this is an empty argument, as in the ```(NP-SBJ (-NONE- *PRO*))``` that you
see below:

```
example
```

in contexts where the annotator sees that these are *not* linked to a surface form, they can link these to a surface form themselves.  But otherwise, they assume that if something can be 
derived form a Treebank coreference index, that they do not need to make that link themselves.

This can follow many traces, but will not follow all traces.  For example, if two empty categories point to the same element -- such as the second ```*PRO*``` below -- then that kind of indexation
is not followed:


```
example of a bad trace
```

In addition, the post-processing adds links included by *RNR* and *ICH* elements.   

### LINK-SLC, and relative calsue annotation

Annotators mark terms but do not mark the realtive clause links, as this can be derived from the relative clause.  Instead, the post-processing finds the treebank relative clause construction 
(NP (NP .. SBAR )), add a separate link showing that this realtive caluse link has been made (LINK-SLC), and add those locations to the argument as well. 


### Corrections

Certain kinds of annotations were automatically corrected, which are assumed to be both invalid and correctable.  For example, arguments which are lower than expected on an annotation are promoted to 
have a shorter path.  For example, an argument of have on the NP below would be promoted to the PP:

```
```

### Nested Argument issues 
