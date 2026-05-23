import unicodedata
from queue import Queue

def remove_diacritics(text: str):
  text = text.strip()
  if text == '':
    return ''
  # Normalize to NFD (Canonical Decomposition)
  # This separates base characters from combining marks
  nfd_form = unicodedata.normalize('NFD', text.lower())
  # Filter out combining marks (category 'Mn')
  # This removes diacritics while keeping base characters
  filtered = ''.join(
    char for char in nfd_form
    if unicodedata.category(char) != 'Mn'
  )
  # Normalize back to NFC (Canonical Composition) for consistency
  return unicodedata.normalize("NFC", filtered)

class TrieNode:
  def __init__(self):
    self.children = {}
    self.is_end_of_word = False

class Trie:
  def __init__(self):
    self.root = TrieNode()

  def collect_node(self, q: Queue, node: TrieNode = None, word: str = ''):
    for key, current_node in node.children.items():
      current_word = word + key

      if current_node.is_end_of_word:
        q.put(current_word)

      self.collect_node(q, current_node, current_word)

  def collect(self, node: TrieNode = None, word: str = '') -> list:
    if node is None:
      node = self.root

    q = Queue()
    self.collect_node(q, node, word)

    items = []
    while not q.empty():
      items.append(q.get())

    return items

  def insert(self, word):
    word = remove_diacritics(word)
    if word == '':
      return

    current_node = self.root

    for char in word:
      if char not in current_node.children:
        current_node.children[char] = TrieNode()
      current_node = current_node.children[char]

    current_node.is_end_of_word = True

  def keys_that_match(self, word):
    word = remove_diacritics(word)
    if word == '':
      return (False, None)

    match = ''
    current_node = self.root

    for char in word:
      if char not in current_node.children:
        return (False, None)

      current_node = current_node.children[char]
      match = match + char

    return (True, match) \
      if current_node.is_end_of_word \
      else (False, None)

  def keys_with_prefix(self, prefix: str):
    prefix = remove_diacritics(prefix)
    if prefix == '':
      return (False, [])

    match = ''
    current_node = self.root

    for char in prefix:
      if char not in current_node.children:
        return (False, [])

      current_node = current_node.children[char]
      match = match + char

    matches = self.collect(current_node, match)
    return (True, matches)

  def longest_prefix_of(self, prefix: str):
    prefix = remove_diacritics(prefix)
    if prefix == '':
      return (False, None)

    match = ''
    current_node = self.root

    has_any_match = False
    for char in prefix:
      if char not in current_node.children:
        if has_any_match:
          return (True, match)
        break

      has_any_match = True
      current_node = current_node.children[char]
      match = match + char

    return (True, match) \
      if has_any_match \
      else (False, None)

def sample_trie() -> Trie:
  trie = Trie()

  trie.insert('apple')
  trie.insert('app')

  trie.insert('strawberry')
  trie.insert('stream')
  trie.insert('STREAMLINE')

  trie.insert('orange')
  trie.insert('order')
  trie.insert('ORGANIZATION')

  trie.insert('banana')
  trie.insert('bank')

  trie.insert('lemon')
  trie.insert('lemonade')

  # strings with diacritics
  trie.insert('café')
  trie.insert('calendário')
  trie.insert('joão')
  trie.insert('JÚLIO')
  trie.insert('naïve')

  return trie

if __name__ in '__main__':
  trie = sample_trie()

  print(trie.collect())
  # ['app', 'apple', 'strawberry', 'stream', 'streamline', 'orange', 'order', 'organization', 'banana', 'bank', 'lemon', 'lemonade', 'cafe', 'calendario', 'joao', 'julio', 'naive']

  # starting from the 'a' node
  print(trie.collect(trie.root.children['a'], 'a'))
  # ['app', 'apple']

  print(trie.keys_that_match(''))
  # (False, None)
  print(trie.keys_that_match('BANANA'))
  # (True, 'banana')
  print(trie.keys_that_match('anything'))
  # (False, None)
  print(trie.keys_that_match('orange'))
  # (True, 'orange')

  print(trie.keys_with_prefix(''))
  # (False, [])
  print(trie.keys_with_prefix('AP'))
  # (True, ['app', 'apple'])
  print(trie.keys_with_prefix('or'))
  # (True, ['orange', 'order', 'organization'])
  print(trie.keys_with_prefix('ca'))
  # (True, ['cafe', 'calendario'])
  print(trie.keys_with_prefix('jú'))
  # (True, ['julio'])
  print(trie.keys_with_prefix('ufo'))
  # (False, [])

  print(trie.longest_prefix_of('cafeteria'))
  # (True, 'cafe')
  print(trie.longest_prefix_of('cama'))
  # (True, 'ca')
  print(trie.longest_prefix_of(''))
  # (False, None)
  print(trie.longest_prefix_of('ufo'))
  # (False, None)
