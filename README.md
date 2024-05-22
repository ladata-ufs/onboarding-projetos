# On Boarding - Diretoria de Projetos

A finalidade desse repositório é ceder a base para a realização do primeiro projeto de treino na LADATA. Além disso, utilizar todas ou a maior parte das ferramentas de desenvolvimento e organização de produtos desenvolvidos dentro da Liga.

## Ferramentas-chave
- Git
- Github (Github projects, Pull Requests, Branchs)
- Notion
- Portais de Bases de dados abertas (Kaggle, HuggingFace, etc...)

## "Ok, mas o que eu faço?"

### 1. Calmaí, já escolheu seu grupo? 🤨

Primeiramente, certifique-se de estar em um grupo com pelo menos 3 pessoas (e menos de 4).

### 2. Tema do projetinho

Para esse onboarding, foram escolhidos 3 temas para trabalho, seu grupo deve escolher um deles (que de preferência seja de agrado de todos), e é nele que vão desenvolver. Não há limite de escolha de temas, então podem escolher temas repetidos. 
Os datasets escolhidos foram:

- [The Complete Pokemon Dataset](https://www.kaggle.com/datasets/rounakbanik/pokemon)

- [IMDb Top 2000 Movies](https://www.kaggle.com/datasets/thegoanpanda/imdb-top-2000-movies)

- [Coffee dataset](https://www.kaggle.com/datasets/michals22/coffee-dataset)

### 3. Organização do projeto

Primeiro, antes de pôr a mão na massa, é necessário criar uma organização para o projeto, dividindo o todo em tarefas. O famoso dividir para conquistar. Contudo, para essa divisão não ser apenas um acordo, são utilizadas as ferramentas: Notion e Github Projects. 

No primeiro, são registrados os projetos que estão em andamento e os passos que precisam ser tomados para que ele seja completo, serve mais para líderes e diretores acompanharem de maneira mais geral o progresso de um projeto.

**O processo de adição na página de projetos fica a cargo do diretor de projetos.**
![alt text](/imagens/image.png)

Certifique se está vendo a página relacionada a seu projeto.
![alt text](/imagens/image-1.png)

Já no segundo, daremos um foco maior em cada tarefa desenvolvida, então além de dizer que está sendo feito, é necessário dizer o que está sendo feito por meio de cards no github Projects. Cada card corresponde a uma partição a ser desenvolvida e cada uma delas deve ser desenvolvida em uma branch separada da "main". E posteriormente, com um processo chamado de Merge, as partes do trabalho serão juntas, gerando um produto final. Mas isso fica para uma parte mais avançada.


Para um panorama mais geral, para facilitar o desenvolvimento do projeto, é possível criar um "fork" desse repositório, ou seja, pegar o modelo deste para desenvolver como base, nesse caso, apenas um membro da equipe precisa realizar o processo. Por questão de organização, o fork deve ser feito com o owner LADATA.

**Podem adicionar um nome mais criativo que esse 😁**
![alt text](/imagens/image-2.png)

Depois de criar o fork, solicite ao diretor de projetos [Sérgio](https://github.com/sergio-UFS) para que o repositório seja adicionado no Time de Projetos. Com isso, já é possível acessar com mais facilidade o repositório por meio da aba Teams no github

![alt text](/imagens/image-4.png)

Acessando a aba de Teams, será possível encontrar os repositórios relacionados ao time e os membros associados

![alt text](/imagens/image-5.png)

Na aba de Projects, é possível encontrar o [Dashboard de projetos](https://github.com/orgs/ladata-ufs/projects/5), é nele que todas as branches e projetos ficarão associados. Separados por projetos e labels e principalmente, status de desenvolvimento

![alt text](/imagens/image-8.png)

Ao adicionar uma tarefa, como na foto anterior, é criado um "draft", que seria um rascunho de tarefa e dentro dela, pode ser transformada em issue, que é quando uma tarefa se torna de fato, algo a desenvolver. Na criação da issue é possível adicionar a um projeto, fique atento(a) para adicionar corretamente o seu projeto. 

![alt text](/imagens/image-9.png)

Depois disso, é possivel criar uma branch para desenvolver aquele problema específico, com a finalidade de proteger o código da main de algum commit com erros, e por isso, todas as branchs devem ser criadas com a base na main.

![alt text](/imagens/image-10.png)




### 4. Desenvolvimento do Projeto


Eu sei que são muitos passos, mas, como o objetivo desse projeto é a colaboração, incluido as diretorias, estaremos sempre à disposição para dúvidas tanto no grupo LADATAS, quanto no e-mail ou github.

Enfim, a finalidade desse projeto é, a partir das bases de dados apresentadas acima, seja possível extrair informações valiosas e interessantes, podem ser por meio de gráficos, comparações, dados brutos e tabelas. 

Os dados necessariamente devem ser importados do formato csv e tratados por meio de código em python por meio de Jupyter Notebooks (o exemplo desse repositório pode ser usado como base). Uma dica valiosa sobre esse onBoarding é: Tentem surpreender. Ou seja, recapitulando, vocês devem:

- Formar equipes de 3 ou 4 pessoas
- Escolher um tema de projeto
- Adicionar a(s) base(s) de dados na pasta data do projeto
- Se reunir com os membros do grupo para a criação do repositório no github a partir desse modelo
- Comunicar o diretor de projetos sobre a criação
- Acessar o [Dashboard de projetos](https://github.com/orgs/ladata-ufs/projects/5)
- Dividir as tarefas e cadastrar no dashboard acima
- Criar issues e branchs para cada issue.

### 5. Objetivo

- Apresentar pelo menos 4 fontes de dados tratados (gráficos, tabelas, etc) com informações retiradas da base de dados escolhida por meio de um Jupyter notebook
- Atualizar o status das tarefas e tirar dúvidas com as diretorias, se necessário
- Atualizar a branch main com todas as alterações.
- Anotar as bibliotecas utilizadas e incluir um arquivo "requirements.txt"

**Lembrando que o objetivo desse projeto não é avaliar, e sim, dar uma noção de como funcionaria a parte de projetos na prática.**