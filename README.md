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

Right now our algorithm takes in Trump's tweets and calls an external library that labels each word with a part of speech and puts each word in a specific part of speech dictionary. We also keep track of the sentence structure of each tweet. Each time the program is run a sentence structure is chosen at random and each part of speech in the structure is filled in with a word that Trump has said that is that part of speech. We are currently taking the top 1/5 of words and choosing one at random to insert. We then output our predicted Trump tweet. We still need to implement the probabilities of words getting chosen in a better way.

## Sample output 

>  @seanhannity @megynkelly @seanhannity poll believes all up Rubio with Trump up lost done of #VoteTrump

>  @CNN @seanhannity @oreillyfactor @JebBush much tonight #TrumpTrain believes being HOW would it make Cruz https://t.co/r8ijPnCsmO

>  @JebBush WILL @oreillyfactor see GREAT that We were from @realDonaldTrump the Thank me must Great To get Great much

> @seanhannity @megynkelly @JebBush poll Thank of @ABC very numbers

> could @JebBush at his Thank Trump debate amp We saying He to be na her Cruz of a Thank

>  #TrumpTrain Trump to go South Just made Thank has Rubio last Great Donald #IACaucus https://t.co/nU39QHzxxX

## Things to implement still

> add in punctuation if a tweet structure is more than one sentence

## UI Implementation

Our UI can be seen by going to matpd.tech/TrumpReg 


