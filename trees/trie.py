class TrieNode:
  def __init__(self):
    self.children = {}
    self.is_end_of_word = False

class Trie:
  def __init__(self):
    self.root = TrieNode()
  
  def insert(self, word):
    current_node = self.root
    for char in word:
      if char not in current_node.children:
        current_node.children[char] = TrieNode()
      current_node = current_node.children[char]
    current_node.is_end_of_word = True
  
  def search(self, word):
    current_node = self.root
    for char in word:
      if char not in current_node.children:
        return False
      current_node = current_node.children[char]
    return current_node.is_end_of_word

  def starts_with(self, prefix):
    current_node = self.root
    for char in prefix:
      if char not in current_node.children:
        return False
      current_node = current_node.children[char]
    return True

if __name__ in '__main__':
  trie = Trie()
  
  trie.insert('apple')
  trie.insert('orange')
  trie.insert('strawberry')
  trie.insert('app')
  trie.insert('banana')
  trie.insert('lemon')

  print(trie.search('banana'))
  # True

  print(trie.search('ap'))
  # False

  print(trie.starts_with('ap'))
  # True

  print(trie.search('orange'))
  # True
