#when we have acyclic graph



graphh = {
    'f':['g','h'],
    'g':['h'],
    'h':[],
    'i':['g','k'],
    'j':['i'],
    'k':[]
}

print(hasPath(graphh,'j','h'))