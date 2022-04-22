USE bossow;

#-------------------- Imagens --------------------#

#--- Fotos de perfil ---#

INSERT INTO image(img, filename, mimetype)
VALUES (LOAD_FILE('C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\default_picture.jpg'), 'default_picture.jpg', 'image/jpeg');

INSERT INTO image(img, filename, mimetype)
VALUES (LOAD_FILE('C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\ac_profile.jpg'), 'ac_profile.jpg', 'image/jpeg');

INSERT INTO image(img, filename, mimetype)
VALUES (LOAD_FILE('C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\link_profile.png'), 'link_profile.png', 'image/png');

INSERT INTO image(img, filename, mimetype)
VALUES (LOAD_FILE('C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\luigi_profile.png'), 'luigi_profile.png', 'image/png');

INSERT INTO image(img, filename, mimetype)
VALUES (LOAD_FILE('C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\mario_profile.png'), 'mario_profile.png', 'image/png');

INSERT INTO image(img, filename, mimetype)
VALUES (LOAD_FILE('C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\rosalina_profile.png'), 'rosalina_profile.png', 'image/png');

#--- Capas de jogos ---#

INSERT INTO image(img, filename, mimetype)
VALUES (LOAD_FILE('C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\botw_art.jpg'), 'botw_art.jpg', 'image/jpeg');

INSERT INTO image(img, filename, mimetype)
VALUES (LOAD_FILE('C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\celeste_art.jpg'), 'celeste_art.jpg', 'image/jpeg');

INSERT INTO image(img, filename, mimetype)
VALUES (LOAD_FILE('C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\disco_elysium_art.jpeg'), 'disco_elysium_art.jpeg', 'image/jpeg');

INSERT INTO image(img, filename, mimetype)
VALUES (LOAD_FILE('C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\going_under_art.jpg'), 'going_under_art.jpg', 'image/jpeg');

INSERT INTO image(img, filename, mimetype)
VALUES (LOAD_FILE('C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\hollow_knight_art.jpg'), 'hollow_knight_art.jpg', 'image/jpeg');

INSERT INTO image(img, filename, mimetype)
VALUES (LOAD_FILE('C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\pokemon_arceus_art.jpeg'), 'pokemon_arceus_art.jpeg', 'image/jpeg');

INSERT INTO image(img, filename, mimetype)
VALUES (LOAD_FILE('C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\stardew_valley_art.jpg'), 'stardew_valley_art.jpg', 'image/jpeg');

INSERT INTO image(img, filename, mimetype)
VALUES (LOAD_FILE('C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\super_mario_3d_world_art.jpg'), 'super_mario_3d_world_art.jpg', 'image/jpeg');

#--- Screenshots de jogos ---#

INSERT INTO image(img, filename, mimetype)
VALUES (LOAD_FILE('C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\celeste1.png'), 'celeste1.png', 'image/png');

INSERT INTO image(img, filename, mimetype)
VALUES (LOAD_FILE('C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\celeste2.jpg'), 'celeste2.jpg', 'image/jpeg');

INSERT INTO image(img, filename, mimetype)
VALUES (LOAD_FILE('C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\celeste3.jpg'), 'celeste3.jpg', 'image/jpeg');

INSERT INTO image(img, filename, mimetype)
VALUES (LOAD_FILE('C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\celeste4.jpg'), 'celeste4.jpg', 'image/jpeg');

INSERT INTO image(img, filename, mimetype)
VALUES (LOAD_FILE('C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\celeste5.jpeg'), 'celeste5.jpeg', 'image/jpeg');

INSERT INTO image(img, filename, mimetype)
VALUES (LOAD_FILE('C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\hollow_knight1.jpg'), 'hollow_knight1.jpg', 'image/jpeg');

INSERT INTO image(img, filename, mimetype)
VALUES (LOAD_FILE('C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\hollow_knight2.jpg'), 'hollow_knight2.jpg', 'image/jpeg');

