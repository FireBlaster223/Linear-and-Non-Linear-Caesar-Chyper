import random

def ceasar_cypher(mensagem, chave):
	return "".join(chr(ord(letra)+chave) for letra in mensagem)

def non_linear_cypher(word: str, key: int) -> str:
	arr = [random.randint(1, 5) for i in range(5)]
	msg = "".join(chr(element+96) for element in arr)
	for index, letter in enumerate(word):
		msg += chr(ord(letter) + arr[index%5])
	return ceasar_cypher(msg, key)  

def reverse_non_linear_cypher(word: str, key: int) -> str:
	word: str = ceasar_cypher(word, key*-1)
	arr: list = [int(ord(word[i])-96) for i in range(5)]
	word: str = word[5:]
	msg: str = ""
	for index, letter in enumerate(word):
		msg += chr(ord(letter) - arr[index%5])
	return msg
	
def chinese_cryp(msg, key: int):
	msg: str = ""
	for c in msg: msg += chr(ord(c) + 30000 + key)
	return msg
   
def reverse_chinese_cryp(msg, key: int):
    msg: str = ""
    for c in msg: msg += chr(ord(c) - 30000)
    return msg