USE bossow;

#-------------------- Imagens --------------------#

#--- Fotos de perfil ---#

INSERT INTO Image(data, file_name, mime_type)
VALUES (LOAD_FILE('/var/lib/mysql-files/default_picture.jpg'), 'default_picture.jpg', 'image/jpeg');

INSERT INTO Image(data, file_name, mime_type)
VALUES (LOAD_FILE('/var/lib/mysql-files/ac_profile.jpg'), 'ac_profile.jpg', 'image/jpeg');

INSERT INTO Image(data, file_name, mime_type)
VALUES (LOAD_FILE('/var/lib/mysql-files/link_profile.png'), 'link_profile.png', 'image/png');

INSERT INTO Image(data, file_name, mime_type)
VALUES (LOAD_FILE('/var/lib/mysql-files/luigi_profile.png'), 'luigi_profile.png', 'image/png');

INSERT INTO Image(data, file_name, mime_type)
VALUES (LOAD_FILE('/var/lib/mysql-files/mario_profile.png'), 'mario_profile.png', 'image/png');

INSERT INTO Image(data, file_name, mime_type)
VALUES (LOAD_FILE('/var/lib/mysql-files/rosalina_profile.png'), 'rosalina_profile.png', 'image/png');

#--- Capas de jogos ---#

INSERT INTO Image(data, file_name, mime_type)
VALUES (LOAD_FILE('/var/lib/mysql-files/botw_art.jpg'), 'botw_art.jpg', 'image/jpeg');

INSERT INTO Image(data, file_name, mime_type)
VALUES (LOAD_FILE('/var/lib/mysql-files/celeste_art.jpg'), 'celeste_art.jpg', 'image/jpeg');

INSERT INTO Image(data, file_name, mime_type)
VALUES (LOAD_FILE('/var/lib/mysql-files/disco_elysium_art.jpeg'), 'disco_elysium_art.jpeg', 'image/jpeg');

INSERT INTO Image(data, file_name, mime_type)
VALUES (LOAD_FILE('/var/lib/mysql-files/going_under_art.jpg'), 'going_under_art.jpg', 'image/jpeg');

INSERT INTO Image(data, file_name, mime_type)
VALUES (LOAD_FILE('/var/lib/mysql-files/hollow_knight_art.jpg'), 'hollow_knight_art.jpg', 'image/jpeg');

INSERT INTO Image(data, file_name, mime_type)
VALUES (LOAD_FILE('/var/lib/mysql-files/pokemon_arceus_art.jpeg'), 'pokemon_arceus_art.jpeg', 'image/jpeg');

INSERT INTO Image(data, file_name, mime_type)
VALUES (LOAD_FILE('/var/lib/mysql-files/stardew_valley_art.jpg'), 'stardew_valley_art.jpg', 'image/jpeg');

INSERT INTO Image(data, file_name, mime_type)
VALUES (LOAD_FILE('/var/lib/mysql-files/super_mario_3d_world_art.jpg'), 'super_mario_3d_world_art.jpg', 'image/jpeg');

#--- Screenshots de jogos ---#

INSERT INTO Image(data, file_name, mime_type)
VALUES (LOAD_FILE('/var/lib/mysql-files/celeste1.png'), 'celeste1.png', 'image/png');

INSERT INTO Image(data, file_name, mime_type)
VALUES (LOAD_FILE('/var/lib/mysql-files/celeste2.jpg'), 'celeste2.jpg', 'image/jpeg');

INSERT INTO Image(data, file_name, mime_type)
VALUES (LOAD_FILE('/var/lib/mysql-files/celeste3.jpg'), 'celeste3.jpg', 'image/jpeg');

INSERT INTO Image(data, file_name, mime_type)
VALUES (LOAD_FILE('/var/lib/mysql-files/celeste4.jpg'), 'celeste4.jpg', 'image/jpeg');

INSERT INTO Image(data, file_name, mime_type)
VALUES (LOAD_FILE('/var/lib/mysql-files/celeste5.jpeg'), 'celeste5.jpeg', 'image/jpeg');

