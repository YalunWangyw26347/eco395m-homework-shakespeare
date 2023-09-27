import csv
import os
import re

INPUT_DIR = os.path.join("data", "shakespeare")
STOPWORDS_PATH = os.path.join(INPUT_DIR, "stopwords.txt")
SHAKESPEARE_PATH = os.path.join(INPUT_DIR, "shakespeare.txt")
OUTPUT_DIR = "artifacts"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "shakespeare_report.csv")

NUM_LINES_TO_SKIP = 246
LAST_LINE_START = "End of this Etext"


def load_stopwords():
    """Load the stopwords from the file and return a set of the cleaned stopwords."""

    stopwords = set()
    with open (STOPWORDS_PATH) as sw:
        for line in sw:
            words=line.strip()  
            stopwords.add(words)
    #print(stopwords)
    # fill this in
#print(load_stopwords())    
    return stopwords


def load_shakespeare_lines():
    "Loads every line in the dataset that was written by Shakespeare as a list of strings."
    should_read = True 
    shakespeare_lines = []
    
    with open(SHAKESPEARE_PATH) as sp:
        for i in range (NUM_LINES_TO_SKIP):
            sp.readline()

        for line in sp:
    
            newline=line.strip()
                
            if "<<" in newline:
                should_read= False
            if LAST_LINE_START in newline:
                should_read= False
            if should_read == True:
                clean_text = re.sub('[^A-Za-z\s]', '', newline)
                text_with_only_spaces = re.sub("\s+", " ", clean_text)   
                shakespeare_lines.append(text_with_only_spaces)        
            if ">>"  in newline:
                should_read= True
                   
    return shakespeare_lines

#print(load_shakespeare_lines())



def get_shakespeare_words(shakespeare_lines):
    """Takes the lines and makes a list of lowercase words."""
    words=[]
    for i in shakespeare_lines:
        wordss=i.split()
        for n in wordss:
            newword=n.lower()
            words.append(newword)
    #print(words)
    return words



def count_words(words, stopwords):
    """Counts the words that are not stopwords.
    returns a dictionary with words as keys and values."""
    word_counts = dict()
    for i in words:
        if i not in stopwords:
            word_counts[i]=word_counts.get(i,0)+1
    #print(word_counts)
    return word_counts



def sort_word_counts(word_counts):
    """Takes a dictionary or word counts.
    Returns a list of (word, count) tuples that are sorted by count in descending order."""
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    # fill this in
    #print(sorted_word_counts)
    return sorted_word_counts


def write_word_counts(sorted_word_counts, path):
    """Takes a list of (word, count) tuples and writes them to a CSV."""
    #print(len(sorted_word_counts))
    with open(OUTPUT_PATH,'w') as f:
        csv_writer= csv.writer(f)
        csv_writer.writerow(['word', 'count'])
        for i in range(len(sorted_word_counts)):
            csv_writer.writerow(sorted_word_counts[i])


if __name__ == "__main__":

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    stopwords = load_stopwords()

    shakespeare_lines = load_shakespeare_lines()
    shakespeare_words = get_shakespeare_words(shakespeare_lines)

    word_counts = count_words(shakespeare_words, stopwords)
    word_counts_sorted = sort_word_counts(word_counts)

    write_word_counts(word_counts_sorted, OUTPUT_PATH)
