acronyms = {"LOL": "laughing out loud", 
            "IDK": "I don't know", 
            "TBH": "to be honest"}

try:
    definition = acronyms["BRB"]
    print(f"The definition of 'BRB' is: {definition}")
except KeyError as e:
    print(f"Error: The acronym '{e.args[0]}' is not found in the dictionary.")
    definition = "unknown acronym"
finally:
    print("Acronyms defined are:")
    for acronym in acronyms:
        print(f"{acronym}: {acronyms[acronym]}")

print("program continues...")