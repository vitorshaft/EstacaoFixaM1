# EstacaoFixaM1

PROJETO DE COMUNICAÇÃO ENTRE RASPBERRY PI 3B+ EM MECANISMO DE POSIÇAO DE ANTENA E PC NA MESMA REDE:

=================== NO RASPBERRY =============================
(VIDE REPO https://github.com/vitorshaft/RaspFixaM1)

1. INSTALAR módulo "vsftpd" no Raspberry:
  $ sudo pip install vsftpd
2. CRIAR PASTA FTP PARA COMPARTILHAMENTO:
  $ mkdir FTP
  $ cd FTP


==================== NO PC ==================================

4. ABRIR ARQUIVO E INSERIR IP DO RASPBERRY NA REDE LOCAL e nome do arquivo em "filename"
5. ABRIR PROMPT/TERMINAL NA PASTA DO PROJETO E EXECUTAR:
  $ python Main.py
