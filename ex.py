text = 'eey'
number = 20

newdict = {text:number}
newdict2 = {text:number+1}
bigdict = {}

bigdict['newdict'] = [newdict]
print(bigdict)
bigdict['newdict'].append(newdict2)
print(bigdict)