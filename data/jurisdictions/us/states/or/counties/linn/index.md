---
type: Jurisdiction
title: "Linn County, OR"
classification: county
fips: "41043"
state: "OR"
demographics:
  population: 130706
  population_under_18: 28724
  population_18_64: 76487
  population_65_plus: 25495
  median_household_income: 76329
  poverty_rate: 12.98
  homeownership_rate: 66.86
  unemployment_rate: 6.0
  median_home_value: 376400
  gini_index: 0.4048
  vacancy_rate: 4.85
  race_white: 109727
  race_black: 664
  race_asian: 1372
  race_native: 887
  hispanic: 13937
  bachelors_plus: 26090
districts:
  - to: "us/states/or/districts/05"
    rel: in-district
    area_weight: 0.9932
  - to: "us/states/or/districts/04"
    rel: in-district
    area_weight: 0.0061
  - to: "us/states/or/districts/senate/6"
    rel: in-district
    area_weight: 0.752
  - to: "us/states/or/districts/senate/9"
    rel: in-district
    area_weight: 0.1991
  - to: "us/states/or/districts/senate/8"
    rel: in-district
    area_weight: 0.0489
  - to: "us/states/or/districts/house/11"
    rel: in-district
    area_weight: 0.7496
  - to: "us/states/or/districts/house/17"
    rel: in-district
    area_weight: 0.1991
  - to: "us/states/or/districts/house/15"
    rel: in-district
    area_weight: 0.0488
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, or]
timestamp: "2026-07-03"
---

# Linn County, OR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 130706 |
| Under 18 | 28724 |
| 18–64 | 76487 |
| 65+ | 25495 |
| Median household income | 76329 |
| Poverty rate | 12.98 |
| Homeownership rate | 66.86 |
| Unemployment rate | 6.0 |
| Median home value | 376400 |
| Gini index | 0.4048 |
| Vacancy rate | 4.85 |
| White | 109727 |
| Black | 664 |
| Asian | 1372 |
| Native | 887 |
| Hispanic/Latino | 13937 |
| Bachelor's or higher | 26090 |

## Districts

- [OR-05](/us/states/or/districts/05.md) — 99% (congressional)
- [OR-04](/us/states/or/districts/04.md) — 1% (congressional)
- [OR Senate District 6](/us/states/or/districts/senate/6.md) — 75% (state senate)
- [OR Senate District 9](/us/states/or/districts/senate/9.md) — 20% (state senate)
- [OR Senate District 8](/us/states/or/districts/senate/8.md) — 5% (state senate)
- [OR House District 11](/us/states/or/districts/house/11.md) — 75% (state house)
- [OR House District 17](/us/states/or/districts/house/17.md) — 20% (state house)
- [OR House District 15](/us/states/or/districts/house/15.md) — 5% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
