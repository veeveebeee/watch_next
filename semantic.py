# Create a file called semantic.py and run all the code extracts above.

import spacy
nlp = spacy.load('en_core_web_md')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

# Write a note about what you found interesting about the similarities
# between cat, monkey and banana and think of an example of your own.

# I find it interesting that the program manages to indentify that monkey is related to banana more than cat is; I wonder what 
# learning and programming took place to allow it to recognise this.

# my example:

tokens = nlp('car bicycle driver cyclist pedestrian')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

'''
I find this interesting as the program finds less similarity between bicycle and cyclist than between car and driver, and they
seem even to me. Also a bicyle has more in common with a pedestrian than a car, maybe because they share lanes sometimes. 
I can't understand why pedestrain has more in common with the bike than the human riding it.
'''

# Run the example file with the simpler language model ‘en_core_web_sm’
# and write a note on what you notice is different from the model
# 'en_core_web_md'.

'''
First of all I got this warning first: 
UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be 
based on the tagger, parser and NER, which may not give useful similarity judgements. This may happen if you're using one 
of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. 
You can always add your own word vectors, or use one of the larger models instead if available.


'''

# Host your solution on a Git host such as GitLab or GitHub.
# Remember to exclude any venv or virtualenv files from your repo.
# Add the link for your remote Git repo to a text file named
# semantic_similarity.txt