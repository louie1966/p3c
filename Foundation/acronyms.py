acronyms=['LOL','IDK','SMH']

acronyms.append('BFN')
acronyms.append('IMHO')

del acronyms[1]
acronyms.remove('SMH')

acronyms.sort()

print(acronyms)

word='LOL'

if word in acronyms:
    print(f"{word} is in the list")
else:
    print(f"{word} is not in the list")
    
for acronym in acronyms:
    print(acronym)