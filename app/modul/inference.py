import pandas as pd
import re
import string
import json

from modul.model_sentiment_analysis import analyze_sentiment_hanifnoerr,analyze_sentiment_crypter70,analyze_sentiment_w11wo,analyze_sentiment_ayameRushia,analyze_sentiment_Aardiiiiy

def get_label_with_highest_score(row):
    max_score = -float('inf')
    best_label = None

    for label_col, score_col in [
        ('sentiment_result_hanifnoerr', 'score_sentiment_result_hanifnoerr'),
        ('sentiment_result_crypter70', 'score_sentiment_result_crypter70'),
        ('sentiment_result_w11wo', 'score_sentiment_result_w11wo'),
        ('sentiment_result_ayameRushia', 'score_sentiment_result_ayameRushia'),
        ('sentiment_result_Aardiiiiy', 'score_sentiment_result_Aardiiiiy')
    ]:
        label = str(row[label_col]).lower()
        score = row[score_col]

        if score > max_score:
            max_score = score
            best_label = label

    return best_label,max_score

def sentiment_analysis(req):
    data = pd.DataFrame(req.review_text, columns=["review_text"])
    data = data.dropna(subset=['review_text'])  # Drop rows where 'review_text' is missing
    data['review_text_cleaned'] = data['review_text'].astype(str).str.lower()  # Convert to string and lowercase
    data['review_text_cleaned'] = [re.sub(r'[^\x00-\x7f]',r'', i) for i in data['review_text_cleaned']]  # Remove non-ASCII characters
    data['review_text_cleaned'] = [re.sub(r'\n', r' ', i) for i in data['review_text_cleaned']]  # Replace newline characters with spaces
    data['review_text_cleaned'] = data['review_text_cleaned'].apply(
        lambda x: re.sub(f"[{re.escape(string.punctuation)}]", " ", x)  # Remove punctuation
    )
    data['review_text_cleaned'] = data['review_text_cleaned'].apply(lambda x: re.sub(r'\d+', '', x))  # Remove numbers
    data['review_text_cleaned'] = data['review_text_cleaned'].apply(lambda x: re.sub(r'\s+', ' ', x).strip())  # Normalize whitespace
    data = data[data['review_text_cleaned'] != ""]  # Remove rows where cleaned text is empty

    # Fix typo word
    with open("modul/typo_dict.json", "r", encoding="utf-8") as f:
        typo_dict = json.load(f)
    data['review_text_cleaned'] = data['review_text_cleaned'].apply(
        lambda x: ' '.join([typo_dict.get(word.lower(), word) for word in x.split()])
    )

    data[['sentiment_result_hanifnoerr', 'score_sentiment_result_hanifnoerr']] = data['review_text_cleaned'].apply(
        lambda x: pd.Series(analyze_sentiment_hanifnoerr(x))
    )

    data[['sentiment_result_crypter70', 'score_sentiment_result_crypter70']] = data['review_text_cleaned'].apply(
        lambda x: pd.Series(analyze_sentiment_crypter70(x))
    )

    data[['sentiment_result_w11wo', 'score_sentiment_result_w11wo']] = data['review_text_cleaned'].apply(
        lambda x: pd.Series(analyze_sentiment_w11wo(x))
    )

    data[['sentiment_result_ayameRushia', 'score_sentiment_result_ayameRushia']] = data['review_text_cleaned'].apply(
        lambda x: pd.Series(analyze_sentiment_ayameRushia(x))
    )

    data[['sentiment_result_Aardiiiiy', 'score_sentiment_result_Aardiiiiy']] = data['review_text_cleaned'].apply(
        lambda x: pd.Series(analyze_sentiment_Aardiiiiy(x))
    )
    data[['fix_sentiment', 'fix_score']] = pd.DataFrame(data.apply(get_label_with_highest_score, axis=1).tolist(), index=data.index)

    return data[['review_text','review_text_cleaned', 'fix_sentiment', 'fix_score']].to_dict(orient="records")
