# EstacaoFixaM1

PROJETO DE COMUNICAÇÃO ENTRE RASPBERRY PI 3B+ EM MECANISMO DE POSIÇAO DE ANTENA E PC NA MESMA REDE:

=================== NO RASPBERRY =============================

1. INSTALAR módulo "vsftpd" no Raspberry:
  $ sudo pip install vsftpd
2. CRIAR PASTA FTP PARA COMPARTILHAMENTO:
  $ mkdir FTP
  $ cd FTP
3. INICIAR SERVIÇO FTP NA PASTA CRIADA PARA COMPARTILHAMENTO:
  $ sudo /etc/init.d/vsftpd start

==================== NO PC ==================================

4. ABRIR ARQUIVO E INSERIR IP DO RASPBERRY NA REDE LOCAL e nome do arquivo em "filename"
5. ABRIR PROMPT/TERMINAL NA PASTA DO PROJETO E EXECUTAR:
  $ python ftp_cliente.py
