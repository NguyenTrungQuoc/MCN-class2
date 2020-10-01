class Prefixcodetree:
  def __init__(self):
    # thiet lap mang cay nhi phan
    self.tree = [0]*1000
  def insert(self,codeword,symbol):
    #tim muc cua tu ma
    index=0
    for element in codeword:
      if element == 1:
        index = index * 2 + 2
      elif element == 0:
        index = index * 2 + 1
    #gan bieu tuong vao cay[index]
    self.tree[index]=symbol

  def decode(self,encodedData, datalen):
    # gan gia tri ban dau
    result=""
    index=0
    # chuyen doi du lieu ma hoa
    data=""
    for byte in encodedData:
      data += f'{byte:0>8b}'
    #bat dau giai ma
    for i in range(datalen):
      char = data[i]
      if char == '1':
        index = index * 2 + 2
      elif char == '0':
        index = index * 2 + 1
      #neu thay bieu tuong thi them ket qua
      if self.tree[index] != 0:
        result += " " + self.tree[index]
        index=0
    return result

codeTree = PrefixCodeTree()
codebook = {
'x1': [0],
'x2': [1,0,0],
'x3': [1,0,1],
'x4': [1,1]
}
for symbol in codebook:
  codeTree.insert(codebook[symbol], symbol)
message = codeTree.decode(b'\xd2\x9f\x20', 21)
print(message)