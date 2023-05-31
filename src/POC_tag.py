import os
import spacy
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Creating a function processes the fanfiction data 
def process_fanfiction():
    # Loading the spaCy English language model
    nlp = spacy.load("en_core_web_md")
    # Increasing the max_length limit of characters to fit the size of the data
    nlp.max_length = 2000000
    # Defining filepath to concatenated chapters   
    fan_file_path = os.path.join(".", "in", "ult_data.txt")
    with open(fan_file_path, "r") as file: # "writing" the text to the desired location
        text = file.read()
    # Assigning the language model to the fanfiction
    fan = nlp(text)
    
    return fan

# Creating function that combines the 3 books to 1 single text and assigning the language model to it
def process_LOTR():
    # Loading the spaCy English language model
    nlp = spacy.load("en_core_web_md")
    # Increasing the max_length limit
    nlp.max_length = 2600000  
    
    # Folder path containing input files
    input_folder = os.path.join(".", "in", "LOTR") 
    # List of input file names
    input_files = ["01 - The Fellowship Of The Ring.txt", "02 - The Two Towers.txt", "03 - The Return Of The King.txt"]  
    # Output file name
    output_file = "LOTR_full.txt"  
    # Defining output path for the conbined .txt
    output_path = os.path.join(".", "in", "LOTR", output_file)
    # Opens the output path file as writeable
    with open(output_path, "w", encoding="utf-8") as outfile:
        # For files in the input files
        for input_file in input_files:
            # Assigning input path
            input_path = os.path.join(input_folder, input_file)
            # Opens the specified file in read mode
            with open(input_path, "r", encoding="latin-1") as infile:
                # Reading the content of the infile and writes it to the output file
                outfile.write(infile.read())
    # Assigning path to the full LOTR text
    LOTR_file_path = os.path.join(".", "in", "LOTR", "LOTR_full.txt")

    with open(LOTR_file_path, "r") as file: # "writing" the text to the desired location
        text = file.read()
    # Assigning the language model to the fanfiction
    LOTR = nlp(text)
    
    return LOTR

# Creating function that counts the amount of POS and the relative frequency of them per 10000 words for the fanfiction
def relfreq_fan(fan):
    # Assigning the count of word classes to a zero before counting them with the following for loop
    noun_count_fan = 0
    adjective_count_fan = 0
    verb_count_fan = 0
    adverb_count_fan = 0

    for token in fan: # for every token in doc
        if token.pos_ == "NOUN": # If token is a noun 
            noun_count_fan += 1 # Add 1 to the count
        elif token.pos_ == "ADJ": # The next lines of code carries on with the same principle
            adjective_count_fan += 1
        elif token.pos_ == "VERB":
            verb_count_fan += 1
        elif token.pos_ == "ADV":
            adverb_count_fan += 1

    # Calculating the relative frequency of each word class and rounding to the amount of desired decimals
    relative_freqN_fan = (noun_count_fan / len(fan)) * 10000
    relative_freqN_fan = round(relative_freqN_fan, 2)
    relative_freqAdj_fan = (adjective_count_fan / len(fan)) * 10000
    relative_freqAdj_fan = round(relative_freqAdj_fan, 2)
    relative_freqV_fan = (verb_count_fan / len(fan)) * 10000
    relative_freqV_fan = round(relative_freqV_fan, 2)
    relative_freqAdv_fan = (adverb_count_fan / len(fan)) * 10000
    relative_freqAdv_fan = round(relative_freqAdv_fan, 2)

    return relative_freqN_fan, relative_freqAdj_fan, relative_freqV_fan, relative_freqAdv_fan

