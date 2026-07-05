---
type: Jurisdiction
title: "Lane County, OR"
classification: county
fips: "41039"
state: "OR"
demographics:
  population: 384207
  population_under_18: 67084
  population_18_64: 237030
  population_65_plus: 80093
  median_household_income: 71544
  poverty_rate: 15.34
  homeownership_rate: 59.69
  unemployment_rate: 6.43
  median_home_value: 430600
  gini_index: 0.4561
  vacancy_rate: 5.5
  race_white: 310002
  race_black: 4587
  race_asian: 10121
  race_native: 4718
  hispanic: 40225
  bachelors_plus: 128549
districts:
  - to: "us/states/or/districts/04"
    rel: in-district
    area_weight: 0.9767
  - to: "us/states/or/districts/senate/6"
    rel: in-district
    area_weight: 0.6555
  - to: "us/states/or/districts/senate/5"
    rel: in-district
    area_weight: 0.2631
  - to: "us/states/or/districts/senate/4"
    rel: in-district
    area_weight: 0.0312
  - to: "us/states/or/districts/senate/7"
    rel: in-district
    area_weight: 0.0284
  - to: "us/states/or/districts/house/12"
    rel: in-district
    area_weight: 0.6554
  - to: "us/states/or/districts/house/9"
    rel: in-district
    area_weight: 0.1683
  - to: "us/states/or/districts/house/10"
    rel: in-district
    area_weight: 0.0948
  - to: "us/states/or/districts/house/8"
    rel: in-district
    area_weight: 0.0246
  - to: "us/states/or/districts/house/14"
    rel: in-district
    area_weight: 0.0237
  - to: "us/states/or/districts/house/7"
    rel: in-district
    area_weight: 0.0066
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, or]
timestamp: "2026-07-03"
---

# Lane County, OR

County jurisdiction — 3 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 384207 |
| Under 18 | 67084 |
| 18–64 | 237030 |
| 65+ | 80093 |
| Median household income | 71544 |
| Poverty rate | 15.34 |
| Homeownership rate | 59.69 |
| Unemployment rate | 6.43 |
| Median home value | 430600 |
| Gini index | 0.4561 |
| Vacancy rate | 5.5 |
| White | 310002 |
| Black | 4587 |
| Asian | 10121 |
| Native | 4718 |
| Hispanic/Latino | 40225 |
| Bachelor's or higher | 128549 |

## Districts

- [OR-04](/us/states/or/districts/04.md) — 98% (congressional)
- [OR Senate District 6](/us/states/or/districts/senate/6.md) — 66% (state senate)
- [OR Senate District 5](/us/states/or/districts/senate/5.md) — 26% (state senate)
- [OR Senate District 4](/us/states/or/districts/senate/4.md) — 3% (state senate)
- [OR Senate District 7](/us/states/or/districts/senate/7.md) — 3% (state senate)
- [OR House District 12](/us/states/or/districts/house/12.md) — 66% (state house)
- [OR House District 9](/us/states/or/districts/house/9.md) — 17% (state house)
- [OR House District 10](/us/states/or/districts/house/10.md) — 9% (state house)
- [OR House District 8](/us/states/or/districts/house/8.md) — 2% (state house)
- [OR House District 14](/us/states/or/districts/house/14.md) — 2% (state house)
- [OR House District 7](/us/states/or/districts/house/7.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
