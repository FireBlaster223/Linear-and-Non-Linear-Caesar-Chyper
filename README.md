# Linear-and-Non-Linear-Caesar-Cypher
APS 2º Semestre - Ciência da Computação

I made this by myself to encrypt text by using caesar chyper and a custom version of it, Basically you write a text message and choose a `Key` between 1 and 55.294 and in the `optionBox` the type of cryptography between Linear Caesar Cypher and Non linear Caesar Cypher.

## Caesar Linear Cypher

The Linear Caesar Cypher uses the normal method just uses the value defined `Key` to add this number in to the  `Message`  and walk over the UTF-8 Table ( If reach the end of the table the code start's again from the beginning). The main weakeness of this method is every carachter has a value and this value repeat like the space on the example uses the value of `%`so in every blank space is a `%` with software assistance can easily discover the secret.

## Caesar Linear Cypher 
The Non Linear Caesar Cypher uses a custom method that he take the message and using the `Key`value he create's a list and randomize a key value and add this value to the text, because of the random values the result will always be random.

### For Example :

I write the message `Hello World !` and chooses the Linear Cypher with the key value 5, so the program add + 5 for every carachter in the text.
`Hello World !` + 5 --> `Mjqqt%\twqi%&`. 

I write the message `Hello World !` and chooses the Non Linear Cypher with the key value 5, so the program add + 5 for every carachter in the text.
`Hello World !` + 5 --> `ifjgjQkvsy)]yyvm&` .
