---
type: Jurisdiction
title: "Lafayette County, AR"
classification: county
fips: "05073"
state: "AR"
demographics:
  population: 6136
  population_under_18: 1120
  population_18_64: 3432
  population_65_plus: 1584
  median_household_income: 41278
  poverty_rate: 22.26
  homeownership_rate: 79.25
  unemployment_rate: 5.3
  median_home_value: 81000
  gini_index: 0.4763
  vacancy_rate: 33.45
  race_white: 3543
  race_black: 2262
  race_asian: 62
  race_native: 14
  hispanic: 36
  bachelors_plus: 508
districts:
  - to: "us/states/ar/districts/04"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ar/districts/senate/3"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ar/districts/house/99"
    rel: in-district
    area_weight: 0.8259
  - to: "us/states/ar/districts/house/98"
    rel: in-district
    area_weight: 0.174
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Lafayette County, AR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 6136 |
| Under 18 | 1120 |
| 18–64 | 3432 |
| 65+ | 1584 |
| Median household income | 41278 |
| Poverty rate | 22.26 |
| Homeownership rate | 79.25 |
| Unemployment rate | 5.3 |
| Median home value | 81000 |
| Gini index | 0.4763 |
| Vacancy rate | 33.45 |
| White | 3543 |
| Black | 2262 |
| Asian | 62 |
| Native | 14 |
| Hispanic/Latino | 36 |
| Bachelor's or higher | 508 |

## Districts

- [AR-04](/us/states/ar/districts/04.md) — 100% (congressional)
- [AR Senate District 3](/us/states/ar/districts/senate/3.md) — 100% (state senate)
- [AR House District 99](/us/states/ar/districts/house/99.md) — 83% (state house)
- [AR House District 98](/us/states/ar/districts/house/98.md) — 17% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