# Creating function that counts the amount of POS and the relative frequency of them per 10000 words for the LOTR .txt
def relfreq_LOTR(LOTR):
    # assigning the count of word classes to a zero before counting them with the following for loop
    noun_count_LOTR = 0
    adjective_count_LOTR = 0
    verb_count_LOTR = 0
    adverb_count_LOTR = 0

    for token in LOTR: # for every token in doc
        if token.pos_ == "NOUN": # If token is a noun 
            noun_count_LOTR += 1 # Add 1 to the count
        elif token.pos_ == "ADJ": # The next lines of code carries on with the same principle
            adjective_count_LOTR += 1
        elif token.pos_ == "VERB":
            verb_count_LOTR += 1
        elif token.pos_ == "ADV":
            adverb_count_LOTR += 1

    # Calculating the relative frequency of each word class and rounding to the amount of desired decimals
    relative_freqN_LOTR = (noun_count_LOTR / len(LOTR)) * 10000
    relative_freqN_LOTR = round(relative_freqN_LOTR, 2)
    relative_freqAdj_LOTR = (adjective_count_LOTR / len(LOTR)) * 10000
    relative_freqAdj_LOTR = round(relative_freqAdj_LOTR, 2)
    relative_freqV_LOTR = (verb_count_LOTR / len(LOTR)) * 10000
    relative_freqV_LOTR = round(relative_freqV_LOTR, 2)
    relative_freqAdv_LOTR = (adverb_count_LOTR / len(LOTR)) * 10000
    relative_freqAdv_LOTR = round(relative_freqAdv_LOTR, 2)

    return relative_freqN_LOTR, relative_freqAdj_LOTR, relative_freqV_LOTR, relative_freqAdv_LOTR

# Creating function that saves a CSV to the "out" folder
def create_csv(fan, LOTR, output_folder, output_file):
    # Creating a DataFrame
    rel_freq_data = {
        "Story": ["Fanfiction", "LOTR"],
        "RelfreqNoun": [fan[0], LOTR[0]],
        "RelfreqAdjective": [fan[1], LOTR[1]],
        "RelfreqVerb": [fan[2], LOTR[2]],
        "RelfreqAdverb": [fan[3], LOTR[3]]
    }
    # Making the dataframe above into a pandas dataframe
    df = pd.DataFrame(rel_freq_data)
    # Assigning the output path of the CSV
    output_path = os.path.join(output_folder, output_file)
    # No index column
    df.to_csv(output_path, index=False)

# Creating function that plots the relative frequencies for both texts in the same plot
def plot_relative_freq(fan, LOTR, output_folder):
    # Data for plotting
    categories = ["Noun", "Adjective", "Verb", "Adverb"]
    fan_freq = fan[:4]
    LOTR_freq = LOTR[:4]

    # Setting the bar width
    bar_width = 0.35
    # Setting the positions of the bars on the x-axis
    r1 = np.arange(len(fan_freq))
    r2 = [x + bar_width for x in r1]

    # Creating the bar plot and assigning colors and labels of the two bars
    plt.bar(r1, fan_freq, color='b', width=bar_width, label='Fanfiction')
    plt.bar(r2, LOTR_freq, color='g', width=bar_width, label='LOTR')

    # Setting plot title and labels
    plt.title("Relative Frequencies Comparison")
    plt.xlabel("POS")
    plt.ylabel("Relative Frequency")
    plt.xticks([r + bar_width/2 for r in range(len(fan_freq))], categories)

    # Adding labels to the bars
    for i, freq in enumerate(fan_freq):
        plt.text(r1[i], freq, str(freq), ha='center', va='bottom')
    for i, freq in enumerate(LOTR_freq):
        plt.text(r2[i], freq, str(freq), ha='center', va='bottom')
    # Adding legend
    plt.legend(loc='upper right')

    # Saving the plot as a file
    outpath = os.path.join(output_folder, "relative_frequencies_plot")
    plt.savefig(outpath)

def main():
    # Processing the fanfiction data
    fan = process_fanfiction()
    # Processing the LOTR data
    LOTR = process_LOTR()
    # Calculating relative frequencies for fanfiction
    fan_results = relfreq_fan(fan)
    # Calculating relative frequencies for LOTR
    LOTR_results = relfreq_LOTR(LOTR)
    # Creating the CSV file
    output_folder = "./out"
    output_file = "relative_frequencies.csv"
    create_csv(fan_results, LOTR_results, output_folder, output_file)
    # Creating the comparative plot
    plot_relative_freq(fan_results, LOTR_results, output_folder)

if __name__ == "__main__":
    main()