INSERT INTO Image(data, file_name, mime_type)
VALUES (LOAD_FILE('/var/lib/mysql-files/hollow_knight1.jpg'), 'hollow_knight1.jpg', 'image/jpeg');

INSERT INTO Image(data, file_name, mime_type)
VALUES (LOAD_FILE('/var/lib/mysql-files/hollow_knight2.jpg'), 'hollow_knight2.jpg', 'image/jpeg');

INSERT INTO Image(data, file_name, mime_type)
VALUES (LOAD_FILE('/var/lib/mysql-files/hollow_knight3.jpg'), 'hollow_knight3.jpg', 'image/jpeg');

#--- Logos de publicadoras e desenvolvedoras ---#

INSERT INTO Image(data, file_name, mime_type)
VALUES (LOAD_FILE('/var/lib/mysql-files/logo_aggro_crab.PNG'), 'logo_aggro_crab.PNG', 'image/png');

INSERT INTO Image(data, file_name, mime_type)
VALUES (LOAD_FILE('/var/lib/mysql-files/logo_concernedape.jpg'), 'logo_concernedape.jpg', 'image/jpeg');

INSERT INTO Image(data, file_name, mime_type)
VALUES (LOAD_FILE('/var/lib/mysql-files/logo_extremely_ok_games.png'), 'logo_extremely_ok_games.png', 'image/png');

INSERT INTO Image(data, file_name, mime_type)
VALUES (LOAD_FILE('/var/lib/mysql-files/logo_game_freak.jpg'), 'logo_game_freak.jpg', 'image/jpeg');

INSERT INTO Image(data, file_name, mime_type)
VALUES (LOAD_FILE('/var/lib/mysql-files/logo_nintendo.png'), 'logo_nintendo.png', 'image/png');

INSERT INTO Image(data, file_name, mime_type)
VALUES (LOAD_FILE('/var/lib/mysql-files/logo_team_cherry.jpg'), 'logo_team_cherry.jpg', 'image/jpeg');

INSERT INTO Image(data, file_name, mime_type)
VALUES (LOAD_FILE('/var/lib/mysql-files/logo_team17.jpg'), 'logo_team17.jpg', 'image/jpeg');

INSERT INTO Image(data, file_name, mime_type)
VALUES (LOAD_FILE('/var/lib/mysql-files/logo_zaum.png'), 'logo_zaum.png', 'image/png');

#--- Fotos de consoles ---#

INSERT INTO Image(data, file_name, mime_type)
VALUES (LOAD_FILE('/var/lib/mysql-files/pc_picture.jpg'), 'pc_picture.jpg', 'image/jpeg');

INSERT INTO Image(data, file_name, mime_type)
VALUES (LOAD_FILE('/var/lib/mysql-files/ps4_picture.jpg'), 'ps4_picture.jpg', 'image/jpeg');

INSERT INTO Image(data, file_name, mime_type)
VALUES (LOAD_FILE('/var/lib/mysql-files/switch_picture.jpg'), 'switch_picture.jpg', 'image/jpeg');

INSERT INTO Image(data, file_name, mime_type)
VALUES (LOAD_FILE('/var/lib/mysql-files/wii_u_picture.jpg'), 'wii_u_picture.jpg', 'image/jpeg');

INSERT INTO Image(data, file_name, mime_type)
VALUES (LOAD_FILE('/var/lib/mysql-files/xbox_one_picture.jpg'), 'xbox_one_picture.jpg', 'image/jpeg');

#--- Fotos para notícias ---#

INSERT INTO Image(data, file_name, mime_type)
VALUES (LOAD_FILE('/var/lib/mysql-files/news_1_wii.jpg'), 'news_1_wii.jpg', 'image/jpeg');

INSERT INTO Image(data, file_name, mime_type)
VALUES (LOAD_FILE('/var/lib/mysql-files/news_2_arceus_anime.jpg'), 'news_2_arceus_anime.jpg', 'image/jpeg');

INSERT INTO Image(data, file_name, mime_type)
VALUES (LOAD_FILE('/var/lib/mysql-files/news_3_xbox_bethesda.jpg'), 'news_3_xbox_bethesda.jpg', 'image/jpeg');

