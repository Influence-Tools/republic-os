---
type: Jurisdiction
title: "Hood River County, OR"
classification: county
fips: "41027"
state: "OR"
demographics:
  population: 23905
  population_under_18: 5212
  population_18_64: 14371
  population_65_plus: 4322
  median_household_income: 88947
  poverty_rate: 8.01
  homeownership_rate: 69.39
  unemployment_rate: 3.84
  median_home_value: 660000
  gini_index: 0.4615
  vacancy_rate: 13.13
  race_white: 16162
  race_black: 236
  race_asian: 190
  race_native: 115
  hispanic: 7325
  bachelors_plus: 9746
districts:
  - to: "us/states/or/districts/03"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/or/districts/senate/26"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/or/districts/house/52"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, or]
timestamp: "2026-07-03"
---

# Hood River County, OR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 23905 |
| Under 18 | 5212 |
| 18–64 | 14371 |
| 65+ | 4322 |
| Median household income | 88947 |
| Poverty rate | 8.01 |
| Homeownership rate | 69.39 |
| Unemployment rate | 3.84 |
| Median home value | 660000 |
| Gini index | 0.4615 |
| Vacancy rate | 13.13 |
| White | 16162 |
| Black | 236 |
| Asian | 190 |
| Native | 115 |
| Hispanic/Latino | 7325 |
| Bachelor's or higher | 9746 |

## Districts

- [OR-03](/us/states/or/districts/03.md) — 100% (congressional)
- [OR Senate District 26](/us/states/or/districts/senate/26.md) — 100% (state senate)
- [OR House District 52](/us/states/or/districts/house/52.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
