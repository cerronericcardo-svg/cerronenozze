# Cerrone Nozze

Sito statico per il matrimonio. Nessuna build, nessuna dipendenza: un solo file.

## File

| File | A cosa serve |
| --- | --- |
| `index.html` | Il sito. Markup, CSS e JS in un unico file: aprilo nel browser e lo vedi. |
| `tools/build-artifact.py` | Genera `build/artifact.html`, la copia da pubblicare come anteprima su claude.ai. |

## Personalizzare

I testi provvisori sono marcati con `class="ph"` e appaiono evidenziati in giallo
nella pagina, insieme a una barra "Bozza" in cima. Per trovarli tutti:

```
grep -n 'class="ph"' index.html
```

I tre valori che stanno nel JavaScript, in fondo a `index.html`:

- `DATA_NOZZE` — data e ora della cerimonia, usata dal countdown
- `TELEFONO_WA` — numero WhatsApp che riceve le conferme (solo cifre, con prefisso)
- `EMAIL_RSVP` — indirizzo email alternativo per le conferme

Quando i contenuti sono definitivi si tolgono la barra `<div class="draft">`,
la classe `ph` e la regola `.ph` nel CSS.

## Pubblicare

Il sito e' un file statico: va su GitHub Pages, Netlify o qualsiasi hosting
copiando `index.html`. Per GitHub Pages: Settings > Pages > Deploy from a branch.
