# Projeto Final UFF-Biologia Computacional

Este projeto foi desenvolvido com o objetivo de construção de um algoritmo para o problema da maior subcadeia em comum 
(Longest Common Substring - LCS) utilizando a abordagem que utiliza árvores de sufixos generalizadas para encontrar a 
solução em tempo linear.

### Pseudo-algoritmo

1. Gerar N caracteres únicos e concatená-los ao final de cada string
2. Concatenar as novas strings geradas, resultando em apenas uma, denotada por S, com comprimento L igual a soma dos comprimentos das strings originais + N
3. Iniciar a construção da árvore, cuja raiz será S
4. Percorrer i em S,de 0 a L, obtendo o sufixo S[i:L], e inserir na árvore como uma nova folha.\
a. Para cada S[i:L], verificar se existe um nó S[j:L], j<i, cuja aresta possa ser escrita como ax, onde a é um prefixo em comum com a aresta de S[i:L]. \
b. Se existir, dividir a aresta de S[j:L] em duas: x e S[i+Len(a):L]. Assim, S[i:L] será uma nova folha de S[j:L]. \
c. Caso contrário, S[i:L] será uma nova folha da raiz.
5. Após a construção da árvore, encontrar o caminho até o nó mais profundo que passe apenas por nós com filhos representando sufixos de todas as strings.

### Execução

Para construção da ávore de sufixos generalizada, basta executar o comando:
```
 $ python suffix-tree.py
 ```