filename = input("Enter file name: ")

def analyze_file(filename):
    # Open the file in read mode
    with open(filename, 'r') as file:
        # Read the content of the file
        content = file.read()
    
    # Calculate the total number of lines
    lines = content.split('\n')
    total_lines = len(lines)

    # Calculate the total number of words
    words = content.split()
    total_words = len(words)

    # Calculate total number of characters
    character_total = len(content)

    # Calculate the most frequent word
    word_count = {}

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    max_frequency = max(word_count.values())
    most_frequent_words = [word for word, count in word_count.items() if count == max_frequency]

    # Print the file analysis report
    print("\n--- File Analysis Report ---")
    print("Total number of lines:", total_lines)
    print("Total number of words:", total_words)
    print("Total number of characters:", character_total)
    print("Most frequent word(s):")
    for word in most_frequent_words:
        print(f'- "{word}" occurs {word_count[word]} times')


analyze_file(filename)