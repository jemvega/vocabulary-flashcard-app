# Vocabulary Flashcard App

## Background
I was motivated to create this app to help me to study vocabulary words for the GRE exam. It does not keep score of correct or wrong answers. Instead, it allows users to cycle through the vocabulary flash card set quickly for studying and personally assessing one's own performance. This app can be useful for anyone studying vocabulary words, math facts, or other info that can be written down on flash cards. I used a .csv for the vocabulary words because the data can be read, imported, and exported from text editors, as well as easily manipulated by Microsoft Excel and Python's Pandas.

## Prerequisites
This app was created using Jupyter Notebook for Python. The vocabulary word list is a .csv file and was created using Microsoft Excel. 

## Getting Started
This app uses three files to get started. 

First, the user must have a vocabulary word list file saved as a .csv file. In order for the app to run, the input file must be in the following format:

column1 | column2
--- | ---
word1 | definition1
word2 | definition2
word3 | definition3
... | ...

My vocabulary word list is included in the repo as a sample. 

Second, a clean up file, '<vocabulary-list-file-clean-up>' uses Python's Pandas to batch process the words and definitions from the input file into a consistent format and in alphabetical order. It also allows the user to save their cleaned file into another .csv, which can then be used as the file for the vocabulary flash card app. 

Third, the file, '<vocabulary-flash-card-app>', is an interactive program that allows the user to load the .csv for studying; to randomize the words; to choose a subset of words or all of the words to study from the list; to cycle through the word list by skipping to the next word or returning to the previous word; and, to save/mark words as unknown. The user can also quit the app at any point in time. 

## Tests
As of right now, I have only been manually testing the app. I would like to create integration test checks and unit test checks. 

## Known Issues
There are no known issues with this app. 

## Future Features
Here are some features I would like to add in the future:
* Having the app reveal only the vocabulary word while hiding the definition. A menu option will be added to allow the user to reveal the word. 
* Having a third column that includes the words in example sentences and a fourth column with synonyms and antonyms. 
* A timer so the user can see how much time passed since studying. 

## Built With

*[Python](https://www.python.org/downloads/) programming language

*[Anaconda Navigator](https://docs.anaconda.com/anaconda/navigator/) GUI

*[Microsoft Excel](https://products.office.com/en-us/home) and [Microsoft Word](https://products.office.com/en-us/home) for the .csv file

*[Notepad++](https://notepad-plus-plus.org/) for README.md and LICENSE.txt

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Authors

* **Jem Vega** - *Initial work* - [JemVega](https://github.com/JemVega)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

