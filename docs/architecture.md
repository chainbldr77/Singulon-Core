# Architecture

### 1. Data Layer
- Pulls on-chain data from Solana RPC endpoints.
- Fetches relevant sentiment data (if Twitter API is configured).

### 2. AI Layer
- **Equilibrium Model** (LSTM-based or Transformer-based model for tokenomics).
- **Trend Predictor** (analyzes short-term swings).
- **Advanced Transformer** (special module for deeper historical analysis).

### 3. Node Layer
- Each node runs Singulon’s code.
- Nodes communicate encrypted actions, proposals, and consensus updates.
- Anchor smart contract enforces trustless governance and fund movements.

