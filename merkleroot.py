import hashlib

Round = 0

print()
print()
print()
# Hash pairs of items recursively until a single
#value is obtained
def merkle(hashList, ):
    global Round
    Round = Round + 1
    if len(hashList) == 1:
        print ("AND OUR MERKLE ROOT IS")
        return hashList[0]
    newHashList = []
    print()
    print ("Number of Branches in Round", Round, "is", len(hashList))
    print()
    print()
    
    # Process pairs. For odd length, last item is hashed
    #with itself
    for i in range(0, len(hashList)-1, 2):
        print ("Branch",i+1, "is", hashList[i])
        print ("Branch",i+2, "is", hashList[i+1])
        print ("their hash is", hash2(hashList[i], hashList[i+1]))
        print()
        newHashList.append(hash2(hashList[i], hashList[i+1]))
    if len(hashList) % 2 == 1: # odd, hash last item twice
        print ("Branch", len(hashList), "is", hashList[len(hashList)-1])
        print ("And Branch",len(hashList),"is hashed with itself to get", hash2(hashList[-1], hashList[-1]))
        newHashList.append(hash2(hashList[-1], hashList[-1]))
    print ("DONE with Round", Round)
    print ("<========================================================>")
    print()
    print()
    newHashList1=[x.decode('utf-8') for x in newHashList]
    return merkle(newHashList1)

def hash2(first, second):
    # Reverse inputs before and after hashing
    #due to big-endian / little-endian nonsense
    #if type(first)=='str':
    firstreverse = str(first[::-1]).encode().hex()
    secondreverse = str(second[::-1]).encode().hex()
    '''else:
      firstreverse = first.decode()
      secondreverse = second.decode()'''

    #print(firstreverse+'----'+secondreverse)
    '''h=hashlib.sha256(
        first.encode('UTF-8')+second.encode('UTF-8')).hexdigest()
                       
    print(h)'''
    
    h = hashlib.sha256((hashlib.sha256(
        first.encode('UTF-8')+second.encode('UTF-8'))
                       .hexdigest()).encode('UTF-8')).hexdigest()
    return h[::-1].encode('UTF-8')

txHashes2 = [
  "aa",
  "bb",
  "cc",
  "dd",
  "ee",
  "11",
  "22",
  "33",
  "44",
  "55",
]
print( merkle(txHashes2))