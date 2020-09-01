#!/bin/bash

source /etc/dysconta.conf

usuario_tmp=${SUDO_USER/./_}
senha_bd=$(pwgen -1)
echo "Escolha 3 ou 2 caracteres para diferenciar seu BD. Exemplos: wp para WordPress ou mdl para Moodle"
echo -n "Digite os caracteres: "
read prefixo
nome_bd="${prefixo}_${usuario_tmp}"
usuario_bd="usuario_${nome_bd}"



# A primeira linha se chama SHEBANG
mysql --user=root --password='${ROOT_PASS}' << FIM
CREATE DATABASE ${nome_bd} CHARACTER SET utf8 COLLATE utf8_general_ci;
GRANT ALL ON ${nome_bd}.* TO '${usuario_bd}'@'localhost' IDENTIFIED BY '${senha_bd}';
FLUSH PRIVILEGES;

FIM

cat << FIM
Parabéns! Foi criado um banco de dados para você. Seguem os dados:
* Nome do banco de dados: ${nome_bd}
* Nome do usuário p/ acesso ao banco: ${usuario_bd}
* Senha p/ usuário: ${senha_bd}
FIM
