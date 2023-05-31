# Assignment5-selfAssigned-comparison between LOTR and fan fiction using spaCy
This is the fifth and last assignment of the five in the Language Analytics course. It is also the self assigned one.

# Contribution
This assignment was made independently by myself without any help from fellow students. However, the sctipt called _make_data.py_ takes a lot of inspiration from the following [GitHub repository](https://github.com/radiolarian/AO3Scraper.git) in terms of setting up a pipeline that can scrape from _Archive of Our Own_. In fact, chunks of code from the repository was copied and then rewritten for my specific purpose. This is because it was completely new for me to scrape text data from a fan fiction archive like  _Archive of Our Own_. In terms of generating the pipeline that processes the data using ```spaCy```, i consulted the notebooks from class as well as my work in assignment 1 since there are some similarities. For this assignment, i also sought inspiration in terms of finetuning my visualization skills with ```matplotlib```, so i used the following [tutorial](https://www.geeksforgeeks.org/bar-plot-in-matplotlib/) to make my output more interpretable.

# Motive
This assignment seeks to track difference in use of word classes between _The Lord of The Rings_ trilogy and a fan fiction called [_Comes Around Again_](https://archiveofourown.org/works/2064171/chapters/4487058). They are almost similar in length. Before creating the code and gettig the output plot showcasing the relative frequencies of POS between the two stories, i had a hypothesis that the fan fiction would have a more abundant use of adjectives and adverbs, but that was in fact not the case. I will touch upon this in the "Discussion of results" section further down. My personal motive for this assignment is rooted in my background of literatute and linguistics courses from the English department at Aarhus University. 

# Data
There are two datasets used for this assignment. The script _make_data.py_ creates the first dataset as it runs. This is the _Comes Around Again_ fan fiction story from _Archive of Our Own_. As the script is run, all the chapters of the story will be scraped to the _in_ folder. Then it is concatenated into a combined .txt file with all the chapters together called _ult_data.txt_. The other dataset used for this assignment is the _The Lord of The Rings_ trilogy, which can be acessed through the following [Kaggle link](https://www.kaggle.com/datasets/ashishsinhaiitr/lord-of-the-rings-text). The dataset is provided by Kaggle user  Ashishsinha. It is a zip file that contains the three books as .txt files. 

# Packages
I used a bigger variety of packages for this assignment since both the script are fairly long and require a lot of tools to work
* ```os``` is used to navigate paths
* ```requests``` is used for requesting to download the fan fiction _Archive of Our Own_
* ```BeautifulSoup``` is used for pulling the scraped data out of HTML formats
* ```zipfile``` is used to unzip the LOTR data 
* ```spaCy``` is used for POS tagging of the two texts
* ```numPy``` is used for arranging in the plotting function
* ```pandas``` is used to create a dataframe that is saved as a CSV 
* ```matplotlib``` is used for the sake of plotting a bar plot

# Methods
This assignment consists of two scripts. The first you have to run is the _make_data.py_ script which starts by unzipping the LOTR texts in the _LOTR_ folder within the _in_ folder. Then it proceeds with a pipeline that uses ```requests``` to obtain permission to download the text from _Archive of Our Own_. The pipeline for this was, as i mentioned above, heavily influenced by the following [GitHub repository](https://github.com/radiolarian/AO3Scraper.git). After each chapter is scraped to the _in_ folder, the script proceeds to concatenate all the 34 chapters into a single .txt file called _ult_data.txt_. This is the .txt file that is used for POS tagging in the second script. 
The second script, _POC_tag.py_, is the script that processes the data using ```spaCy``` and calculates relative frequencies of nouns, verbs, adjectives and adverbs for both the .txt's. It starts off by processing the fanfiction data by assigning it to the ```"en_core_web_md"``` English language model from ```spaCy```. Then the script does the same for the LOTR .txt's however, it also combines the three .txt's into a single long concatenated version of the LOTR trilogy called _LOTR_full.txt_. Then the script calculates the relative frequencies of the chosen POS for buth of the .txt. It calculates the relative frequencies per 10000 words. It then runs a function that utilizes ```pandas``` in order to create a dataframe that contains the relative frequencies for both the datasets. It saves the dataframe as a CSV to the folder called _out_. Then the plotting function is run using ```matplotlib```'s ```plt.bar()``` function. I set the parameters that makes the outout interpretable. This being an informative legend, assigning different colours to the two dataset and making legends for each bar containing the exact relative frequency. The plot is saved to the _out_ folder.

# Discussion of results
As i mentioned earlier, i had initially thought that there would be a more frequent use of adjectives and adverbs in the fan fiction, but this is not the case with the data i used at least. My common sense and my knowledge of literature from my English minor tells me that fan fictopn usually woudl rely on more descriptive language using many adjectives and adverbs. However from the results of this assignment, i have figured that in the case of LOTR vs fanfiction it isnt necessarily always the case. In fact, the more abundant use of nouns and verbs in the fan fiction implies that the style of writing is more direct and has more intensity than the language of Tolkiens LOTR. This does make sense since Tolkien puts heavy emphasis on world building and description of characters, mood and environment using an abundance of adjectives and adverbs. It is possible to change the scraped data input URL for this pipeline in order to test the POS comparison on another fan fiction story of the same scale as _Comes Around Again_. That might be for future entertainment!

# Usage
* First you need to acquire the LOTR data from the following [Kaggle lin](https://www.kaggle.com/datasets/ashishsinhaiitr/lord-of-the-rings-text) and place the zip file in the _LOTR_ folder within the _in_ folder. 
* Run ```bash setup.sh``` from the command line to install requirements and create a virtual environment
* Run ```source ./assignment5_env/bin/activate```  to activate the virtual environment
* Now run the _make_data.py_ script in order to scrape the fan fiction and unzip the LOTR data: ```python3 src/make_data.py```
* Now run the POS tagging script: ```python3 src/POC_tag.py```
* The outputs of the script are located in the _out_ folder
