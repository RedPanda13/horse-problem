# Problema do Cavalo

### Descrição:
O problema do cavalo, ou passeio do cavalo, é um problema matemático envolvendo o movimento da peça do
cavalo no tabuleiro de xadrez. O cavalo é colocado no tabuleiro vazio e, seguindo as regras do jogo,
precisa passar por todas as casas exatamente uma vez em movimentos consecutivos.

### Objetivo:
Criar algoritmos usando TDD para fazer o cavalo andar pelo máximo de casas possíveis.

### Restrições:
* #### Movimentos Possiveis:
    * Alto, Alto, Direita
    * Alto, Alto, Esquerda
    * Baixo, Baixo, Direita
    * Baixo, Baixo, Esquerda
    * Direita, Direita, Alto
    * Direita, Direita, Baixo
    * Esquerda, Esquerda, Alto
    * Esquerda, Esquerda, Baixo

    
* Cada casa só poder ser visitada uma vez.
* O cavalo não pode sair do tabuleiro.

### Etapas
    
- [x] Criar do tabuleiro
- [x] Criar teste para a função que gera os movimentos.
- [x] Criar função que gera todos os movimentos possíveis a partir de um ponto inicial.
- [ ] Criar teste para validar que um movimento foi escolhido.
- [ ] Criar função que escolha aleatoriamente um movimento dentro dos movimentos gerados.
- [x] Criar teste para a função que garante que o cavalo não saia do tabuleiro.
- [x] Criar função garantir que o movimento não faça o cavalo sair do tabuleiro.
- [x] Criar teste para a função que verifica se o destino não é uma casa já visitada.
- [x] Criar função para garantir se o destino daquele movimento não é uma casa já visitada.
