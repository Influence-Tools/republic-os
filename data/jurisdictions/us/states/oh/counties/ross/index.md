---
type: Jurisdiction
title: "Ross County, OH"
classification: county
fips: "39141"
state: "OH"
demographics:
  population: 76492
  population_under_18: 16098
  population_18_64: 46697
  population_65_plus: 13697
  median_household_income: 61303
  poverty_rate: 15.69
  homeownership_rate: 69.61
  unemployment_rate: 3.82
  median_home_value: 171500
  gini_index: 0.4514
  vacancy_rate: 7.12
  race_white: 67825
  race_black: 4202
  race_asian: 417
  race_native: 167
  hispanic: 1092
  bachelors_plus: 13122
districts:
  - to: "us/states/oh/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/oh/districts/senate/17"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/oh/districts/house/92"
    rel: in-district
    area_weight: 0.5887
  - to: "us/states/oh/districts/house/91"
    rel: in-district
    area_weight: 0.4112
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, oh]
timestamp: "2026-07-03"
---

# Ross County, OH

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 76492 |
| Under 18 | 16098 |
| 18–64 | 46697 |
| 65+ | 13697 |
| Median household income | 61303 |
| Poverty rate | 15.69 |
| Homeownership rate | 69.61 |
| Unemployment rate | 3.82 |
| Median home value | 171500 |
| Gini index | 0.4514 |
| Vacancy rate | 7.12 |
| White | 67825 |
| Black | 4202 |
| Asian | 417 |
| Native | 167 |
| Hispanic/Latino | 1092 |
| Bachelor's or higher | 13122 |

## Districts

- [OH-02](/us/states/oh/districts/02.md) — 100% (congressional)
- [OH Senate District 17](/us/states/oh/districts/senate/17.md) — 100% (state senate)
- [OH House District 92](/us/states/oh/districts/house/92.md) — 59% (state house)
- [OH House District 91](/us/states/oh/districts/house/91.md) — 41% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
