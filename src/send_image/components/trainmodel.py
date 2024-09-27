
import joblib
class TrainedModel:
    def __init__(self, model_path):
        """
        Initialize the class by loading the trained model from the specified .pkl file.

        :param model_path: The path to the .pkl file containing the trained model.
        """
        self.model = joblib.load(model_path)
    
    def predict(self, data):
        """
        Make predictions using the loaded model.

        :param data: Input data for making predictions.
        :return: Predictions made by the model.
        """
        # Make sure data is an iterable (list of strings)
        if isinstance(data, str):
           data = [data]
        return self.model.predict(data)


