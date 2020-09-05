#!/usr/bin/python3

from os import environ, chown
import sys
from pathlib import Path
from pwd import getpwnam

import markdown

usuario = environ['SUDO_USER']
dados_usuario = getpwnam(usuario)
nome = dados_usuario.pw_gecos
uid = dados_usuario.pw_uid
gid = dados_usuario.pw_gid
prim_nome = nome.split()[0]

if ',' in nome:
    nome = nome.split(',')[0]
else:
    sys.exit()

site = Path(f'/var/www/html/estudante/{usuario}')

if site.exists():
    print(f'''{prim_nome}, você já tem um site na Mange.

Para acessá-lo, visite <https://mange.ifrn.edu.br/estudante/{usuario}/>.

Para manipular as páginas de seu site, entre no diretório: `/var/www/html/estudante/{usuario}/`

''')
else:
    site.mkdir()
    chown(site, uid, gid)
    site.chmod(0o755)
    conteudo_md = f'''# Site de {nome}

Caro visitante,

Este não é um site oficial do [IFRN](http://portal.ifrn.edu.br). Ele foi criado meramente para que {nome} possa praticar a criação e hospedagem de páginas HTML e navegar em um sistema de arquivos via linha de comando (CLI).

## Mensagem para {nome}

Caro(a) {prim_nome},

Para manipular as páginas de seu site, entre no diretório `/var/www/html/estudante/{usuario}` do servidor SSH.

'''

    leiame = site / 'README.html'
    leiame.touch()
    md = markdown.Markdown(output_format='html')
    with open(leiame, 'w', encoding='utf-8') as arq_html:
        arq_html.write(md.convert(conteudo_md))

    leiame.chmod(0o755)
    system(f'chmod 755 {leiame.as_posix()}')
    print(f'''{prim_nome}, agora você tem um site na Mange.

Para acessá-lo, visite <https://mange.ifrn.edu.br/estudante/{usuario}/>.

Para manipular as páginas de seu site, entre no diretório: `/var/www/html/estudante/{usuario}/`

''')