INSERT INTO image(img, filename, mimetype)
VALUES (LOAD_FILE('C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\hollow_knight3.jpg'), 'hollow_knight3.jpg', 'image/jpeg');

#-------------------- Usuários --------------------#

INSERT INTO user(email, password, full_name, role, profile_picture)
VALUES ('admin@bossow.com', 'admin123', 'Admin', 'admin', 2);

INSERT INTO user(email, password, full_name, role, profile_picture)
VALUES ('maria_testadora@bossow.com', 'teste123', 'Maria Testadora', 'user', 3);

INSERT INTO user(email, password, full_name, role, profile_picture)
VALUES ('bowser_voador@bossow.com', 'teste123', 'Bowser Voador', 'user', 4);

INSERT INTO user(email, password, full_name, role, profile_picture)
VALUES ('joana_silva@bossow.com', 'teste123', 'Joana Silva', 'user', 5);

INSERT INTO user(email, password, full_name, role, profile_picture)
VALUES ('luigi_fantasma@bossow.com', 'teste123', 'Luigi Fantasma', 'user', 6);

#-------------------- Jogos --------------------#

INSERT INTO game(title, release_date, description, developer, publisher, trailer_url, cover_picture)
VALUES ('The Legend of Zelda: Breath of the Wild', '2017-03-03 00:00:00', 'Hyrule regrediu a um estado medieval. Dez mil anos depois, os hyrulianos leram as profecias de seus ancestrais e reconheceram os sinais do retorno de Ganon, escavando e recuperando as Feras Divinas e os Guardiões.', 'Nintendo', 'Nintendo', 'https://www.youtube.com/watch?v=1rPxiXXxftE', 7);

INSERT INTO game(title, release_date, description, developer, publisher, trailer_url, cover_picture)
VALUES ('Celeste', '2018-01-25 00:00:00', 'A trama acompanha a história de Madeline, uma jovem garota que resolveu, em um ato imprudente, escalar até o topo da montanha Celeste apenas para provar para si mesma de que ela era capaz.', 'Extremely OK Games', 'Extremely OK Games', 'https://www.youtube.com/watch?v=iofYDsA2yqg', 8);

INSERT INTO game(title, release_date, description, developer, publisher, trailer_url, cover_picture)
VALUES ('Disco Elysium', '2019-10-15 00:00:00', 'O jogo se passa na fictícia cidade de Revachol, mais especificamente no bairro costal de Martinaise, cheio de crime, pobreza e corrupção, controlada pelo corrupto Sindicato dos estivadores.', 'ZA/UM', 'ZA/UM', 'https://www.youtube.com/watch?v=YV2lp6p_gXw', 9);

INSERT INTO game(title, release_date, description, developer, publisher, trailer_url, cover_picture)
VALUES ('Going Under', '2020-09-23 00:00:00', 'Going Under é um dungeon crawler roguelike satírico baseado na cultura de startups de tecnologia, usando-se de trocadilhos deste mundo tanto nos diálogos, quanto na mecânica e no design dos personagens rendendo boas risadas.', 'Aggro Crab', 'Team17', 'https://www.youtube.com/watch?v=nKLELV7YLns', 10);

INSERT INTO game(title, release_date, description, developer, publisher, trailer_url, cover_picture)
VALUES ('Hollow Knight', '2017-02-24 00:00:00', 'Hollow Knight conta a historia de um diminuto guerreiro que decide entrar nas cavernas que abrigam as ruínas do reino de Hallownest. Devido à uma infestação que roubou os insetos de sua inteligência e os reverteu aos seus instintos primitivos, uma nação foi destruída.', 'Team Cherry', 'Team Cherry', 'https://www.youtube.com/watch?v=kWo5g-tsBNk', 11);

