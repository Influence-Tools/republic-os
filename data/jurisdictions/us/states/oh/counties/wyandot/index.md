---
type: Jurisdiction
title: "Wyandot County, OH"
classification: county
fips: "39175"
state: "OH"
demographics:
  population: 21598
  population_under_18: 4844
  population_18_64: 12261
  population_65_plus: 4493
  median_household_income: 69768
  poverty_rate: 8.77
  homeownership_rate: 74.14
  unemployment_rate: 1.92
  median_home_value: 163400
  gini_index: 0.4046
  vacancy_rate: 9.03
  race_white: 20440
  race_black: 52
  race_asian: 25
  race_native: 2
  hispanic: 674
  bachelors_plus: 4181
districts:
  - to: "us/states/oh/districts/05"
    rel: in-district
    area_weight: 0.8713
  - to: "us/states/oh/districts/04"
    rel: in-district
    area_weight: 0.1287
  - to: "us/states/oh/districts/senate/26"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/oh/districts/house/87"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, oh]
timestamp: "2026-07-03"
---

# Wyandot County, OH

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 21598 |
| Under 18 | 4844 |
| 18–64 | 12261 |
| 65+ | 4493 |
| Median household income | 69768 |
| Poverty rate | 8.77 |
| Homeownership rate | 74.14 |
| Unemployment rate | 1.92 |
| Median home value | 163400 |
| Gini index | 0.4046 |
| Vacancy rate | 9.03 |
| White | 20440 |
| Black | 52 |
| Asian | 25 |
| Native | 2 |
| Hispanic/Latino | 674 |
| Bachelor's or higher | 4181 |

## Districts

- [OH-05](/us/states/oh/districts/05.md) — 87% (congressional)
- [OH-04](/us/states/oh/districts/04.md) — 13% (congressional)
- [OH Senate District 26](/us/states/oh/districts/senate/26.md) — 100% (state senate)
- [OH House District 87](/us/states/oh/districts/house/87.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
