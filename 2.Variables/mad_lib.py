#
# mad_lib.py
# This program will generate a mad lib based on user input
#

base_prompt = 'Please enter a '  # A prompt instructs the user to enter something
# What do you think string (text) + string (text) does?
noun_prompt = base_prompt + 'noun: '
adjective_prompt = base_prompt + 'adjective: '
verb_prompt = base_prompt + 'verb: '
year_prompt = base_prompt + 'year: '

# We are defining out variables here. Input is a function (we will discuss in the future), that lets us collect data from the user
year_1 = input(year_prompt)
adjective_1 = input(adjective_prompt)
noun_1 = input(noun_prompt)
adjective_2 = input(adjective_prompt)
adjective_3 = input(adjective_prompt)
verb_1 = input(verb_prompt)
verb_2 = input(verb_prompt)

print("It is year " + year_1 +
      " and in the vastness of the universe humans are not alone.")
print("Many light years away from Earth is a " +
      adjective_1 + " plant named " + noun_1 + ".")
print("On " + noun_1 + ", a species of " + adjective_2 + " aliens live.")
print("Their technology is extermely " +
      adjective_3 + " compared to ours here on Earth.")
print("They have cars that can " + verb_1 + " and houses that can " + verb_2)
