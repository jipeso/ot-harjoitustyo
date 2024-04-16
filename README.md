# Physics simulations

Sovelluksen avulla käyttäjän on mahdollista asettaa systeemille haluamansa parametrit ja simuloida sen toimintaa ajan kuluessa.

## Dokumentaatio

[vaatimusmaarittely.md](https://github.com/jipeso/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)

[tuntikirjanpito.md](https://github.com/jipeso/ot-harjoitustyo/blob/main/dokumentaatio/tuntikirjanpito.md)

[changelog.md](https://github.com/jipeso/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)

[arkkitehtuuri.md](https://github.com/jipeso/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)

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
### Pylint

Tiedoston [.pylintrc](./.pylintrc) määrittelemät tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke lint
```