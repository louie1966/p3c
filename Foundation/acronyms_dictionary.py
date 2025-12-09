acronyms = {
    "LOL": "Laughing Out Loud",
    "BRB": "Be Right Back",
    "IDK": "I Don't Know",
    "IMO": "In My Opinion",
    "FYI": "For Your Information",
}
acronyms['SMH'] = "Shaking My Head"
acronyms['TBH'] = "To Be Honest"
acronyms['TBH']="Honestly"
del acronyms['LOL'] 

print(acronyms['TBH'])  # Output: Be Right Back
definition = acronyms.get('LOL')  # Output: Laughing Out Loud

if(definition):
    print(definition)
else:
    print("Definition not found")
