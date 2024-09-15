# (BD - 2021.2): Bossow, rede social de jogos
Projeto final da disciplina de Bancos de Dados, ofertada na Universidade de Brasília (UnB) no semestre 2021.2.

## Executando o projeto

O site foi feito utilizando Flask. Para executá-lo, basta dar build no docker-compose. A aplicação em Flask e o banco MySQL já estão configurados como contêineres. A imagem MySQL foi customizada para já ser inicializada com alguns dados básicos.

```bash
docker-compose build
docker-compose up
```

O site poderá ser acessado através da URL: `http://localhost:5001/`.

## Interface com usuário

A interface permite a interação com as entidades de usuário, jogo, avaliações, reclamações, lembretes e imagens.

O acesso à biblioteca geral de jogos do Bossow é livre para qualquer pessoa (mesmo as não autenticadas), resultando na tela abaixo.

<p align="center"><img src="media/jogos.png" alt="all_games" style="width:55%;"/></p>

Cada jogo tem sua tela própria, onde é possível que os usuários logados façam avaliações, com notas, assim como façam reclamações para os administradores, pedindo alterações na página.

<p align="center"><img src="media/reviews.png" alt="game_reviews" style="width:55%;"/></p>

As notas dadas nas avaliações dos usuários são então usadas como base para o ranking de jogos cadastrados na plataforma.

<p align="center"><img src="media/ranking.png" alt="ranking" style="width:55%;"/></p>

As informações gerais de cada usuário podem ser acessadas na sua página de perfil, onde há informações sobre a conta, jogos adquiridos e avaliações publicadas.

<p align="center"><img src="media/profile.png" alt="profile" style="width:55%;"/></p>

Outras telas foram implementadas.

## Usuários de teste

O banco já está populado com vários perfis de teste. No entanto, os dois perfis básicos para testar os acessos ao site são os seguintes, com as permissões de administrador e usuário comum, respectivamente:

```
E-mail: admin@bossow.com
Senha: admin123
```

```
E-mail: luigi_fantasma@bossow.com
Senha: teste123
```
