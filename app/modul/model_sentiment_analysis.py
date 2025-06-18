from transformers import pipeline

hanifnoerr = "hanifnoerr/Fine-tuned-Indonesian-Sentiment-Classifier"
hanifnoerr_model = pipeline(
    "sentiment-analysis",
    model=hanifnoerr,
    tokenizer=hanifnoerr,
    truncation=True,
     max_length=512
)
def analyze_sentiment_hanifnoerr(text):
    try:
        result = hanifnoerr_model(str(text))[0]
        return result['label'], result['score']
    except:
        return 'error', 'error'

crypter70 = "crypter70/IndoBERT-Sentiment-Analysis"
crypter70_model = pipeline(
    "sentiment-analysis",
    model=crypter70,
    tokenizer=crypter70,
    truncation=True,
     max_length=512
)
def analyze_sentiment_crypter70(text):
    try:
        result = crypter70_model(str(text))[0]
        return result['label'], result['score']
    except:
        return 'error', 'error'

w11wo = "w11wo/indonesian-roberta-base-sentiment-classifier"
w11wo_model = pipeline(
    "sentiment-analysis",
    model=w11wo,
    tokenizer=w11wo,
    truncation=True,
     max_length=512
)
def analyze_sentiment_w11wo(text):
    try:
        result = w11wo_model(str(text))[0]
        return result['label'], result['score']
    except:
        return 'error', 'error'

ayameRushia = "ayameRushia/bert-base-indonesian-1.5G-sentiment-analysis-smsa"
ayameRushia_model = pipeline(
    "sentiment-analysis",
    model=ayameRushia,
    tokenizer=ayameRushia,
    truncation=True,
     max_length=512
)
def analyze_sentiment_ayameRushia(text):
    try:
        result = ayameRushia_model(str(text))[0]
        return result['label'], result['score']
    except:
        return 'error', 'error'

Aardiiiiy = "Aardiiiiy/indobertweet-base-Indonesian-sentiment-analysis"
Aardiiiiy_model = pipeline(
    "sentiment-analysis",
    model=Aardiiiiy,
    tokenizer=Aardiiiiy,
    truncation=True,
     max_length=512
)
def analyze_sentiment_Aardiiiiy(text):
    try:
        result = Aardiiiiy_model(str(text))[0]
        return result['label'], result['score']
    except:
        return 'error', 'error'