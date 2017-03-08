import nltk
from nltk import tree, nonterminals, induce_pcfg

#==============================================================================
# Grammar
#==============================================================================
rules = """
S -> NP VP
S -> Aux NP VP
S -> VP
S -> IVP 

NP -> NP PP
NP -> Pronoun
NP -> Proper-Noun
NP -> Det Nominal 

Nominal -> Noun 
Nominal -> Nominal Noun
Nominal -> Nominal PP 

IVP -> IVerb NP NP 
IVerb ->  NP NP PP

VP -> V NP
VP -> Verb
VP -> Verb NP
VP -> Verb NP PP
VP -> Verb PP
VP -> VP PP

verb -> VP

PP -> Preposition NP

Det -> 'the'
N -> 'students' | 'subject'
V -> 'like' | 'love'
NP -> Det N | 'NLP' | 'I'     
Det -> 'that' | 'this' | 'the' | 'a'
Noun -> 'book' | 'flight' | 'meal' | 'money' | 'meals'
Verb -> 'book' | 'include' | 'prefer' | 'Show'
IVerb -> 'Show'
Pronoun -> 'I' | 'she' | 'me'
Proper-Noun -> 'Houston' | 'NWA' | 'SF'
Aux -> 'does'
Preposition -> 'from' | 'to' | 'on' | 'near' |'through'
"""

grammar = nltk.CFG.fromstring(rules)

parser = nltk.ChartParser(grammar)

sentence = "show me the meals on the flight from Phoenix"

#==============================================================================
# Functions
#==============================================================================
def loadData(path):
	with open(path,'r') as f:
		data = f.read().split('\n')
	return data

def getTreeData(data):
	return map(lambda s: tree.Tree.fromstring(s), data)

def printParses(parses):
	for trees in parses:
		print(trees)

def processSentence(sentence):
	sentenceList = sentence
	if isinstance(sentence,str):
		sentenceList = sentence.split(' ')
	print ('Original sentence: ' + ' '.join(sentenceList))
	printParses(allParses(sentenceList))
    
def allParses(sentenceList):
	return parser.parse(sentenceList)
#==============================================================================
#  Main script
#==============================================================================
data = loadData('parseTrees.txt')
treeData = getTreeData(data)
print ("done loading data\n\n")

S = nltk.Nonterminal("S")
allSubTreesProd = []
for itms in treeData:
    allSubTreesProd+=itms.productions()    

grammar = nltk.induce_pcfg(S, allSubTreesProd)
parser = nltk.InsideChartParser(grammar)

#viterbi_parser = nltk.ViterbiParser(grammar)
#viterbi_parser.trace(100)
for item in parser.parse((sentence).split()):
    print(item)