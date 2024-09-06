# Function to count words in a text file
def count_words(file_path):
    word_count = {}
    
    with open(file_path, 'r') as file:
        for line in file:
            words = line.lower().split()  # Convert to lowercase and split into words
            for word in words:
                word = word.strip('.,!?";:()[]{}')  # Remove punctuation
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
                    
    return word_count

# Provide the path to your text file
file_path = 'C:\\Users\\Acer\\Desktop\\hello.txt'

# Count words in the file
word_count = count_words(file_path)

# Print the word count
for word, count in word_count.items():
    print(f'{word}: {count}')
