# trump-reg

## Installation

Simply download the master zip file of our code. Navigate to the root folder and open the `Algorithm` folder. 

## Dependencies

If you do not have the dependencies listed below already installed, you will need to do so before our code will be able to run on your computer.

> `pip install textblob`

> `pip install xlrd`

> `python -m textblob.download_corpora`

## Running the Code

To run the code simply type `python TheHorsesMouth.py`

## Description of Algorithm

Right now our algorithm takes in Trump's tweets and calls an external library that labels each word with a part of speech and puts each word in a specific part of speech dictionary. We also keep track of the sentence structure of each tweet. Each time the program is run a sentence structure is chosen at random and each part of speech in the structure is filled in with a word that Trump has said that is that part of speech. We are currently taking the top 1/5 of words and choosing one at random to insert. We then output our predicted Trump tweet.

## Sample output 

> my favorite has to be in MakeAmericaGreatAgain no realDonaldTrump lies fired AGAIN

> He ever be his @ noon TRUMP would interpret fired at You Against Can at my dirty mom promos you is this poll