INSERT INTO game(title, release_date, description, developer, publisher, trailer_url, cover_picture)
VALUES ('Pokémon Legends: Arceus', '2022-01-28 00:00:00', 'A trama é ambientada em uma época em que Pokémon e humanos viviam separados. Nesse contexto, surge um time de pesquisa que decide estudar e aprender mais sobre os Pokémon. Este grupo é chamado de Galaxy Team.', 'Game Freak', 'Nintendo', 'https://www.youtube.com/watch?v=SbIA8FKhwl0', 12);

INSERT INTO game(title, release_date, description, developer, publisher, trailer_url, cover_picture)
VALUES ('Stardew Valley', '2016-02-26 00:00:00', 'É um jogo de simulação de fazenda, onde o jogador pode selecionar um de cinco tipos de fazenda de acordo com sua preferência, como uma com mais oportunidades de pilhamento da terra, uma com mais recursos de mineração e outra com um rio de pesca.', 'ConcernedApe', 'ConcernedApe', 'https://www.youtube.com/watch?v=8A7A1X1TVNc', 13);

INSERT INTO game(title, release_date, description, developer, publisher, trailer_url, cover_picture)
VALUES ('Super Mario 3D World', '2013-11-21 00:00:00', 'Mario, Luigi, Princesa Peach e Toad estão caminhando no Reino dos Cogumelos, quando veem um cano transparente, Mario e Luigi consertam-o, e dele saem vários objetos. No final, uma Anafada sai do cano desesperada, contando que Bowser invadiu o reino e capturou as outras seis princesas.', 'Nintendo', 'Nintendo', 'https://www.youtube.com/watch?v=wLOKVABfrzw', 14);

#-------------------- Biblioteca de jogos --------------------#

INSERT INTO library_game(user_id, game_id, hours_played, completion_percentage, last_logged_in)
VALUES (1, 1, 43, 30, '2020-01-01 00:00:00');

INSERT INTO library_game(user_id, game_id, hours_played, completion_percentage, last_logged_in)
VALUES (1, 2, 8, 63, '2020-01-01 00:00:00');

INSERT INTO library_game(user_id, game_id, hours_played, completion_percentage, last_logged_in)
VALUES (1, 3, 25, 89, '2020-01-01 00:00:00');

INSERT INTO library_game(user_id, game_id, hours_played, completion_percentage, last_logged_in)
VALUES (2, 1, 65, 52, '2020-01-01 00:00:00');

INSERT INTO library_game(user_id, game_id, hours_played, completion_percentage, last_logged_in)
VALUES (2, 3, 31, 91, '2020-01-01 00:00:00');

INSERT INTO library_game(user_id, game_id, hours_played, completion_percentage, last_logged_in)
VALUES (2, 4, 24, 77, '2020-01-01 00:00:00');

INSERT INTO library_game(user_id, game_id, hours_played, completion_percentage, last_logged_in)
VALUES (2, 6, 31, 72, '2020-01-01 00:00:00');

INSERT INTO library_game(user_id, game_id, hours_played, completion_percentage, last_logged_in)
VALUES (3, 1, 12, 10, '2020-01-01 00:00:00');

INSERT INTO library_game(user_id, game_id, hours_played, completion_percentage, last_logged_in)
VALUES (3, 5, 78, 71, '2020-01-01 00:00:00');

INSERT INTO library_game(user_id, game_id, hours_played, completion_percentage, last_logged_in)
VALUES (3, 7, 143, 89, '2020-01-01 00:00:00');

INSERT INTO library_game(user_id, game_id, hours_played, completion_percentage, last_logged_in)
VALUES (3, 8, 31, 92, '2020-01-01 00:00:00');

INSERT INTO library_game(user_id, game_id, hours_played, completion_percentage, last_logged_in)
VALUES (4, 1, 98, 92, '2020-01-01 00:00:00');

INSERT INTO library_game(user_id, game_id, hours_played, completion_percentage, last_logged_in)
VALUES (4, 2, 12, 41, '2020-01-01 00:00:00');

INSERT INTO library_game(user_id, game_id, hours_played, completion_percentage, last_logged_in)
VALUES (4, 5, 64, 73, '2020-01-01 00:00:00');

