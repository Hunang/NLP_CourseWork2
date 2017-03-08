from nltk.corpus import treebank
from nltk import treetransforms
from nltk import induce_pcfg
from nltk.parse import pchart
from nltk import tokenize, toy_pcfg1, nonterminals

pcfg_prods = toy_pcfg1.productions()

pcfg_prod = pcfg_prods[2]
print ('A PCFG production:', pcfg_prod)
print ('    pcfg_prod.lhs()  =>', pcfg_prod.lhs())
print ('    pcfg_prod.rhs()  =>', pcfg_prod.rhs())
print ('    pcfg_prod.prob() =>', pcfg_prod.prob())

# extract productions from three trees and induce the PCFG
print ("Induce PCFG grammar from treebank data:")

productions = []
for item in treebank.items[:2]:
    for tree in treebank.parsed_sents(item):
        # perform optional tree transformations, e.g.:
        tree.collapse_unary(collapsePOS = False)    # Remove branches A-B-C into A-B+C
        tree.chomsky_normal_form(horzMarkov = 2)    # Remove A->(B,C,D) into A->B,C+D->D

        productions += tree.productions()

S = Nonterminal('S')
grammar = induce_pcfg(S, productions)
print (grammar)