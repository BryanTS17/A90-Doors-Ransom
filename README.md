A90 Doors Ransom

Projeto desenvolvido em Python, inspirado no A-90 do jogo DOORS, com uma experiência de terror baseada em sustos, imagens, sons, vídeos e janelas interativas.

A proposta é explorar a criação de uma experiência de terror para desktop, utilizando elementos visuais inspirados no personagem A-90 e situações inesperadas para surpreender o usuário.

Sobre o projeto

O A90 Doors Ransom é um projeto experimental que combina interface gráfica, reprodução de mídia, temporizadores e automação para criar uma experiência inspirada em jogos de terror.

Durante a execução, o programa apresenta elementos visuais e sonoros, janelas que aparecem em posições aleatórias e animações que simulam situações caóticas na área de trabalho.

O projeto foi desenvolvido principalmente para praticar Python, trabalhar com interfaces gráficas e experimentar diferentes recursos da linguagem.

Funcionalidades

Janelas interativas: criação de janelas com imagens temáticas, tamanhos variados e posições aleatórias.

Efeitos visuais: janelas sem bordas, imagens redimensionáveis e movimentos que simulam tremores.

Reprodução de mídia: exibição de vídeos em tela cheia e reprodução de efeitos sonoros e música.

Temporizadores: utilização de eventos temporizados para coordenar diferentes acontecimentos.

Elementos interativos: moedas clicáveis que alteram a pontuação exibida na interface.

Automação: experimentos com movimentação do mouse por meio de bibliotecas Python.

Gerenciamento de janelas: controle de múltiplas janelas e encerramento de componentes da aplicação.

Tecnologias utilizadas

Python: linguagem principal do projeto.

PySide6: criação de interfaces gráficas e gerenciamento de janelas.

Qt Multimedia: reprodução de áudio e vídeo.

PyAutoGUI: acesso às dimensões da tela e automação do mouse.

pynput: monitoramento de eventos do mouse.

threading: execução de tarefas em threads.

random: geração de posições e escolhas aleatórias.

Bibliotecas padrão do Python: utilização de módulos como os, sys, subprocess, ctypes, winreg e pathlib.

Organização do projeto

O código é dividido em módulos para separar responsabilidades:

Arquivo

Responsabilidade

main.py

Coordena a execução principal e os eventos do programa.

JanelaMain.py

Implementa a janela principal, o cronômetro e a pontuação.

JanelaPopUp.py

Cria janelas com imagens e efeitos de movimento.

JanelaPopUpEstica.py

Implementa janelas com dimensões aleatórias.

JanelaCara.py

Gerencia janelas com imagens do A-90.

JanelaMoedas.py

Implementa as moedas clicáveis.

JanelaVideo.py

Reproduz vídeos em uma janela de tela cheia.

JanelaThank.py

Exibe a janela final da experiência.

VariasJanelas.py

Organiza a criação de sequências de janelas.

Automacao.py

Contém a função de movimentação aleatória do mouse.

Wallpaper.py

Contém funções para consultar, alterar e restaurar o papel de parede.

Sons.py

Centraliza o carregamento e o controle dos sons.

BG.py

Organiza os caminhos dos recursos visuais.

Globais.py

Armazena variáveis compartilhadas entre os módulos.

Label.py

Define um componente de imagem que emite um sinal ao ser clicado.

Os recursos utilizados pelo programa, como imagens, sons e vídeos, ficam em pastas próprias e são carregados durante a execução.

Aprendizados e objetivos técnicos

Este projeto permitiu praticar conceitos importantes de desenvolvimento de software, incluindo:

Programação orientada a objetos com classes e herança.

Organização de código em módulos Python.

Construção de interfaces gráficas com PySide6.

Uso de sinais e eventos para conectar componentes.

Programação orientada a eventos com QTimer.

Gerenciamento do ciclo de vida de janelas.

Reprodução de áudio e vídeo.

Manipulação de arquivos e recursos externos.

Integração com funcionalidades do Windows.

Uso de funções, listas, módulos e bibliotecas externas.

Aviso de segurança

Este projeto não deve ser considerado inofensivo em sua versão atual.

Embora tenha sido criado como uma experiência de terror inspirada em um jogo, o código contém operações que podem interferir no uso normal do computador. Entre elas estão a alteração do papel de parede, a abertura de múltiplas janelas e terminais, a movimentação do mouse e um comando de desligamento imediato do sistema.

Execute somente após revisar o código e compreender seus efeitos. Não utilize em computadores de terceiros ou em ambientes com arquivos importantes. Para uma versão segura de demonstração, essas operações devem ser removidas ou substituídas por simulações visuais.

Objetivo

O objetivo do projeto é explorar os recursos de Python para criar experiências interativas, praticar desenvolvimento desktop e compreender como diferentes módulos podem trabalhar juntos em uma aplicação.

O repositório também serve como registro da minha evolução na programação e dos desafios técnicos explorados durante o desenvolvimento.

Desenvolvido por Bryan Tavares

Projeto pessoal para estudo e experimentação com Python.
