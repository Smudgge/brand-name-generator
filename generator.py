sources = ["source/source_message_broker.txt", "source/source_spooky.txt"]
good_file_name = "good.txt"
bad_file_name = "bad.txt"
min_length = 3
max_length = 8

if __name__ == '__main__':
  # Get the words.
  words = []
  for source in sources:
    with open(source, "r", encoding="utf-8") as file:
      for word in file.read().lower().split():
        words.append(word)

  # Get good words.
  with open(good_file_name, "r", encoding="utf-8") as file:
    good_words = file.read().lower().split()

  # Get bad words.
  with open(bad_file_name, "r", encoding="utf-8") as file:
    bad_words = file.read().lower().split()

  # Save good and bad words.
  def save():
    with open(good_file_name, "w", encoding="utf-8") as file:
      file.write('\n'.join(good_words))
    with open(bad_file_name, "w", encoding="utf-8") as file:
      file.write('\n'.join(bad_words))

  # Suggest a word to deside which file to go to.
  def suggest(word, amount, done):
    if good_words.__contains__(word): return False
    if bad_words.__contains__(word): return False
    print(word)
    response = input(f"({done}/{amount}) yes(y) no(n) exit(e): ").lower()
    if response == "y": good_words.append(word)
    if response == "n": bad_words.append(word)
    save()
    if response == "e": return True
    return False

  # Find words.
  def generate_words():
    generated_words = []
    for word1 in words:
      for word2 in words:
        if word1 == word2: continue
        word_generated = ''
        if word1[len(word1) - 1] == word2[0]:
          word_generated = word1 + word2[1:]
        if word2[len(word2) - 1] == word1[0]:
          word_generated = word2 + word1[1:]
        if word_generated == '': continue
        if generated_words.__contains__(word_generated): continue
        if min_length < len(word_generated) > max_length: continue
        generated_words.append(word_generated)
    return generated_words

  # Count the amount of words sorted.
  def count_words_done(words_to_count):
    done = 0
    for x in words_to_count:
      if good_words.__contains__(x): done += 1
      if bad_words.__contains__(x): done += 1
    return done

  # Main Programme
  generated = generate_words()
  for word in generated:
    if suggest(word, len(generated), count_words_done(generated)): break

  # Exit.
  print(
    '\n'
    f'{len(good_words) + len(bad_words)} words have been sorted.\n' +
    f'List length was {len(words)}.\n' +
    f'List more words in the source files for more options.'
  )