INSERT INTO Image(data, file_name, mime_type)
VALUES (LOAD_FILE('/var/lib/mysql-files/news_4_playstation_plus.jpg'), 'news_4_playstation_plus.jpg', 'image/jpeg');

INSERT INTO Image(data, file_name, mime_type)
VALUES (LOAD_FILE('/var/lib/mysql-files/news_5_old_game.png'), 'news_5_old_game.png', 'image/png');

#-------------------- Usuários --------------------#

INSERT INTO User(user_email, password, full_name, role, profile_picture)
VALUES ('admin@bossow.com', 'admin123', 'Admin', 'admin', 2);

INSERT INTO User(user_email, password, full_name, role, profile_picture)
VALUES ('maria_testadora@bossow.com', 'teste123', 'Maria Testadora', 'user', 3);

INSERT INTO User(user_email, password, full_name, role, profile_picture)
VALUES ('bowser_voador@bossow.com', 'teste123', 'Bowser Voador', 'user', 4);

INSERT INTO User(user_email, password, full_name, role, profile_picture)
VALUES ('joana_silva@bossow.com', 'teste123', 'Joana Silva', 'user', 5);

INSERT INTO User(user_email, password, full_name, role, profile_picture)
VALUES ('luigi_fantasma@bossow.com', 'teste123', 'Luigi Fantasma', 'user', 6);

#-------------------- Desenvolvedora --------------------#

INSERT INTO Developer(developer_name, headquarters, foundation_date, logo_picture)
VALUES ('Nintendo EPD', 'Kyoto, Japão', '1983-09-30 00:00:00', 27);

INSERT INTO Developer(developer_name, headquarters, foundation_date, logo_picture)
VALUES ('Extremely OK Games', 'Vancouver, Canadá', '2019-09-05 00:00:00', 25);

INSERT INTO Developer(developer_name, headquarters, foundation_date, logo_picture)
VALUES ('ZA/UM', 'Londres, Inglaterra', '2016-01-01 00:00:00', 30);

INSERT INTO Developer(developer_name, headquarters, foundation_date, logo_picture)
VALUES ('Aggro Crab Games', 'Seattle, EUA', '2019-01-01 00:00:00', 23);

INSERT INTO Developer(developer_name, headquarters, foundation_date, logo_picture)
VALUES ('Team Cherry', 'Adelaide, Austrália', '2014-01-01 00:00:00', 28);

INSERT INTO Developer(developer_name, headquarters, foundation_date, logo_picture)
VALUES ('Game Freak', 'Tóquio, Japão', '1989-04-26 00:00:00', 26);

INSERT INTO Developer(developer_name, headquarters, foundation_date, logo_picture)
VALUES ('ConcernedApe', 'Los Angeles, EUA', '2012-01-01 00:00:00', 24);

#-------------------- Publicadoras --------------------#

INSERT INTO Publisher(publisher_name, headquarters, foundation_date, logo_picture)
VALUES ('Nintendo', 'Kyoto, Japão', '1889-09-23 00:00:00', 27);

INSERT INTO Publisher(publisher_name, headquarters, foundation_date, logo_picture)
VALUES ('Extremely OK Games', 'Vancouver, Canadá', '2019-09-05 00:00:00', 25);

INSERT INTO Publisher(publisher_name, headquarters, foundation_date, logo_picture)
VALUES ('ZA/UM', 'Londres, Inglaterra', '2016-01-01 00:00:00', 30);

INSERT INTO Publisher(publisher_name, headquarters, foundation_date, logo_picture)
VALUES ('Team17', 'Wakefield, Inglaterra', '1990-12-07 00:00:00', 28);

INSERT INTO Publisher(publisher_name, headquarters, foundation_date, logo_picture)
VALUES ('Team Cherry', 'Adelaide, Austrália', '2014-01-01 00:00:00', 28);

INSERT INTO Publisher(publisher_name, headquarters, foundation_date, logo_picture)
VALUES ('ConcernedApe', 'Los Angeles, EUA', '2012-01-01 00:00:00', 24);

