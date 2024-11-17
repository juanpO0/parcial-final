import json

soup =  [ ["A", "M", "A", "R", "S"],
          ["S", "T", "E", "R", "I"],
          ["O", "M", "A", "Z", "C"],
          ["A", "L", "C", "R", "H"],
          ["P", "O", "L", "O", "S"]]

def line_search(soup, word):
    
    for line in soup:  
        found = True
    
        for i in range(len(word)):  
            if line[i] != word[i]:  
                found = False  
        if found:
            return True

        line.reverse()  
        found = True
        for i in range(len(word)):  
            if line[i] != word[i]:  
                found = False  
        if found:
            return True

    return False  


print(line_search(soup, "POLOS"))


def col_search(soup, word):

    for col in range(len(soup[0])):  

        column = [soup[line][col] for line in range(len(soup))] 

        if ''.join(column).find(word) != -1:

            return True

        if ''.join(column[::-1]).find(word) != -1:

            return True
        
    return False

print(col_search(soup, "OSA"))

def diag_search(soup, word):
    
    if len(word) > len(soup):
        return False  

    for i in range(len(word)):
        if soup[i][i] != word[i]:  
            return False  

    return True  

print(diag_search(soup, "ATAR"))


def verify_words(soup, lista_words):
    resultados = {}  
    
    for word in lista_words:
        
        if (line_search(soup, word) or
            col_search(soup, word) or
            diag_search(soup, word)):
            resultados[word] = "Encontrada"
        else:
            resultados[word] = "No encontrada"
    
    return resultados



def guardar_resultados(results):
    with open("resultados.json", "w") as f:
        json.dump(results, f, indent=4)

words = ["AMAR", "OSA", "ATAR", "SOLO", "POLOS"]

results = verify_words(soup, words)

guardar_resultados(results)
