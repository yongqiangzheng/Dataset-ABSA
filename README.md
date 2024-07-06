# Dataset-ABSA

## Task Definition

- ATSA: sentence+aspect term->sentiment
    - Pipeline: prediction
    - End-to-End: extraction + prediction
- ACSA: sentence+aspect category->sentiment
    - Pipeline: prediction
    - End-to-End: extraction + prediction

ATSA: Twitter, Lap14, Rest14 Rest15_v2, Rest16_v2, MAMS

- Rest16: English, Dutch, French, Russian, Spanish, Turkish
- Hotel16: Arabic
  ACSA: Lap14, Rest14, Rest15, Rest16, MAMS
- Hotel15 (out-of-domain)
- Rest16: English, Dutch, Russian, Spanish, Turkish
- Hotel16: Arabic
- Elec16: English (Laptops) , Chinese (Mobile Phones), Chinese (Digital Cameras), Dutch (Mobile Phones)
- Tele16: Turkish

Lap14 and Rest14 has v1 and v2 version
previous work use v1, we use v2 to correct the annotation of v1 and manually correct additional errors.

SemEval15

Entity types: RESTAURANT, FOOD, DRINKS, SERVICE, AMBIENCE, LOCATION

Attribute labels: GENERAL, PRICES, QUALITY, STYLE_OPTIONS, MISCELLANEOUS

SemEval16

...

The Aspect is positive/neutral/negative

The Attr1 of Ent1 is positive/neutral/negative
The Attr2 of Ent2 is positive/neutral/negative
The Attr3 of Ent3 is positive/neutral/negative

## Dataset

## ABSA

1. Twitter
2. Lap14
3. Rest14
4. Rest15
5. Rest16
6. MAMS

| Dataset | Train | Val | Test | Pos:Neu:Neg |
|:-------:|:-----:|:---:|:----:|:-----------:|
| Twitter | 6248  |     | 692  |    1:2:1    |

## Others

mixed language sentimnet analysis [SemEval-2020 Task9](https://zenodo.org/records/3974927#.XyxAZCgzZPZ)
structure sentiment analysis [SemEval-2022 Task10](https://github.com/jerbarnes/semeval22_structured_sentiment)

| Dataset | Aspect | Category | (A,C) | Opinion | ATSA | ACSA | TASD |
|:--------|:------:|:--------:|:-----:|:-------:|:----:|:----:|:----:|
| Twitter |   ✅    |    ❌     |   ❌   |    ❌    |  ✅   |  ❌   |  ❌   |
| Lap14_en   |   ✅    |    ❌     |   ❌   |    ❌    |  ✅   |  ❌   |  ❌   |
| Rest14_en  |   ✅    |    ✅     |   ❌   |    ❌    |  ✅   |  ✅   |  ❌   |
| Lap15_en   |   ❌    |    ✅     |   ❌   |    ❌    |  ❌   |  ✅   |  ❌   |
| Rest15_en  |   ✅    |    ✅     |   ✅   |    ❌    |  ✅   |  ✅   |  ✅   |
| Lap16_en   |   ❌    |    ✅     |   ❌   |    ❌    |  ❌   |  ✅   |  ❌   |
| Rest16_en  |   ✅    |    ✅     |   ✅   |    ❌    |  ✅   |  ✅   |  ✅   |
| Rest16_nl  |   ✅    |    ✅     |   ✅   |    ❌    |  ✅   |  ✅   |  ✅   |
| Rest16_ru  |   ✅    |    ✅     |   ✅   |    ❌    |  ✅   |  ✅   |  ✅   |
| Rest16_es  |   ✅    |    ✅     |   ✅   |    ❌    |  ✅   |  ✅   |  ✅   |
| Rest16_tr  |   ✅    |    ✅     |   ✅   |    ❌    |  ✅   |  ✅   |  ✅   |
| Hotel16_ar |   ✅    |    ✅     |   ✅   |    ❌    |  ✅   |  ✅   |  ✅   |
| Came16_zh  |   ❌    |    ✅     |   ❌   |    ❌    |  ❌   |  ✅   |  ❌   |
| Phone16_zh |   ❌    |    ✅     |   ❌   |    ❌    |  ❌   |  ✅   |  ❌   |
| Phone16_nl |   ❌    |    ✅     |   ❌   |    ❌    |  ❌   |  ✅   |  ❌   |
| MAMS    |   ✅    |    ✅     |   ❌   |    ❌    |  ✅   |  ✅   |  ❌   |
| Hotel15_en |   ✅    |    ✅     |   ✅   |    ❌    |  ✅   |  ✅   |  ✅   |

| Task     | Input | Output |
|----------|-------|--------|
| ATSA     | S,a   | s      |
| E2E-ABSA | S     | a,s    |
| ACSA     | S     | c,s    |
| TASD     | S     | a,c,s  |
