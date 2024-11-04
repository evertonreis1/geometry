# GeoExplorer 3D

Este projeto foi desenvolvido como parte de uma disciplina de Computação Gráfica e explora conceitos fundamentais para criação de ambientes virtuais interativos em OpenGL. O tema do trabalho é "Jogos Educativos", e o objetivo é criar um ambiente 3D que permite explorar formas geométricas, animações, colisões e efeitos de câmera e iluminação de forma educativa.

## Funcionalidades

### 1. Câmera em Primeira Pessoa e Câmeras Fixas
- **Câmera em Primeira Pessoa**: Permite ao usuário explorar a cena a partir de uma perspectiva em primeira pessoa, posicionada à altura dos olhos.
- **Câmeras Fixas**: Incluímos outras duas câmeras fixas, oferecendo diferentes ângulos de visão da cena. A alternância entre as câmeras é feita pelo teclado.

### 2. Iluminação
- **Luz Fixa**: Uma fonte de luz constante ilumina a cena, destacando os objetos.
- **Luz Ativável**: Outra luz pode ser ativada para dar ênfase em diferentes áreas, proporcionando maior flexibilidade e controle sobre o ambiente iluminado.

### 3. Sensor de Proximidade (Colisão)
- Implementamos um sensor de proximidade que detecta quando o usuário está próximo de um objeto. Quando a proximidade é detectada, uma breve descrição do objeto é exibida no terminal.
  
### 4. Cores e Materiais
- **Cores Aleatórias**: Cada objeto possui uma cor aleatória para tornar a cena mais viva e diversificada.
- **Materiais**: Aplicamos materiais diferenciados para cada objeto, o que melhora o realismo e a experiência visual.

### 5. Objetos Compostos e Animados
- A cena é composta por diversos objetos geométricos (cubo, esfera, cone, cilindro, toroide, icosaedro e dodecaedro), cada um posicionado para criar um ambiente interativo.
- Um dos objetos é animado e se ativa conforme o usuário se aproxima, proporcionando uma experiência educativa dinâmica.

## Estrutura do Código

### Importações e Configurações
Utilizamos as bibliotecas OpenGL, GLUT e GLU para renderizar a cena e aplicar os efeitos de câmera e iluminação.

### Funções Principais
- **setup_lighting**: Configura a iluminação da cena com fontes de luz fixa e ativável.
- **draw_shapes**: Desenha os objetos geométricos na cena.
- **detect_nearby_object**: Detecta quando a câmera se aproxima de um objeto e exibe sua descrição.
- **keyboard**: Controla a movimentação da câmera e a troca de câmeras fixas.
- **mouse_motion**: Altera o ângulo de visão da câmera com base no movimento do mouse.
- **update_camera**: Atualiza a posição da câmera de acordo com a câmera ativa.
- **display**: Função de renderização que desenha os objetos, a iluminação e a câmera.

### Configuração da Cena
- **Cores Aleatórias**: As cores dos objetos são geradas aleatoriamente.
- **Animação**: Um dos objetos é animado, ativando-se conforme a câmera se aproxima.

## Como Executar

Para executar o projeto, tenha as bibliotecas OpenGL instaladas em seu ambiente Python e execute o código com o seguinte comando:

```bash
python main.py
```
## Controles do Jogo

- **W, A, S, D**: Movimentação em primeira pessoa
- **C**: Alterna entre as câmeras fixas
- **Mouse**: Controle da visão em primeira pessoa

## Requisitos do Projeto

Este ambiente foi projetado com base nas especificações do projeto de Computação Gráfica:

- **Câmera em Primeira Pessoa e Câmeras Fixas**: Implementadas três câmeras com transições controladas pelo teclado.
- **Iluminação**: Luz fixa e ativável configuradas com intensidade e difusão variáveis.
- **Sensor de Proximidade**: Implementado com detecção de distância.
- **Cores**: As cores dos objetos foram cuidadosamente selecionadas.
- **Objetos Animados e Compostos**: Inclui objetos geométricos básicos e um objeto animado ativado por proximidade.
