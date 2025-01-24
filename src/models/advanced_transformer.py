import tensorflow as tf
from tensorflow.keras import layers, Model

class AdvancedTransformer(Model):
    """
    A simplified Transformer-like architecture for deeper historical analysis
    of on-chain data. 
    """

    def __init__(self, embed_dim=64, num_heads=4, ff_dim=128, num_transformer_blocks=2):
        super(AdvancedTransformer, self).__init__()
        self.embedding = layers.Dense(embed_dim)
        self.transformer_blocks = [
            tf.keras.layers.TransformerBlock(embed_dim, num_heads, ff_dim) 
            for _ in range(num_transformer_blocks)
        ]
        self.flatten = layers.Flatten()
        self.out_layer = layers.Dense(1, activation='linear')

    def call(self, inputs):
        x = self.embedding(inputs)
        for block in self.transformer_blocks:
            x = block(x)
        x = self.flatten(x)
        return self.out_layer(x)
