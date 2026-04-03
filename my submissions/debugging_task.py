# Function to print dictionary values given the keys
def print_values_of(dictionary, keys):
    for key in keys:
        print(dictionary[key]) #changed line to print the dictionary value for given key, not key

# Print dictionary values from simpson_catch_phrases
simpson_catch_phrases = {"lisa": "BAAAAAART!", 
                         "bart": "Eat My Shorts!", 
                         "marge": "Mmm~mmmmm", 
                         "homer": "d'oh!", #added missing comma and quotation mark
                         "maggie": "(Pacifier Suck)"} #closed paranthesis

print_values_of(simpson_catch_phrases, ['lisa', 'bart', 'homer'])

'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''