#-------------------- Jogos --------------------#

INSERT INTO Game(game_title, release_date, description, developer_id, publisher_id, trailer_url, cover_picture)
VALUES ('The Legend of Zelda: Breath of the Wild', '2017-03-03 00:00:00', 'Hyrule regrediu a um estado medieval. Dez mil anos depois, os hyrulianos leram as profecias de seus ancestrais e reconheceram os sinais do retorno de Ganon, escavando e recuperando as Feras Divinas e os Guardiões.', 1, 1, 'https://www.youtube.com/watch?v=1rPxiXXxftE', 7);

INSERT INTO Game(game_title, release_date, description, developer_id, publisher_id, trailer_url, cover_picture)
VALUES ('Celeste', '2018-01-25 00:00:00', 'A trama acompanha a história de Madeline, uma jovem garota que resolveu, em um ato imprudente, escalar até o topo da montanha Celeste apenas para provar para si mesma de que ela era capaz.', 2, 2, 'https://www.youtube.com/watch?v=iofYDsA2yqg', 8);

INSERT INTO Game(game_title, release_date, description, developer_id, publisher_id, trailer_url, cover_picture)
VALUES ('Disco Elysium', '2019-10-15 00:00:00', 'O jogo se passa na fictícia cidade de Revachol, mais especificamente no bairro costal de Martinaise, cheio de crime, pobreza e corrupção, controlada pelo corrupto Sindicato dos estivadores.', 3, 3, 'https://www.youtube.com/watch?v=YV2lp6p_gXw', 9);

INSERT INTO Game(game_title, release_date, description, developer_id, publisher_id, trailer_url, cover_picture)
VALUES ('Going Under', '2020-09-23 00:00:00', 'Going Under é um dungeon crawler roguelike satírico baseado na cultura de startups de tecnologia, usando-se de trocadilhos deste mundo tanto nos diálogos, quanto na mecânica e no design dos personagens rendendo boas risadas.', 4, 4, 'https://www.youtube.com/watch?v=nKLELV7YLns', 10);

INSERT INTO Game(game_title, release_date, description, developer_id, publisher_id, trailer_url, cover_picture)
VALUES ('Hollow Knight', '2017-02-24 00:00:00', 'Hollow Knight conta a historia de um diminuto guerreiro que decide entrar nas cavernas que abrigam as ruínas do reino de Hallownest. Devido à uma infestação que roubou os insetos de sua inteligência e os reverteu aos seus instintos primitivos, uma nação foi destruída.', 5, 5, 'https://www.youtube.com/watch?v=kWo5g-tsBNk', 11);

INSERT INTO Game(game_title, release_date, description, developer_id, publisher_id, trailer_url, cover_picture)
VALUES ('Pokémon Legends: Arceus', '2022-01-28 00:00:00', 'A trama é ambientada em uma época em que Pokémon e humanos viviam separados. Nesse contexto, surge um time de pesquisa que decide estudar e aprender mais sobre os Pokémon. Este grupo é chamado de Galaxy Team.', 6, 1, 'https://www.youtube.com/watch?v=SbIA8FKhwl0', 12);

INSERT INTO Game(game_title, release_date, description, developer_id, publisher_id, trailer_url, cover_picture)
VALUES ('Stardew Valley', '2016-02-26 00:00:00', 'É um jogo de simulação de fazenda, onde o jogador pode selecionar um de cinco tipos de fazenda de acordo com sua preferência, como uma com mais oportunidades de pilhamento da terra, uma com mais recursos de mineração e outra com um rio de pesca.', 7, 6, 'https://www.youtube.com/watch?v=8A7A1X1TVNc', 13);

INSERT INTO Game(game_title, release_date, description, developer_id, publisher_id, trailer_url, cover_picture)
VALUES ('Super Mario 3D World', '2013-11-21 00:00:00', 'Mario, Luigi, Princesa Peach e Toad estão caminhando no Reino dos Cogumelos, quando veem um cano transparente, Mario e Luigi consertam-o, e dele saem vários objetos. No final, uma Anafada sai do cano desesperada, contando que Bowser invadiu o reino e capturou as outras seis princesas.', 1, 1, 'https://www.youtube.com/watch?v=wLOKVABfrzw', 14);

