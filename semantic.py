import spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

tokens = nlp('cat apple monkey banana')

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

# Interesting Findings

'''

1. Similarity between cat and monkey

Cat and monkey seem to be similar since they are both animals, therefore they have
some semantic similarity.

2. Similarity between banana and monkey

Banana and monkey's semantic similarity is relatively high suggesting
these two words are linked, because monkeys are normally associated with eating
bananas.

3. Similarity between banana and cat

The semantic similarity between banana and cat is low because they belong to two
entirely different categories of "animal" and "fruit" therefore they have a lower level of semantic
similarity.


'''

# An example of my own 

word1 = nlp("dog")
word2 = nlp("bark")

similarity = word1.similarity(word2)
print(similarity)

'''

This example will have a high level of semantic similarity since dog is
associated with action of barking.

'''

# Observations betweeen the two different language models

'''

The main difference between these two models is in their size and the amount
of training data they have been trained on:

en_core_web_md is a larger model that includes word vectors that have been trained
on more data. So it provides more accurate word representations and is suitable for tasks
requiring higher precision and accuracy, like similarity comparisons between longer text.

en-core_web_sm is a smaller model which contains fewer word vectors and is trained on less data
It is lighter in size and faster which makes it suitable for apps with limited computational resources.

'''

