---
type: Jurisdiction
title: "Marion County, MS"
classification: county
fips: "28091"
state: "MS"
demographics:
  population: 24193
  population_under_18: 5666
  population_18_64: 13970
  population_65_plus: 4557
  median_household_income: 45110
  poverty_rate: 19.68
  homeownership_rate: 77.22
  unemployment_rate: 7.47
  median_home_value: 122800
  gini_index: 0.4562
  vacancy_rate: 18.28
  race_white: 15416
  race_black: 7625
  race_asian: 76
  race_native: 69
  hispanic: 449
  bachelors_plus: 3307
districts:
  - to: "us/states/ms/districts/03"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ms/districts/senate/41"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ms/districts/house/100"
    rel: in-district
    area_weight: 0.5669
  - to: "us/states/ms/districts/house/99"
    rel: in-district
    area_weight: 0.433
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Marion County, MS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 24193 |
| Under 18 | 5666 |
| 18–64 | 13970 |
| 65+ | 4557 |
| Median household income | 45110 |
| Poverty rate | 19.68 |
| Homeownership rate | 77.22 |
| Unemployment rate | 7.47 |
| Median home value | 122800 |
| Gini index | 0.4562 |
| Vacancy rate | 18.28 |
| White | 15416 |
| Black | 7625 |
| Asian | 76 |
| Native | 69 |
| Hispanic/Latino | 449 |
| Bachelor's or higher | 3307 |

## Districts

- [MS-03](/us/states/ms/districts/03.md) — 100% (congressional)
- [MS Senate District 41](/us/states/ms/districts/senate/41.md) — 100% (state senate)
- [MS House District 100](/us/states/ms/districts/house/100.md) — 57% (state house)
- [MS House District 99](/us/states/ms/districts/house/99.md) — 43% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