#-------------------- Biblioteca de jogos --------------------#

INSERT INTO Library(user_id, game_id, hours_played, completion_percentage, last_logged_in)
VALUES (1, 1, 43, 30, '2020-01-01 00:00:00');

INSERT INTO Library(user_id, game_id, hours_played, completion_percentage, last_logged_in)
VALUES (1, 2, 8, 63, '2020-01-01 00:00:00');

INSERT INTO Library(user_id, game_id, hours_played, completion_percentage, last_logged_in)
VALUES (1, 3, 25, 89, '2020-01-01 00:00:00');

INSERT INTO Library(user_id, game_id, hours_played, completion_percentage, last_logged_in)
VALUES (2, 1, 65, 52, '2020-01-01 00:00:00');

INSERT INTO Library(user_id, game_id, hours_played, completion_percentage, last_logged_in)
VALUES (2, 3, 31, 91, '2020-01-01 00:00:00');

INSERT INTO Library(user_id, game_id, hours_played, completion_percentage, last_logged_in)
VALUES (2, 4, 24, 77, '2020-01-01 00:00:00');

INSERT INTO Library(user_id, game_id, hours_played, completion_percentage, last_logged_in)
VALUES (2, 6, 31, 72, '2020-01-01 00:00:00');

INSERT INTO Library(user_id, game_id, hours_played, completion_percentage, last_logged_in)
VALUES (3, 1, 12, 10, '2020-01-01 00:00:00');

INSERT INTO Library(user_id, game_id, hours_played, completion_percentage, last_logged_in)
VALUES (3, 5, 78, 71, '2020-01-01 00:00:00');

INSERT INTO Library(user_id, game_id, hours_played, completion_percentage, last_logged_in)
VALUES (3, 7, 143, 89, '2020-01-01 00:00:00');

INSERT INTO Library(user_id, game_id, hours_played, completion_percentage, last_logged_in)
VALUES (3, 8, 31, 92, '2020-01-01 00:00:00');

INSERT INTO Library(user_id, game_id, hours_played, completion_percentage, last_logged_in)
VALUES (4, 1, 98, 92, '2020-01-01 00:00:00');

INSERT INTO Library(user_id, game_id, hours_played, completion_percentage, last_logged_in)
VALUES (4, 2, 12, 41, '2020-01-01 00:00:00');

INSERT INTO Library(user_id, game_id, hours_played, completion_percentage, last_logged_in)
VALUES (4, 5, 64, 73, '2020-01-01 00:00:00');

INSERT INTO Library(user_id, game_id, hours_played, completion_percentage, last_logged_in)
VALUES (4, 6, 43, 94, '2020-01-01 00:00:00');

INSERT INTO Library(user_id, game_id, hours_played, completion_percentage, last_logged_in)
VALUES (4, 8, 33, 85, '2020-01-01 00:00:00');

INSERT INTO Library(user_id, game_id, hours_played, completion_percentage, last_logged_in)
VALUES (5, 1, 54, 39, '2020-01-01 00:00:00');

INSERT INTO Library(user_id, game_id, hours_played, completion_percentage, last_logged_in)
VALUES (5, 3, 38, 95, '2020-01-01 00:00:00');

INSERT INTO Library(user_id, game_id, hours_played, completion_percentage, last_logged_in)
VALUES (5, 4, 35, 99, '2020-01-01 00:00:00');

INSERT INTO Library(user_id, game_id, hours_played, completion_percentage, last_logged_in)
VALUES (5, 5, 82, 78, '2020-01-01 00:00:00');

INSERT INTO Library(user_id, game_id, hours_played, completion_percentage, last_logged_in)
VALUES (5, 7, 234, 100, '2020-01-01 00:00:00');

#-------------------- Capturas de tela --------------------#

INSERT INTO Screenshot(pic_id, user_id, game_id)
VALUES (15, 1, 2);

INSERT INTO Screenshot(pic_id, user_id, game_id)
VALUES (16, 1, 2);

