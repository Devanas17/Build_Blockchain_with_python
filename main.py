import hashlib


def hashGenerator(data):
    result = hashlib.sha256(data.encode())
    return result.hexdigest()


class Block:

    def __init__(self, data, hash, prevHash):
        self.data = data
        self.hash = hash
        self.prevHash = prevHash


class Blockchain:

    def __init__(self):
        hashLast = hashGenerator('gen_last')
        hashStart = hashGenerator('gen_hash')

        genesis = Block('gen-data', hashStart, hashLast)
        self.chain = [genesis]

    def add_block(self, data):
        prevHash = self.chain[-1].hash
        hash = hashGenerator(data + prevHash)
        block = Block(data, hash, prevHash)
        self.chain.append(block)


blChain = Blockchain()
blChain.add_block('1')
blChain.add_block('2')
blChain.add_block('3')

for block in blChain.chain:
    print(block.__dict__)
