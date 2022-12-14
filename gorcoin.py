import hashlib as hasher
import datetime as date

# Структура блока
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()
        
    def hash_block(self):
        sha = hasher.sha256()
        sha.update((str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)).encode('utf-8'))
        return sha.hexdigest()
 
 
# Создает первый блок
def create_genesis_block():
    return Block(0, date.datetime.now(), "Genesis Block", "0")
    

# Создает следующие блоки
def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "Hey! I'm block " + str(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)
    
    
# Создаем блокчейн и добавляем первый блок
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# Сколько блоков добавляем
num_of_blocks_to_add = 20

# Добавляем блоки в цикле
for i in range(0, num_of_blocks_to_add):
    block_to_add = next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add
    
    # Выводим на экран
    print("Block #{} has been added to the blockchain!".format(block_to_add.index))
    print("Hash: {}\n".format(block_to_add.hash))
