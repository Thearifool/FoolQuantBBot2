from transformers import AutoModelForSequenceClassification, AutoTokenizer
class SentimentRiskController:
    def __init__(self):
        self.model = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert")
        self.tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")
        self.risk_multipliers = {
            "positive": 1.2,
            "neutral": 1.0,
            "negative": 0.8
        }

    def adjust_risk(self, news_headlines):
        inputs = self.tokenizer(news_headlines, return_tensors="pt", padding=True)
        outputs = self.model(**inputs)
        sentiment = self.model.config.id2label[outputs.logits.argmax().item()]
        return self.risk_multipliers[sentiment.lower()]
