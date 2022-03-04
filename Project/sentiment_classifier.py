import pickle


class SentimentClassifier(object):
    def __init__(self):
        with open("model.pkl", "rb") as f:
            self.model = pickle.load(f)

    @staticmethod
    def get_probability_words(pred):
        print(pred)
        if pred == 0:
            return "Негативный"
        else:
            return "Позитивный"

    def predict_text(self, sentence):
        prediction = self.model.predict([sentence])
        return self.get_probability_words(prediction)
