from datetime import datetime
import hashlib as hasher
import random
import decimal
import time
from datetime import date
#Done by newklear December 2019
#Blockchain simulation writing to a text file and using 'User Input' Mining Difficulty Crypto Currency amounts as data fillers
#Each time the script is run, the data is saved in data.txt and seperated by start time and date.

print("\t-----Automated BlockChain Generator-----")
noBlocks = input("Enter number of Blocks to create in the BlockChain: ")
mineDiff = input("Enter Mining Difficulty level eg. 1-10/100/100/1000/10000 etc: ")

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def __str__(self):
        return 'Block #{}'.format(self.index)

    def hash_block(self):
        sha = hasher.sha256()
        seq = (str(x) for x in (
               self.index, self.timestamp, self.data, self.previous_hash))
        sha.update(''.join(seq).encode('utf-8'))
        return sha.hexdigest()


def make_genesis_block():
    """Make the first block in a block-chain."""
    block = Block(index=0,
                  timestamp=datetime.now(),
                  data="Genesis Block",
                  previous_hash="0")
    return block


def next_block(last_block, data=''):
    """Return next block in a block chain."""
    idx = last_block.index + 1
    block = Block(index=idx,
                  timestamp=datetime.now(),
                  data='{}{}'.format(data, idx),
                  previous_hash=last_block.hash)
    return block


def build_blockchain():
    """Build the predetermined amount of blocks."""
    blockchain = [make_genesis_block()]
    prev_block = blockchain[0]
    global total
    total = 0
    for _ in range(0, int(noBlocks)):
        amount = decimal.Decimal(random.randrange(30, 300))/int(mineDiff)
        total += amount
        block = next_block(prev_block, data='blah blah')
        blockchain.append(block)
        prev_block = block
        with open('data.txt', 'a') as file:
            file.write(str('\n{} added to blockchain\n'.format(block)))
            file.write(str('Hash: {}\n'.format(block.hash)))
            file.write(str('Crypto Currency Amount: ' + str(f'{amount:.8f}\n')))
        print('{} added to blockchain'.format(block))
        print('Hash: {}'.format(block.hash))
        print('Crypto Currency Amount:', f'{amount:.8f}\n')

today = str(date.today())
now = datetime.now()
current = str(now.strftime("%H:%M:%S"))
with open('data.txt', 'a') as file:
    file.write('Blockchain by newklear 2019 Initiated: ' + today)
    file.write('\nAutomated process of mining commenced: ' + current)
    file.write('\n')
start = time.time()
# run the test code
build_blockchain()
final = time.time() - start
print()
print("Blockchain took", f'{final:.2f}', "seconds to build.")
print('Total CryptoCurrency Mined:', f'{total:.8f}', 'Average Mined per Block:', int(total)/int(noBlocks))
with open('data.txt', 'a') as file:
    file.write('\n')
    file.write('Blockchain took: ' f'{final:.2f}' 'seconds to build.')
    file.write('\nTotal CryptoCurrency Mined:' f'{total:.8f}')