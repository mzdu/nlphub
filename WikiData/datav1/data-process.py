lines = open('integerated.txt').read().split('\n')

import re
from collections import defaultdict

print 'length of lines', len(lines)

dataset = defaultdict(list)

for line in lines:
     
    res = re.split('[:]', line)  
    word = res[0]
    definition  = res[1]
 
    dataset[word].append(definition)
 
print 'final dataset'    
print dataset


    
counter = 1
# only print out sentences with multiple definitions
with open('output.txt', 'w') as f:
    
    f.write('\t'.join(['ID', 'term', 'sentence A', 'sentence B', 'score1', 'score2', 'score3']) + '\n')
    
    for wordDef in dataset:
        if len(dataset[wordDef]) < 2:
            continue
        else:
            defs = '\t'.join(dataset[wordDef][:2])
            wordDefs = '\t'.join([wordDef, defs])
            newline1 = '\t'.join([str(counter), wordDefs])
            
#             print newline1
            
            f.write(newline1 + '\n')
            
            counter += 1
        

