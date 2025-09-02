# Pautas Pitorescas – Estilo Tabloide

## Como usar
1. Suba este pacote no GitHub em um repositório público.
2. Vá em Settings -> Pages -> Branch main, pasta /docs.
3. Vá em Settings -> Actions -> General -> Read and write permissions.
4. O site ficará em https://SEU_USUARIO.github.io/NOME_REPO

## O que faz
- `generator.py`: cria páginas diárias em docs/posts/ (estilo tabloide).
- `column_stub.py`: cria coluna semanal em docs/colunas/ (assinada por @otaldefelipeloureiro).
- `style.css`: define a estética de tabloide (vermelho/preto/branco).
- `.github/workflows/build.yml`: agenda execuções diárias e semanais automáticas.
