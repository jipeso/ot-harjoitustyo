# Physics simulations

Sovelluksen avulla käyttäjän on mahdollista asettaa systeemille haluamansa parametrit ja simuloida sen toimintaa ajan kuluessa.

## Dokumentaatio

[gitlog.txt](https://github.com/jipeso/ot-harjoitustyo/blob/main/laskarit/viikko1/gitlog.txt)

[komentorivi.txt](https://github.com/jipeso/ot-harjoitustyo/blob/main/laskarit/viikko1/komentorivi.txt)

[vaatimusmaarittely.md](https://github.com/jipeso/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)

[tuntikirjanpito.md](https://github.com/jipeso/ot-harjoitustyo/blob/main/dokumentaatio/tuntikirjanpito.md)

[changelog.md](https://github.com/jipeso/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)


## Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi luoda komennolla:

```bash
poetry run invoke coverage-report
```