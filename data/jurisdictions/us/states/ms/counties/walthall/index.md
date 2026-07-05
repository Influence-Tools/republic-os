---
type: Jurisdiction
title: "Walthall County, MS"
classification: county
fips: "28147"
state: "MS"
demographics:
  population: 13839
  population_under_18: 3122
  population_18_64: 7678
  population_65_plus: 3039
  median_household_income: 48905
  poverty_rate: 18.77
  homeownership_rate: 80.28
  unemployment_rate: 6.63
  median_home_value: 126600
  gini_index: 0.5013
  vacancy_rate: 23.52
  race_white: 7324
  race_black: 5792
  race_asian: 26
  race_native: 51
  hispanic: 274
  bachelors_plus: 1744
districts:
  - to: "us/states/ms/districts/03"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ms/districts/senate/41"
    rel: in-district
    area_weight: 0.6027
  - to: "us/states/ms/districts/senate/38"
    rel: in-district
    area_weight: 0.3971
  - to: "us/states/ms/districts/house/99"
    rel: in-district
    area_weight: 0.7881
  - to: "us/states/ms/districts/house/98"
    rel: in-district
    area_weight: 0.2118
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Walthall County, MS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 13839 |
| Under 18 | 3122 |
| 18–64 | 7678 |
| 65+ | 3039 |
| Median household income | 48905 |
| Poverty rate | 18.77 |
| Homeownership rate | 80.28 |
| Unemployment rate | 6.63 |
| Median home value | 126600 |
| Gini index | 0.5013 |
| Vacancy rate | 23.52 |
| White | 7324 |
| Black | 5792 |
| Asian | 26 |
| Native | 51 |
| Hispanic/Latino | 274 |
| Bachelor's or higher | 1744 |

## Districts

- [MS-03](/us/states/ms/districts/03.md) — 100% (congressional)
- [MS Senate District 41](/us/states/ms/districts/senate/41.md) — 60% (state senate)
- [MS Senate District 38](/us/states/ms/districts/senate/38.md) — 40% (state senate)
- [MS House District 99](/us/states/ms/districts/house/99.md) — 79% (state house)
- [MS House District 98](/us/states/ms/districts/house/98.md) — 21% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
