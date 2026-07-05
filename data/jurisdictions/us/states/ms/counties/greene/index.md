---
type: Jurisdiction
title: "Greene County, MS"
classification: county
fips: "28041"
state: "MS"
demographics:
  population: 13615
  population_under_18: 2572
  population_18_64: 8982
  population_65_plus: 2061
  median_household_income: 54276
  poverty_rate: 18.29
  homeownership_rate: 82.16
  unemployment_rate: 11.89
  median_home_value: 92700
  gini_index: 0.446
  vacancy_rate: 20.83
  race_white: 9673
  race_black: 3241
  race_asian: 4
  race_native: 164
  hispanic: 198
  bachelors_plus: 1530
districts:
  - to: "us/states/ms/districts/04"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ms/districts/senate/43"
    rel: in-district
    area_weight: 0.8541
  - to: "us/states/ms/districts/senate/42"
    rel: in-district
    area_weight: 0.1457
  - to: "us/states/ms/districts/house/105"
    rel: in-district
    area_weight: 0.8248
  - to: "us/states/ms/districts/house/86"
    rel: in-district
    area_weight: 0.175
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Greene County, MS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 13615 |
| Under 18 | 2572 |
| 18–64 | 8982 |
| 65+ | 2061 |
| Median household income | 54276 |
| Poverty rate | 18.29 |
| Homeownership rate | 82.16 |
| Unemployment rate | 11.89 |
| Median home value | 92700 |
| Gini index | 0.446 |
| Vacancy rate | 20.83 |
| White | 9673 |
| Black | 3241 |
| Asian | 4 |
| Native | 164 |
| Hispanic/Latino | 198 |
| Bachelor's or higher | 1530 |

## Districts

- [MS-04](/us/states/ms/districts/04.md) — 100% (congressional)
- [MS Senate District 43](/us/states/ms/districts/senate/43.md) — 85% (state senate)
- [MS Senate District 42](/us/states/ms/districts/senate/42.md) — 15% (state senate)
- [MS House District 105](/us/states/ms/districts/house/105.md) — 82% (state house)
- [MS House District 86](/us/states/ms/districts/house/86.md) — 18% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
