from random_username.generate import generate_username
from nltk.tokenize import word_tokenize, sent_tokenize
import re


# Welcome user
def welcome_user():
    print("Welcome to Text-Analysis-tool. I will mine and analyze text data.")

# Get Username
def get_username():
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        if attempts == 0:
            inputPrompt = "\nTo begin, please enter your username:\n"
        else:
            inputPrompt = "\nPlease try again:\n"

        usernameFromInput = input(inputPrompt).strip()

        if len(usernameFromInput) < 5 or not usernameFromInput.isidentifier():
            print(
                "Your username must be at least 5 characters long "
                "and contain only letters, numbers, or underscores."
            )
            attempts += 1
        else:
            return usernameFromInput

    print(f"\nMaximum {max_attempts} attempts reached. Assigning a random username.")
    return generate_username()

# Greet user
def greetuser(name):
    print(f"\nHello, {name}! Let's get started with your text analysis.")

#Get text from file
def getArticleText():
    f = open("files/article.txt", "r")
    rawText = f.read()
    f.close()
    return rawText.replace("\n", " ").replace("\r", "")

# Extract Sentences from raw Text Body
def tokenizeSentences(rawText):
	return sent_tokenize(rawText)

# Extract Words from list of Sentences
def tokenizeWords(sentences):
	words = []
	for sentence in sentences:
		words.extend(word_tokenize(sentence))
	return words

# Get the key sentences based on search pattern of key words
def extractKeySentences(sentences, searchPattern):
	matchedSentences = []
	for sentence in sentences:
		# If sentence matches desired pattern, add to matchedSentences
		if re.search(searchPattern, sentence.lower()):
			matchedSentences.append(sentence)
	return matchedSentences

# Get user info and greet
welcome_user()
username = get_username()
greetuser(username)


# Extract and Tokenize Text
articleTextRaw = getArticleText()
articleSentences = tokenizeSentences(articleTextRaw)
articleWords = tokenizeWords(articleSentences)

# Get Analytics
stockSearchPattern = "[0-9]|[%$€£]|thousand|million|billion|trillion|profit|loss"
keySentences = extractKeySentences(articleSentences, stockSearchPattern)


#print for testing
articleTextRaw = getArticleText()
print("GOT:")
print(articleTextRaw)