INSERT INTO library_game(user_id, game_id, hours_played, completion_percentage, last_logged_in)
VALUES (4, 6, 43, 94, '2020-01-01 00:00:00');

INSERT INTO library_game(user_id, game_id, hours_played, completion_percentage, last_logged_in)
VALUES (4, 8, 33, 85, '2020-01-01 00:00:00');

INSERT INTO library_game(user_id, game_id, hours_played, completion_percentage, last_logged_in)
VALUES (5, 1, 54, 39, '2020-01-01 00:00:00');

INSERT INTO library_game(user_id, game_id, hours_played, completion_percentage, last_logged_in)
VALUES (5, 3, 38, 95, '2020-01-01 00:00:00');

INSERT INTO library_game(user_id, game_id, hours_played, completion_percentage, last_logged_in)
VALUES (5, 4, 35, 99, '2020-01-01 00:00:00');

INSERT INTO library_game(user_id, game_id, hours_played, completion_percentage, last_logged_in)
VALUES (5, 5, 82, 78, '2020-01-01 00:00:00');

INSERT INTO library_game(user_id, game_id, hours_played, completion_percentage, last_logged_in)
VALUES (5, 7, 234, 100, '2020-01-01 00:00:00');

#-------------------- Capturas de tela --------------------#

INSERT INTO screenshot(pic_id, user_id, game_id)
VALUES (15, 1, 2);

INSERT INTO screenshot(pic_id, user_id, game_id)
VALUES (16, 1, 2);

INSERT INTO screenshot(pic_id, user_id, game_id)
VALUES (17, 1, 2);

INSERT INTO screenshot(pic_id, user_id, game_id)
VALUES (18, 1, 2);

INSERT INTO screenshot(pic_id, user_id, game_id)
VALUES (19, 1, 2);

INSERT INTO screenshot(pic_id, user_id, game_id)
VALUES (20, 3, 5);

INSERT INTO screenshot(pic_id, user_id, game_id)
VALUES (21, 3, 5);

INSERT INTO screenshot(pic_id, user_id, game_id)
VALUES (22, 3, 5);

#-------------------- Avaliações --------------------#

INSERT INTO review(user_id, game_id, review_text, score)
VALUES (1, 1, 'Apenas o melhor jogo já feito... Mais de 100 horas e ainda tô longe dos 100%.', 5);

INSERT INTO review(user_id, game_id, review_text, score)
VALUES (1, 2, 'Difícil demais para o meu gosto, mas sem dúvida muito bom e bonito.', 4);

INSERT INTO review(user_id, game_id, review_text, score)
VALUES (1, 5, 'Melhor metroidvania que já joguei - e praticamente de graça, 30 reais por mais de 50h de gameplay.', 5);

INSERT INTO review(user_id, game_id, review_text, score)
VALUES (2, 1, 'Exploração literalmente infinita. Jogo de Zelda de mundo aberto que até quem não gosta de mundo aberto ou jogo de Zelda vai curtir.', 5);

INSERT INTO review(user_id, game_id, review_text, score)
VALUES (2, 3, 'Muito raro achar algo (livro, filme, jogo) tão bem escrito e pensado. Ainda mais raro ver um jogo tratando temas tão complexos como aqui.', 5);

INSERT INTO review(user_id, game_id, review_text, score)
VALUES (2, 6, 'História fraca, diálogos mais fracos ainda. Gráficos inconsistentes - às vezes bonitos, às vezes feios. Tinha tudo para ser bom mas foi ruim.', 1);

INSERT INTO review(user_id, game_id, review_text, score)
VALUES (2, 7, 'Me sinto de volta ao Colheita Feliz, mas sem a possibilidade de interação online com mais de 100 amigos no Orkut. Barato, mas não empolga.', 2);

INSERT INTO review(user_id, game_id, review_text, score)
VALUES (3, 1, 'Impossível alguém dar menos que 5/5 pra BOTW.', 5);

