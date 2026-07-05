---
type: Jurisdiction
title: "Columbiana County, OH"
classification: county
fips: "39029"
state: "OH"
demographics:
  population: 100704
  population_under_18: 20329
  population_18_64: 58268
  population_65_plus: 22107
  median_household_income: 58180
  poverty_rate: 15.15
  homeownership_rate: 72.74
  unemployment_rate: 4.46
  median_home_value: 151600
  gini_index: 0.4625
  vacancy_rate: 10.11
  race_white: 93207
  race_black: 1978
  race_asian: 264
  race_native: 242
  hispanic: 1923
  bachelors_plus: 16739
districts:
  - to: "us/states/oh/districts/06"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/oh/districts/senate/33"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/oh/districts/house/79"
    rel: in-district
    area_weight: 0.8716
  - to: "us/states/oh/districts/house/59"
    rel: in-district
    area_weight: 0.1282
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, oh]
timestamp: "2026-07-03"
---

# Columbiana County, OH

County jurisdiction — 3 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 100704 |
| Under 18 | 20329 |
| 18–64 | 58268 |
| 65+ | 22107 |
| Median household income | 58180 |
| Poverty rate | 15.15 |
| Homeownership rate | 72.74 |
| Unemployment rate | 4.46 |
| Median home value | 151600 |
| Gini index | 0.4625 |
| Vacancy rate | 10.11 |
| White | 93207 |
| Black | 1978 |
| Asian | 264 |
| Native | 242 |
| Hispanic/Latino | 1923 |
| Bachelor's or higher | 16739 |

## Districts

- [OH-06](/us/states/oh/districts/06.md) — 100% (congressional)
- [OH Senate District 33](/us/states/oh/districts/senate/33.md) — 100% (state senate)
- [OH House District 79](/us/states/oh/districts/house/79.md) — 87% (state house)
- [OH House District 59](/us/states/oh/districts/house/59.md) — 13% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
