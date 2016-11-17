# ! /usr/bin/env python
# usage: bisectTree.py <treeFile>

import sys
from sepp.tree import PhylogeneticTree as Tree

treeFile = sys.argv[1]

T = Tree(treepath=treeFile,schema='nexus')
#T.write_newick_to_path('nw.tre')
t1,t2,e = T.bisect_tree(breaking_edge_style='longest')
t1.write_newick_to_path('t1.tre')
t2.write_newick_to_path('t2.tre')
