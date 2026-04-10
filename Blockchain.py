'''
This class defines the structure of a block, including its index, previous hash, timestamp, data, nonce, and hash value.
The `calculate_hash` method computes the hash of the block using SHA-256, and the `__str__` 
method provides a string representation of the block for easy visualization.
Note: The `hashlib` library is used for hashing, so make sure to import it at the beginning of your code.
'''

import time
import hashlib

class Block:
    def __init__(self, index, previous_hash, timestamp, data, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce
        self.hash = self.calculate_hash()
 
    def calculate_hash(self):
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()
 
    def __str__(self):
        return f"Block(Index: {self.index}, Hash: {self.hash}, Prev: {self.previous_hash}, Data: {self.data})"
    
'''
This class initializes the blockchain, adds new blocks, 
and implements a proof-of-work (PoW) function to simulate the mining process.
The `add_block` method creates a new block with the provided data, 
mines it using the `proof_of_work` method, and appends it to the chain.
The `proof_of_work` method iteratively increments the nonce until it finds a hash that meets the specified difficulty 
(i.e., a hash that starts with a certain number of leading zeros).
The `is_chain_valid` method checks the integrity of the blockchain by verifying that each block's
'''
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
 
    def create_genesis_block(self):
        return Block(0, "0", time.time(), "Genesis Block")
 
    def get_latest_block(self):
        return self.chain[-1]
 
    def add_block(self, data):
        latest_block = self.get_latest_block()
        new_block = Block(
            index=latest_block.index + 1,
            previous_hash=latest_block.hash,
            timestamp=time.time(),
            data=data
        )
        new_block = self.proof_of_work(new_block)
        self.chain.append(new_block)
 
    def proof_of_work(self, block, difficulty=4):
        required_prefix = "0" * difficulty
        while not block.hash.startswith(required_prefix):
            block.nonce += 1
            block.hash = block.calculate_hash()
        print(f"Block mined: {block.hash}")
        return block
 
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
 
            if current_block.hash != current_block.calculate_hash():
                print("Current block's hash is invalid!")
                return False
 
            if current_block.previous_hash != previous_block.hash:
                print("Previous block's hash is invalid!")
                return False
        return True
'''
This code demonstrates how to create a simple blockchain, add blocks with data, and validate the integrity of the blockchain.
When you run the code, it will create a blockchain, add three blocks with sample data, print the details of each block, 
and finally check if the blockchain is valid.
'''

if __name__ == "__main__":
    my_blockchain = Blockchain()
 
    # Add new blocks
    my_blockchain.add_block("Block 1 Data")
    my_blockchain.add_block("Block 2 Data")
    my_blockchain.add_block("Block 3 Data")
 
    # Print the blockchain
    for block in my_blockchain.chain:
        print(block)
 
    # Validate the blockchain
    is_valid = my_blockchain.is_chain_valid()
    print(f"Blockchain valid: {is_valid}")
