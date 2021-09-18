# Bleu_scoreeee

The old original paper shows the bleu score value is Blue = BP * exp( 1/N * sum(pn) ) which is wrong because the value of pn is always greater than 1, which make exp( +ve ) > 2.71. 

The new paper resolve the error, the blue score value is �:

![newb](https://user-images.githubusercontent.com/75822824/133872675-a1ca6266-cf10-4335-a2ec-a2b0b9e22571.png)


