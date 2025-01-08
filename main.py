import collections

def count_characters(text):
    # Convert text to lowercase
    text = text.lower()
    # Count the frequency of each character
    character_count = collections.Counter(text)
    return character_count

def generate_report(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    
    # Count words
    word_count = len(file_contents.split())
    
    # Count characters
    character_count = count_characters(file_contents)
    
    # Generate report
    report = f"--- Begin report of {file_path} ---\n"
    report += f"{word_count} words found in the document\n\n"
    
    for char, count in character_count.items():
        if char.isalpha():  # Only include alphabetic characters
            report += f"The '{char}' character was found {count} times\n"
    
    report += "--- End report ---"
    
    return report

# Generate and print the report
file_path = 'books/frankenstein.txt'
print(generate_report(file_path))
