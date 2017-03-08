import nltk
from nltk.corpus import treebank

# here we load in the sentences
sentence22 = treebank.parsed_sents('wsj_0003.mrg')[21]
sentence7 = treebank.parsed_sents('wsj_0003.mrg')[6]
sentence13 = treebank.parsed_sents('wsj_0004.mrg')[12]

# here we define a grammar
grammar = nltk.CFG.fromstring("""
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

IVP -> IVerb NP NP | IVerb  NP NP PP

VP -> V NP
VP -> Verb
VP -> Verb NP
VP -> Verb NP PP
VP -> Verb PP
VP -> VP PP

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
""")

# here we let nltk construct a chart parser from our grammar
parser = nltk.ChartParser(grammar)

# input: a list of words
# returns all the parses of a sentence
def allParses(sentenceList):
	return parser.parse(sentenceList)

# input: a list of parse trees
# prints all the parse trees
def printParses(parses):
	for tree in parses:
		print(tree, "\n")

# input: a sentence as a string or as a list of words
# prints a sentence, then parses it and prints all the parse trees
def processSentence(sentence):
	sentenceList = sentence
	if isinstance(sentence,str):
		sentenceList = sentence.split(' ')
	print ('\nOriginal sentence: ' + ' '.join(sentenceList))
	printParses(allParses(sentenceList))

def mainScript():
	processSentence('I like NLP')
	processSentence('the students love the subject')

mainScript()

meals = "Show me the meals on the flight from SF"
processSentence(meals)
