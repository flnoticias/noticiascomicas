import os, datetime, pathlib
ROOT = pathlib.Path(__file__).resolve().parent
DOCS = ROOT / "docs" / "colunas"

def main():
    today = datetime.date.today()
    year, week, _ = today.isocalendar()
    fname = f"{year}-W{week:02d}.html"
    html = f"""<!doctype html>
<html><head><meta charset='utf-8'><title>Coluna {year}-W{week:02d}</title>
<link rel="stylesheet" href="../style.css"></head>
<body>
<h1>Coluna Autoral</h1>
<h2>Semana {week} – {today}</h2>
<div class='card'>
  <p><strong>Por @otaldefelipeloureiro</strong></p>
  <p><em>Rascunho automático criado em {today}. Substitua este texto pelo seu artigo de opinião sobre a notícia mais curiosa da semana.</em></p>
</div>
<footer>Seção de Opinião – Pautas Pitorescas</footer>
</body></html>"""
    DOCS.mkdir(parents=True, exist_ok=True)
    (DOCS / fname).write_text(html, encoding='utf-8')
    print("Coluna criada:", DOCS / fname)

if __name__ == "__main__":
    main()