INSERT INTO Screenshot(pic_id, user_id, game_id)
VALUES (17, 1, 2);

INSERT INTO Screenshot(pic_id, user_id, game_id)
VALUES (18, 1, 2);

INSERT INTO Screenshot(pic_id, user_id, game_id)
VALUES (19, 1, 2);

INSERT INTO Screenshot(pic_id, user_id, game_id)
VALUES (20, 3, 5);

INSERT INTO Screenshot(pic_id, user_id, game_id)
VALUES (21, 3, 5);

INSERT INTO Screenshot(pic_id, user_id, game_id)
VALUES (22, 3, 5);

#-------------------- Avaliações --------------------#

INSERT INTO Review(user_id, game_id, review_text, score)
VALUES (1, 1, 'Apenas o melhor jogo já feito... Mais de 100 horas e ainda tô longe dos 100%.', 5);

INSERT INTO Review(user_id, game_id, review_text, score)
VALUES (1, 2, 'Difícil demais para o meu gosto, mas sem dúvida muito bom e bonito.', 4);

INSERT INTO Review(user_id, game_id, review_text, score)
VALUES (1, 5, 'Melhor metroidvania que já joguei - e praticamente de graça, 30 reais por mais de 50h de gameplay.', 5);

INSERT INTO Review(user_id, game_id, review_text, score)
VALUES (2, 1, 'Exploração literalmente infinita. Jogo de Zelda de mundo aberto que até quem não gosta de mundo aberto ou jogo de Zelda vai curtir.', 5);

INSERT INTO Review(user_id, game_id, review_text, score)
VALUES (2, 3, 'Muito raro achar algo (livro, filme, jogo) tão bem escrito e pensado. Ainda mais raro ver um jogo tratando temas tão complexos como aqui.', 5);

INSERT INTO Review(user_id, game_id, review_text, score)
VALUES (2, 6, 'História fraca, diálogos mais fracos ainda. Gráficos inconsistentes - às vezes bonitos, às vezes feios. Tinha tudo para ser bom mas foi ruim.', 1);

INSERT INTO Review(user_id, game_id, review_text, score)
VALUES (2, 7, 'Me sinto de volta ao Colheita Feliz, mas sem a possibilidade de interação online com mais de 100 amigos no Orkut. Barato, mas não empolga.', 2);

INSERT INTO Review(user_id, game_id, review_text, score)
VALUES (3, 1, 'Impossível alguém dar menos que 5/5 pra BOTW.', 5);

INSERT INTO Review(user_id, game_id, review_text, score)
VALUES (3, 7, 'Viciante - se inspira e melhora as mecânicas de Harvest Moon. E também é de graça - mais de 100h de gameplay fácil.', 5);

INSERT INTO Review(user_id, game_id, review_text, score)
VALUES (3, 8, 'Meu Mario 3D favorito. É o único Mario 3D que é de fato uma versão 3D do jogo em 2D, pegando toda a jogabilidade dos Marios clássicos e jogando para um 3D.', 5);

INSERT INTO Review(user_id, game_id, review_text, score)
VALUES (4, 1, 'Como assim as armas quebram? Jogo de 2017 com esses gráficos? Patético.', 2);

INSERT INTO Review(user_id, game_id, review_text, score)
VALUES (4, 2, 'Arte muito bonita e jogabilidade interessante.', 5);

INSERT INTO Review(user_id, game_id, review_text, score)
VALUES (4, 4, 'Divertido e viciante, e ainda carregado de críticas à exploração no ambiente de trabalho.', 5);

INSERT INTO Review(user_id, game_id, review_text, score)
VALUES (4, 6, 'O mais perto de mundo aberto que Pokémon já chegou - o que é incrível.', 5);

INSERT INTO Review(user_id, game_id, review_text, score)
VALUES (4, 8, 'Não é tão bom quanto os outros Super Mario 3D, principalmente o Odyssey, mas ainda assim é mto detalhado e rico.', 4);

#-------------------- Denúncias --------------------#

