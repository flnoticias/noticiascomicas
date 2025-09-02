import os, datetime, pathlib

ROOT = pathlib.Path(__file__).resolve().parent
DOCS = ROOT / "docs" / "posts"

def main():
    today = datetime.date.today().isoformat()
    html = f"""<!doctype html>
<html><head><meta charset='utf-8'><title>Pautas de {today}</title>
<link rel="stylesheet" href="../style.css"></head>
<body>
<h1>Pautas Pitorescas</h1>
<h2>{today}</h2>
<div class='card'>
  <h3>Homem tenta assaltar com melancia na cabeça</h3>
  <div class='meta'>Por que é pitoresco: Disfarce digno de desenho animado.</div>
  <p><b>Gancho setup:</b> No Brasil isso se chama quarta-feira.</p>
  <p><b>Gancho exagero:</b> Próxima moda no carnaval.</p>
</div>
<div class='card'>
  <h3>Vizinho chama bombeiros para resgatar gato... de pelúcia</h3>
  <div class='meta'>Por que é pitoresco: Confusão que só tabloide rende.</div>
  <p><b>Gancho setup:</b> Até o Garfield ficou ofendido.</p>
  <p><b>Gancho exagero:</b> Ano que vem é licitação pública para resgatar Pikachu.</p>
</div>
<footer>Site gerado automaticamente. Atualizado diariamente.</footer>
</body></html>"""
    DOCS.mkdir(parents=True, exist_ok=True)
    (DOCS / f"{today}.html").write_text(html, encoding='utf-8')
    print("Página criada:", DOCS / f"{today}.html")

if __name__ == "__main__":
    main()
