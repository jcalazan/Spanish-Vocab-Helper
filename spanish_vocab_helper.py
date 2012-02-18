import sys
import csv
import random

def get_wordlist(filepath):
    wordlist = {}
    try:
        with open(filepath, 'rb') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                wordlist['%s' % row[0].strip().lower()] = \
                '%s' % row[1].strip().lower()
    except IOError:
        print "\nCould not open %s!\nExiting..." % filepath
        sys.exit(1)
    return wordlist

def get_answer(english_word, wordlist):
    print "\n[%s word(s) remaining]" % len(wordlist.items())
    print "\nEnglish: %s" % english_word
    return raw_input('Spanish: ').strip().lower()

def get_option():
    print "\n[1] Try again.\n[2] Show answer."
    return raw_input("\nEnter option number: ").strip().lower()

if __name__ == '__main__':
    wordfile = raw_input('\nPlease enter the path of the word list file: ')
    wordlist = get_wordlist(wordfile.strip().lower())
    
    # Shuffle the dictionary keys so the objects will be displayed
    # in random order to the user.
    keys = wordlist.keys()
    random.shuffle(keys)
    
    # Keep track of incorrect answers here.
    missed_words = {}
    
    # Pretty ugly for loop. Should refactor later (ok, I confess, I probably
    # won't get to it).
    for key in keys:
        def handle_correct_answer():
            print "\nCorrecto!"
            wordlist.pop(key)
            
        def handle_incorrect_answer():
            print "\nIncorrecto!"

        if get_answer(wordlist[key], wordlist) == key:
            handle_correct_answer()
        else:
            handle_incorrect_answer()
            while True:
                option = get_option()
                if option == '1':
                    if get_answer(wordlist[key], wordlist) == key:
                        handle_correct_answer()
                        break
                    handle_incorrect_answer()
                elif option == '2':
                    print "\nThe correct answer is '%s'" % key.upper()
                    missed_words[key] = wordlist[key]
                    wordlist.pop(key)
                    break
                else:
                    print "\nInvalid option, amigo! Put down the cerveza."
    
    # Display words that were missed and the answers.
    if missed_words:
        print "\nBelow are the word(s) that you missed.\n"
        for key, value in missed_words.items():
            print "%s - %s" % (key.upper(), value)
            