INSERT INTO review(user_id, game_id, review_text, score)
VALUES (3, 7, 'Viciante - se inspira e melhora as mecânicas de Harvest Moon. E também é de graça - mais de 100h de gameplay fácil.', 5);

INSERT INTO review(user_id, game_id, review_text, score)
VALUES (3, 8, 'Meu Mario 3D favorito. É o único Mario 3D que é de fato uma versão 3D do jogo em 2D, pegando toda a jogabilidade dos Marios clássicos e jogando para um 3D.', 5);

INSERT INTO review(user_id, game_id, review_text, score)
VALUES (4, 1, 'Como assim as armas quebram? Jogo de 2017 com esses gráficos? Patético.', 2);

INSERT INTO review(user_id, game_id, review_text, score)
VALUES (4, 2, 'Arte muito bonita e jogabilidade interessante.', 5);

INSERT INTO review(user_id, game_id, review_text, score)
VALUES (4, 4, 'Divertido e viciante, e ainda carregado de críticas à exploração no ambiente de trabalho.', 5);

INSERT INTO review(user_id, game_id, review_text, score)
VALUES (4, 6, 'O mais perto de mundo aberto que Pokémon já chegou - o que é incrível.', 5);

INSERT INTO review(user_id, game_id, review_text, score)
VALUES (4, 8, 'Não é tão bom quanto os outros Super Mario 3D, principalmente o Odyssey, mas ainda assim é mto detalhado e rico.', 4);

#-------------------- Denúncias --------------------#

INSERT INTO complaint(user_id, game_id, type, complaint_text)
VALUES (2, 1, 'change', 'Enredo mal escrito, precisa encontrar um texto que resuma melhor o que se passa no jogo.');

INSERT INTO complaint(user_id, game_id, type, complaint_text)
VALUES (2, 2, 'change', 'Faltou mencionar em alguma parte que uma equipe brasileira trabalhou na arte do jogo.');

INSERT INTO complaint(user_id, game_id, type, complaint_text)
VALUES (3, 3, 'delete', 'Esse jogo tem cenas para maiores de 18 anos. Como essa é uma plataforma aberta, acho que qualquer jogo que não tenha indicação livre precisa ser apagado daqui.');

INSERT INTO complaint(user_id, game_id, type, complaint_text)
VALUES (3, 7, 'change', 'Existem trailers muito mais completos que vocês poderiam colocar para Stardew Valley.');

INSERT INTO complaint(user_id, game_id, type, complaint_text)
VALUES (4, 8, 'change', 'Poderiam atualizar a edição aqui. Já lançaram uma edição completa do jogo no Switch, mas aí está a versão para o Wii U.');

INSERT INTO complaint(user_id, game_id, type, complaint_text, solved)
VALUES (3, 1, 'delete', 'Tem muitos 5 na avaliação, acho que é melhor apagar a página e recriar do 0.', 1);

INSERT INTO complaint(user_id, game_id, type, complaint_text, solved)
VALUES (3, 2, 'delete', 'Jogo fala sobre depressão... Não acho que esse tipo de conteúdo devesse estar aqui no Bossow.', 1);

INSERT INTO complaint(user_id, game_id, type, complaint_text, solved)
VALUES (4, 4, 'delete', 'Quase ninguém joga esse jogo, pra que ter na plataforma???', 1);

#-------------------- Lembretes --------------------#

INSERT INTO note(user_id, note_text)
VALUES (1, 'Checar todas as denúncias e solucioná-las.');

INSERT INTO note(user_id, note_text)
VALUES (2, 'Comprar Switch Sports na pré-venda na Amazon!');

INSERT INTO note(user_id, note_text)
VALUES (3, 'Zerar Super Mario 3D World logo.');

INSERT INTO note(user_id, note_text)
VALUES (3, 'Encher o saco do administrador para ele excluir BOTW daqui logo.');

INSERT INTO note(user_id, note_text)
VALUES (4, 'Adicionar Pokémon Scarlet no catálogo do Bossow.');