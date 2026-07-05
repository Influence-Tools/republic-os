---
type: Jurisdiction
title: "Lucas County, OH"
classification: county
fips: "39095"
state: "OH"
demographics:
  population: 428018
  population_under_18: 97509
  population_18_64: 255300
  population_65_plus: 75209
  median_household_income: 62224
  poverty_rate: 17.72
  homeownership_rate: 61.97
  unemployment_rate: 6.3
  median_home_value: 163900
  gini_index: 0.4852
  vacancy_rate: 8.83
  race_white: 291946
  race_black: 82681
  race_asian: 7447
  race_native: 902
  hispanic: 33507
  bachelors_plus: 118867
districts:
  - to: "us/states/oh/districts/09"
    rel: in-district
    area_weight: 0.5828
  - to: "us/states/oh/districts/senate/11"
    rel: in-district
    area_weight: 0.3018
  - to: "us/states/oh/districts/senate/2"
    rel: in-district
    area_weight: 0.2798
  - to: "us/states/oh/districts/house/44"
    rel: in-district
    area_weight: 0.2797
  - to: "us/states/oh/districts/house/42"
    rel: in-district
    area_weight: 0.1494
  - to: "us/states/oh/districts/house/41"
    rel: in-district
    area_weight: 0.0942
  - to: "us/states/oh/districts/house/43"
    rel: in-district
    area_weight: 0.0583
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, oh]
timestamp: "2026-07-03"
---

# Lucas County, OH

County jurisdiction — 4 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 428018 |
| Under 18 | 97509 |
| 18–64 | 255300 |
| 65+ | 75209 |
| Median household income | 62224 |
| Poverty rate | 17.72 |
| Homeownership rate | 61.97 |
| Unemployment rate | 6.3 |
| Median home value | 163900 |
| Gini index | 0.4852 |
| Vacancy rate | 8.83 |
| White | 291946 |
| Black | 82681 |
| Asian | 7447 |
| Native | 902 |
| Hispanic/Latino | 33507 |
| Bachelor's or higher | 118867 |

## Districts

- [OH-09](/us/states/oh/districts/09.md) — 58% (congressional)
- [OH Senate District 11](/us/states/oh/districts/senate/11.md) — 30% (state senate)
- [OH Senate District 2](/us/states/oh/districts/senate/2.md) — 28% (state senate)
- [OH House District 44](/us/states/oh/districts/house/44.md) — 28% (state house)
- [OH House District 42](/us/states/oh/districts/house/42.md) — 15% (state house)
- [OH House District 41](/us/states/oh/districts/house/41.md) — 9% (state house)
- [OH House District 43](/us/states/oh/districts/house/43.md) — 6% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
