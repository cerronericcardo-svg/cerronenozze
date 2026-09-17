# Cerrone Nozze

Sito dello studio di organizzazione matrimoni ed eventi — cerronenozze.it

Sito statico: nessuna build, nessuna dipendenza, un solo file.

## File

| File | A cosa serve |
| --- | --- |
| `index.html` | Il sito. Markup, CSS e JS in un unico file: aprilo nel browser e lo vedi. |
| `tools/build-artifact.py` | Genera `build/artifact.html`, la copia pubblicata come anteprima su claude.ai. |

## Struttura della pagina

Pagina singola con ancore: servizi, metodo di lavoro, realizzazioni, chi siamo,
testimonianze, richiesta preventivo.

Il modulo preventivo non ha backend: compone un messaggio WhatsApp o una email
precompilata con i dati inseriti. Non invia e non salva nulla, quindi non serve
un server ne' un'informativa sul trattamento dei dati raccolti dal sito.

## Personalizzare

I contenuti provvisori sono marcati `class="ph"` e appaiono evidenziati in giallo,
insieme alla barra "Bozza" in cima. Per elencarli tutti:

```
grep -n 'class="ph"' index.html
```

Le due costanti in fondo a `index.html`:

- `TELEFONO_WA` — numero WhatsApp che riceve le richieste (solo cifre, con prefisso)
- `EMAIL_INFO` — indirizzo email per le richieste

Le foto sono riquadri segnaposto (`<div class="photo">`): vanno sostituiti con
`<img src="..." alt="...">`, mettendo i file in una cartella `img/`.

Quando i contenuti sono definitivi si tolgono la barra `<div class="draft">`,
la classe `ph` e le due regole `.ph` nel CSS.

## Pubblicare

Il sito e' un file statico: va su qualsiasi hosting copiando `index.html`
(piu' la cartella `img/` quando ci sara'). Per GitHub Pages:
Settings > Pages > Deploy from a branch.
