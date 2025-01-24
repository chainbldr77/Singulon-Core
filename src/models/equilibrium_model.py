import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout

class EquilibriumModel:
    def __init__(self):
        self.model = self._build_model()

    def _build_model(self):
        model = Sequential()
        model.add(LSTM(64, input_shape=(24, 8), return_sequences=True))
        model.add(Dropout(0.2))
        model.add(LSTM(32, return_sequences=False))
        model.add(Dense(1, activation='linear'))
        model.compile(optimizer='adam', loss='mse')
        return model

    def train(self, x_train, y_train, epochs=5):
        self.model.fit(x_train, y_train, epochs=epochs, batch_size=32)

    def predict_equilibrium(self, x_input):
        return self.model.predict(x_input).flatten().tolist()
