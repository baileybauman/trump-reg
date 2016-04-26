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

Right now our algorithm takes in Trump's tweets and calls an external library that labels each word with a part of speech and puts each word in a specific part of speech dictionary. We also keep track of the sentence structure of each tweet. Each time the program is run a sentence structure is chosen at random and each part of speech in the structure is filled in with a word that Trump has said that is that part of speech. We are currently taking the top words and choosing one at random to insert. We then output our predicted Trump tweet. 

We have another method of generating tweets that involves looking at common phrases and parts of speech that occur together often. We keep track of certain pairs of important parts of speech and then when generating a tweet, if we find a pair in the sentence, we generate a pair of words that Trump has said before. 

## Sample output 

>  @seanhannity @megynkelly @seanhannity poll believes all up Rubio with Trump up lost done of #VoteTrump

>  @CNN @seanhannity @oreillyfactor @JebBush much tonight #TrumpTrain believes being HOW would it make Cruz https://t.co/r8ijPnCsmO

>  @JebBush WILL @oreillyfactor see GREAT that We were from @realDonaldTrump the Thank me must Great To get Great much

> could @JebBush at his Thank Trump debate amp We saying He to be na her Cruz of a Thank

>  #TrumpTrain Trump to go South Just made Thank has Rubio last Great Donald #IACaucus https://t.co/nU39QHzxxX

> who failed president by my live run by looking for on i watching any lowest much years on him on @cnn !

> @morningjoe @seanhannity @megynkelly @jebbush america trump ratings trump done for you see poll wants amazing https://_

> much president poll ted donald america polls of poll i at trump to trump cruz trump . https://t.co/jg50w3rcnn

> @foxnews #trumptrain trump may again america of i and #gopdebate . their trump gives respected to @oreillyfactor donald numbers ! president with every cruz.

> can have president at @realdonaldtrump at 1000 trump !

> @oreillyfactor hillary last for last hillary cruz thank ads last debate trump one president but any thanks .

> @foxnews any done poll people million ratings from much hillary from i thanks her looking america https://t.co/ANvTcZqfOq", 
> the vote since i makes any so stay win ! us feel total hes then & are tough because cruz ! https://t.co/BmZyKQOZJJ

> @ivankatrump @abc another hit since politics country allow are jeb i under budget increase say crippled controlled their rt represents bigger than bernie must campaign !

> because this total failure rubio give endorsed my donald trump.th to rubio from 1000 politics another next little barry wo time drudge 

> debate would say dont into @danscavino dont under 4 . itself wo give us together showing america thank . want .

> @nbcsnl @wsj https://t.co/oEh5cVJCFa hillary represents massive crowd in sc !

> shows want myself any showed donald hello some rest . only donald any @drudgereport thank .


## Things to implement still


## UI Implementation

Our UI can be seen by going to matpd.tech/TrumpReg 