INSERT INTO Complaint(user_id, game_id, complaint_type, complaint_text)
VALUES (2, 1, 'change', 'Enredo mal escrito, precisa encontrar um texto que resuma melhor o que se passa no jogo.');

INSERT INTO Complaint(user_id, game_id, complaint_type, complaint_text)
VALUES (2, 2, 'change', 'Faltou mencionar em alguma parte que uma equipe brasileira trabalhou na arte do jogo.');

INSERT INTO Complaint(user_id, game_id, complaint_type, complaint_text)
VALUES (3, 3, 'delete', 'Esse jogo tem cenas para maiores de 18 anos. Como essa é uma plataforma aberta, acho que qualquer jogo que não tenha indicação livre precisa ser apagado daqui.');

INSERT INTO Complaint(user_id, game_id, complaint_type, complaint_text)
VALUES (3, 7, 'change', 'Existem trailers muito mais completos que vocês poderiam colocar para Stardew Valley.');

INSERT INTO Complaint(user_id, game_id, complaint_type, complaint_text)
VALUES (4, 8, 'change', 'Poderiam atualizar a edição aqui. Já lançaram uma edição completa do jogo no Switch, mas aí está a versão para o Wii U.');

INSERT INTO Complaint(user_id, game_id, complaint_type, complaint_text, solved)
VALUES (3, 1, 'delete', 'Tem muitos 5 na avaliação, acho que é melhor apagar a página e recriar do 0.', 1);

INSERT INTO Complaint(user_id, game_id, complaint_type, complaint_text, solved)
VALUES (3, 2, 'delete', 'Jogo fala sobre depressão... Não acho que esse tipo de conteúdo devesse estar aqui no Bossow.', 1);

INSERT INTO Complaint(user_id, game_id, complaint_type, complaint_text, solved)
VALUES (4, 4, 'delete', 'Quase ninguém joga esse jogo, pra que ter na plataforma???', 1);

#-------------------- Lembretes --------------------#

INSERT INTO Note(user_id, note_text)
VALUES (1, 'Checar todas as denúncias e solucioná-las.');

INSERT INTO Note(user_id, note_text)
VALUES (2, 'Comprar Switch Sports na pré-venda na Amazon!');

INSERT INTO Note(user_id, note_text)
VALUES (3, 'Zerar Super Mario 3D World logo.');

INSERT INTO Note(user_id, note_text)
VALUES (4, 'Encher o saco do administrador para ele excluir BOTW daqui logo.');

INSERT INTO Note(user_id, note_text)
VALUES (4, 'Adicionar Pokémon Scarlet no catálogo do Bossow.');

#-------------------- Consoles --------------------#

INSERT INTO Console(console_name, specifications, developer, release_date, product_picture)
VALUES ('Nintendo Switch', 'ARM 4 Cortex-A57 cores @', 'Nintendo', '2017-03-03 00:00:00', 32);

INSERT INTO Console(console_name, specifications, developer, release_date, product_picture)
VALUES ('Wii U', '1.24 GHz Tri-Core IBM', 'Nintendo', '2012-11-18 00:00:00', 33);

INSERT INTO Console(console_name, specifications, developer, release_date, product_picture)
VALUES ('PlayStation 4', 'Semi-custom 8-core AMD x86-64 Jaguar 1.6 GHz CPU', 'Sony', '2013-11-15 00:00:00', 31);

INSERT INTO Console(console_name, specifications, developer, release_date, product_picture)
VALUES ('PC', 'Undefined', 'Undefined', '1990-01-01 00:00:00', 30);

INSERT INTO Console(console_name, specifications, developer, release_date, product_picture)
VALUES ('Xbox One', 'Custom 1.75 GHz AMD 8-core APU', 'Microsoft', '2013-11-22 00:00:00', 34);

#-------------------- Disponibilidade --------------------#

INSERT INTO Available(game_id, console_id)
VALUES (1, 1);

INSERT INTO Available(game_id, console_id)
VALUES (1, 2);

INSERT INTO Available(game_id, console_id)
VALUES (2, 1);

INSERT INTO Available(game_id, console_id)
VALUES (2, 3);

INSERT INTO Available(game_id, console_id)
VALUES (2, 4);

