import numpy as np
from src.models.equilibrium_model import EquilibriumModel

def test_equilibrium_model():
    model = EquilibriumModel()
    x_input = np.random.rand(1, 24, 8)
    output = model.predict_equilibrium(x_input)
    assert len(output) == 1  # Expecting a single float output
