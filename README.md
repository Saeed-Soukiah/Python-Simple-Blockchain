# 🧱 Simple Proof‑of‑Work Blockchain in Python

A minimal blockchain implementation written in Python, demonstrating the core concepts behind decentralized ledger technology.  
This project includes block creation, SHA‑256 hashing, Proof‑of‑Work mining, and full chain validation — all implemented from scratch without external dependencies.

---

## 📌 Features

- **Block structure** with:
  - Index  
  - Timestamp  
  - Data  
  - Nonce  
  - Previous hash  
  - SHA‑256 hash  
- **Proof‑of‑Work mining** (difficulty‑based)
- **Genesis block creation**
- **Automatic block linking**
- **Blockchain validation**
- **Readable block output**

---

## 📂 Project Structure

```
/your-repo
│
├── blockchain.py   # Main blockchain implementation
└── README.md       # Documentation
```

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Run the blockchain
```bash
python blockchain.py
```

---

## 🧪 Example Output

```
Block mined: 0000a3f9...
Block mined: 0000c1b2...
Block mined: 0000f9d4...

Block(Index: 0, Hash: ..., Prev: 0, Data: Genesis Block)
Block(Index: 1, Hash: ..., Prev: ..., Data: Block 1 Data)
Block(Index: 2, Hash: ..., Prev: ..., Data: Block 2 Data)
Block(Index: 3, Hash: ..., Prev: ..., Data: Block 3 Data)

Blockchain valid: True
```

---

## 🛠 How It Works

### Block Class
Each block contains:
- Index  
- Previous hash  
- Timestamp  
- Data  
- Nonce  
- SHA‑256 hash  

The hash is computed from all fields, ensuring immutability.

### Blockchain Class
Handles:
- Genesis block creation  
- Adding new blocks  
- Mining via Proof‑of‑Work  
- Validating the entire chain  

### Proof‑of‑Work
The miner increments the nonce until the hash starts with a required number of zeros:

```
difficulty = 4  →  hash must start with "0000"
```

---

## 🔒 Blockchain Validation

The chain is valid if:

1. Each block’s stored hash matches its recalculated hash  
2. Each block’s `previous_hash` matches the hash of the block before it  

Any tampering breaks the chain.

---

## 📘 Use Cases

- Learning blockchain fundamentals  
- Academic assignments  
- Demonstrating PoW concepts  
- Building more advanced blockchain systems  

---

## 📈 Future Improvements

- Merkle trees  
- P2P networking  
- Wallets & digital signatures  
- Transaction pools  
- Dynamic difficulty  
- Persistent storage  
