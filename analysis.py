from random_username.generate import generate_username
import re, nltk, json
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet, stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from wordcloud import WordCloud
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('vader_lexicon')
wordLemmatizer = WordNetLemmatizer()
stopWords = set(stopwords.words('english'))
sentimentAnalyzer = SentimentIntensityAnalyzer()


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


# Get the average words per sentence, excluding punctuation
def getWordsPerSentence(sentences):
	totalWords = 0
	for sentence in sentences:
		totalWords += len(sentence.split(" "))
	return totalWords / len(sentences)

# Convert part of speech from pos_tag() function
# into wordnet compatible pos tag
posToWordnetTag = {
	"J": wordnet.ADJ,
	"V": wordnet.VERB,
	"N": wordnet.NOUN,
	"R": wordnet.ADV
}
def treebankPosToWordnetPos(partOfSpeech):
	posFirstChar = partOfSpeech[0]
	if posFirstChar in posToWordnetTag:
		return posToWordnetTag[posFirstChar]
	return wordnet.NOUN

# Convert raw list of (word, POS) tuple to a list of strings
# that only include valid english words
def cleanseWordList(posTaggedWordTuples):
	cleansedWords = []
	invalidWordPattern = "[^a-zA-Z-+]"
	for posTaggedWordTuple in posTaggedWordTuples:
		word = posTaggedWordTuple[0]
		pos = posTaggedWordTuple[1]
		cleansedWord = word.replace(".", "").lower()
		if (not re.search(invalidWordPattern, cleansedWord)) and len(cleansedWord) > 1 and cleansedWord not in stopWords:
			cleansedWords.append(wordLemmatizer.lemmatize(cleansedWord, treebankPosToWordnetPos(pos)))
	return cleansedWords



# Get user info and greet
#welcome_user()
#username = get_username()
#greetuser(username)


# Extract and Tokenize Text
articleTextRaw = getArticleText()
articleSentences = tokenizeSentences(articleTextRaw)
articleWords = tokenizeWords(articleSentences)

# Get Sentence Analytics
stockSearchPattern = "[0-9]|[%$€£]|thousand|million|billion|trillion|profit|loss"
keySentences = extractKeySentences(articleSentences, stockSearchPattern)
wordsPerSentence = getWordsPerSentence(articleSentences)

# Get Word Analytics
wordsPosTagged = nltk.pos_tag(articleWords, lang='eng')
articleWordsCleansed = cleanseWordList(wordsPosTagged)

# Generate word cloud
separator = " "
wordCloudFilePath = "wordcloud.png"
wordcloud = WordCloud(width = 1000, height = 700, background_color="beige", colormap="Set2", \
     collocations=False).generate(separator.join(articleWordsCleansed))
wordcloud.to_file(wordCloudFilePath)

# Run Sentiment Analysis
sentimentResult = sentimentAnalyzer.polarity_scores(articleTextRaw)

# Collate analyses into one dictionary
finalResult = {
    "data": {
        "keySentences": keySentences,
        "wordsPerSentence": round(wordsPerSentence, 1),
        "sentiment": sentimentResult,
        "wordCloudFilePath": wordCloudFilePath
    },
    "metadata": {
        "sentencesAnalyzed": len(articleSentences),
        "wordsAnalyzed": len(articleWordsCleansed)
    }
}
finalResultJson = json.dumps(finalResult, indent=4)

# Print for testing
print(finalResultJson)

