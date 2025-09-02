# Pautas Pitorescas – Edição Tabloide

## Estrutura
- `feeds.txt`: lista de portais brasileiros e tabloides internacionais.
- `requirements.txt`: dependências mínimas (feedparser, python-dateutil).
- `style.css`: estilo tabloide (vermelho/preto/branco).
- `generator.py`: gera posts diários em docs/posts/.
- `column_stub.py`: cria colunas semanais em docs/colunas/, assinadas por @otaldefelipeloureiro.
- `docs/index.html`: página inicial.
- `docs/edicao-zero.html`: capa especial de lançamento.

## Como publicar
1. Suba todos os arquivos deste pacote no GitHub.
2. Vá em Settings -> Pages -> Branch main, pasta /docs.
3. Vá em Settings -> Actions -> General -> Read and write permissions.
4. O site ficará em https://SEU_USUARIO.github.io/NOME_REPO
