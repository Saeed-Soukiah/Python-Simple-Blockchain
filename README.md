🧱 Simple Proof‑of‑Work Blockchain in Python
A minimal blockchain implementation written in Python, demonstrating the core concepts behind decentralized ledger technology.
This project includes block creation, SHA‑256 hashing, Proof‑of‑Work mining, and full chain validation — all implemented from scratch without external dependencies.

📌 Features
Block structure with:

Index

Timestamp

Data

Nonce

Previous hash

SHA‑256 hash

Proof‑of‑Work mining  
Adjustable difficulty (default: 4 leading zeros)

Genesis block creation

Automatic block linking  
Each block references the hash of the previous one

Blockchain validation  
Ensures:

Hash integrity

Correct previous hash linkage

Readable block output using __str__

📂 Project Structure
Code
/your-repo
│
├── blockchain.py   # Main blockchain implementation
├── README.md       # Project documentation
└── (optional) examples, tests, etc.
🚀 Getting Started
1. Clone the repository
bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2. Run the blockchain
bash
python blockchain.py
🧪 Example Output
When running the script, you will see:

Blocks being mined

Their hashes

The full chain printed

A final validation check

Example:

Code
Block mined: 0000a3f9...
Block mined: 0000c1b2...
Block mined: 0000f9d4...

Block(Index: 0, Hash: ..., Prev: 0, Data: Genesis Block)
Block(Index: 1, Hash: ..., Prev: ..., Data: Block 1 Data)
Block(Index: 2, Hash: ..., Prev: ..., Data: Block 2 Data)
Block(Index: 3, Hash: ..., Prev: ..., Data: Block 3 Data)

Blockchain valid: True
🛠 How It Works
Block Class
Each block contains:

Index

Previous block hash

Timestamp

Data

Nonce

Its own SHA‑256 hash

The hash is computed from all fields, ensuring immutability.

Blockchain Class
Handles:

Genesis block creation

Adding new blocks

Mining via Proof‑of‑Work

Validating the entire chain

Proof‑of‑Work
The miner increments the nonce until the hash starts with a required number of zeros:

Code
difficulty = 4  →  hash must start with "0000"
This simulates real blockchain mining.

🔒 Blockchain Validation
The chain is considered valid if:

Every block’s stored hash matches its recalculated hash

Every block’s previous_hash matches the hash of the block before it

If any block is tampered with, validation fails.

📘 Use Cases
This project is ideal for:

Learning blockchain fundamentals

Academic assignments

Demonstrating PoW concepts

Building more advanced blockchain systems

📈 Future Improvements (Optional)
You can extend this project with:

Merkle trees

Peer‑to‑peer networking

Wallets & digital signatures

Transaction pools

Dynamic difficulty adjustment

Persistent storage
