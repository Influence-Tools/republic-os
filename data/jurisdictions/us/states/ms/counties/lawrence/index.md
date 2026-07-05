---
type: Jurisdiction
title: "Lawrence County, MS"
classification: county
fips: "28077"
state: "MS"
demographics:
  population: 11786
  population_under_18: 2874
  population_18_64: 6607
  population_65_plus: 2305
  median_household_income: 43531
  poverty_rate: 23.65
  homeownership_rate: 83.5
  unemployment_rate: 9.17
  median_home_value: 100000
  gini_index: 0.5141
  vacancy_rate: 23.79
  race_white: 7519
  race_black: 3737
  race_asian: 37
  race_native: 45
  hispanic: 251
  bachelors_plus: 1345
districts:
  - to: "us/states/ms/districts/03"
    rel: in-district
    area_weight: 0.999
  - to: "us/states/ms/districts/senate/35"
    rel: in-district
    area_weight: 0.5989
  - to: "us/states/ms/districts/senate/39"
    rel: in-district
    area_weight: 0.401
  - to: "us/states/ms/districts/house/91"
    rel: in-district
    area_weight: 0.5602
  - to: "us/states/ms/districts/house/53"
    rel: in-district
    area_weight: 0.2623
  - to: "us/states/ms/districts/house/92"
    rel: in-district
    area_weight: 0.0962
  - to: "us/states/ms/districts/house/99"
    rel: in-district
    area_weight: 0.0812
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Lawrence County, MS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 11786 |
| Under 18 | 2874 |
| 18–64 | 6607 |
| 65+ | 2305 |
| Median household income | 43531 |
| Poverty rate | 23.65 |
| Homeownership rate | 83.5 |
| Unemployment rate | 9.17 |
| Median home value | 100000 |
| Gini index | 0.5141 |
| Vacancy rate | 23.79 |
| White | 7519 |
| Black | 3737 |
| Asian | 37 |
| Native | 45 |
| Hispanic/Latino | 251 |
| Bachelor's or higher | 1345 |

## Districts

- [MS-03](/us/states/ms/districts/03.md) — 100% (congressional)
- [MS Senate District 35](/us/states/ms/districts/senate/35.md) — 60% (state senate)
- [MS Senate District 39](/us/states/ms/districts/senate/39.md) — 40% (state senate)
- [MS House District 91](/us/states/ms/districts/house/91.md) — 56% (state house)
- [MS House District 53](/us/states/ms/districts/house/53.md) — 26% (state house)
- [MS House District 92](/us/states/ms/districts/house/92.md) — 10% (state house)
- [MS House District 99](/us/states/ms/districts/house/99.md) — 8% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