INSERT INTO Available(game_id, console_id)
VALUES (2, 5);

INSERT INTO Available(game_id, console_id)
VALUES (3, 1);

INSERT INTO Available(game_id, console_id)
VALUES (3, 3);

INSERT INTO Available(game_id, console_id)
VALUES (3, 4);

INSERT INTO Available(game_id, console_id)
VALUES (3, 5);

INSERT INTO Available(game_id, console_id)
VALUES (4, 1);

INSERT INTO Available(game_id, console_id)
VALUES (4, 3);

INSERT INTO Available(game_id, console_id)
VALUES (4, 4);

INSERT INTO Available(game_id, console_id)
VALUES (4, 5);

INSERT INTO Available(game_id, console_id)
VALUES (5, 1);

INSERT INTO Available(game_id, console_id)
VALUES (5, 3);

INSERT INTO Available(game_id, console_id)
VALUES (5, 4);

INSERT INTO Available(game_id, console_id)
VALUES (5, 5);

INSERT INTO Available(game_id, console_id)
VALUES (6, 1);

INSERT INTO Available(game_id, console_id)
VALUES (7, 1);

INSERT INTO Available(game_id, console_id)
VALUES (7, 3);

INSERT INTO Available(game_id, console_id)
VALUES (7, 4);

INSERT INTO Available(game_id, console_id)
VALUES (7, 5);

INSERT INTO Available(game_id, console_id)
VALUES (8, 1);

INSERT INTO Available(game_id, console_id)
VALUES (8, 2);

#-------------------- Notícias --------------------#

INSERT INTO News(news_title, news_text, news_picture, author_id)
VALUES ('Nintendo Switch supera vendas de Wii', 'De acordo com o relatório financeiro da Nintendo para o terceiro trimestre do ano fiscal, que termina em março de 2022, a empresa divulgou que 103,54 milhões unidades do Nintendo Switch foram vendidas até 31 de dezembro de 2021. Isso significa que o Switch ultrapassou a grandiosa marca de vendas do Wii.', 35, 1);

INSERT INTO News(news_title, news_text, news_picture, author_id)
VALUES ('Pokémon ganha nova série inspirada em Legends: Arceus', 'A The Pokémon Company compartilhou novas informações da série Pokémon: As Neves de Hisui, que foi brevemente apresentado em um Pokémon Presents no Dia do Pokémon 2022. A web-série estreia em 18 de maio, com o primeiro episódio da animação de três partes chegando ao Pokémon TV e ao canal de YouTube de Pokémon.', 36, 1);

INSERT INTO News(news_title, news_text, news_picture, author_id)
VALUES ('Xbox e Bethesda farão apresentação em junho', 'O Xbox & Bethesda Games Showcase focará em títulos da Xbox Game Studios, Bethesda e estúdios parceiros (third-party). Fãs da publisher adquirida pela Microsoft antecipam games como Starfield, previsto para o final deste ano, bem como algo de novo de The Elder Scrolls 6, já que a nova geração de consoles está estabelecida no mercado.', 37, 1);

INSERT INTO News(news_title, news_text, news_picture, author_id)
VALUES ('PlayStation exige que estúdios criem demos de 2 horas para novos jogos', 'De acordo com um relatório da Game Developer, muitos estúdios receberam esta notícia em uma nova atualização no portal de desenvolvedores da Sony e, supostamente, não houve nenhuma comunicação anterior sobre tal mudança. Esta nova política não se aplica retroativamente, nem aos jogos do PlayStation VR. No entanto, os desenvolvedores que planejam lançar jogos para PlayStation no futuro terão que aderir a essas diretrizes atualizadas.', 38, 1);

INSERT INTO News(news_title, news_text, news_picture, author_id)
VALUES ('PS4, PS5: PlayStation cria time de preservação de games', 'Revelado por meio das publicações de um novo funcionário no Twitter e LinkedIn (conforme apontado pelo Video Games Chronicle), a divisão focará na preservação de Propriedades Intelectuais (PI) da PlayStation para "garantir que a história da nossa indústria não seja esquecida".', 39, 1);