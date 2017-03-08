import nltk
from nltk import tree, nonterminals 



#==============================================================================
# Grammar rules
#==============================================================================
#grammar = nltk.CFG.fromstring("""
#S -> NP VP
#NP -> Det N | 'NLP' | 'I'
#VP -> V NP
#Det -> 'the'
#N -> 'students' | 'subject'
#V -> 'like' | 'love'
#
#
#S -> Aux NP VP
#S -> VP
#NP -> Pronoun
#NP -> Proper-Noun
#NP -> Det Nominal 
#Nominal -> Noun 
#Nominal -> Nominal Noun
#Nominal -> Nominal PP 
#
#
#
#S -> IVP 
#IVP -> IVerb NP NP 
#IVerb ->  NP NP PP
#
#NP -> NP PP
#
#VP -> Verb
#VP -> Verb NP
#VP -> Verb NP PP
#VP -> Verb PP
#VP -> VP PP
#verb -> VP
#PP -> Preposition NP     
# 
#Det -> 'that' | 'this' | 'the' | 'a'
#Noun -> 'book' | 'flight' | 'meal' | 'money' | 'meals'
#Verb -> 'book' | 'include' | 'prefer' | 'Show'
#IVerb -> 'Show' |'show'
#Pronoun -> 'I' | 'she' | 'me'
#Proper-Noun -> 'Houston' | 'NWA' | 'SF' | 'Phoenix' | 'phoenix'
#Aux -> does
#Preposition -> 'from' | 'to' | 'on' | 'near' |'through'
#
#""")

#parser = nltk.ChartParser(grammar)



#==============================================================================
# 
#==============================================================================

sentence = "show me the meals on the flight from Phoenix"

def loadData(path):
	with open(path,'r') as f:
		data = f.read().split('\n')
	return data

def getTreeData(data):
	return map(lambda s: tree.Tree.fromstring(s), data)



# Main script
print ("loading data..")
data = loadData('parseTrees.txt')
print ("generating trees..")
treeData = getTreeData(data)
print ("done!")

allSubTreesProd = []

for itms in treeData:
    allSubTreesProd+=itms.productions()
    print(itms.productions())


S = nltk.Nonterminal("S")
grammar = nltk.induce_pcfg(S, allSubTreesProd)
parser = nltk.ChartParser(grammar)

def allParses(sentenceList):
	return parser.parse(sentenceList)

# input: a list of parse trees
# prints all the parse trees
printTree = []
def printParses(parses):
    for curtree in parses:
        print(curtree)
        printTree.append(curtree)

# input: a sentence as a string or as a list of words
# prints a sentence, then parses it and prints all the parse trees
theParses = ""
def processSentence(sentence):
    sentenceList = sentence
    if isinstance(sentence,str):
        sentenceList = sentence.split(' ')
    print ('Original sentence: ' + ' '.join(sentenceList))
    theParses = ((allParses(sentenceList)))
    printParses(allParses(sentenceList))


print("#############################################################")
print("Parsed sentences")
print("#############################################################")

print(processSentence(sentence))



sortedGrammar = sorted(grammar.productions(rhs=nltk.Nonterminal("IVP")))[:2]
print(sortedGrammar)
# finding the probability of the left hand side 
print( grammar.productions(lhs=nltk.Nonterminal("IVP"))[1].prob())


for item in grammar.productions(lhs=nltk.Nonterminal("S")):
    print(item)


viterbi_parser = nltk.ViterbiParser(grammar)
viterbi_parser.trace(100)
for item in viterbi_parser.parse((sentence).split()):
    print(item)
    
