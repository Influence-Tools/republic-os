---
type: Jurisdiction
title: "Warren County, NJ"
classification: county
fips: "34041"
state: "NJ"
demographics:
  population: 110849
  population_under_18: 21393
  population_18_64: 67784
  population_65_plus: 21672
  median_household_income: 100869
  poverty_rate: 8.34
  homeownership_rate: 75.06
  unemployment_rate: 5.1
  median_home_value: 346500
  gini_index: 0.4146
  vacancy_rate: 2.99
  race_white: 85215
  race_black: 6677
  race_asian: 3381
  race_native: 299
  hispanic: 14378
  bachelors_plus: 39235
districts:
  - to: "us/states/nj/districts/07"
    rel: in-district
    area_weight: 0.999
  - to: "us/states/nj/districts/senate/23"
    rel: in-district
    area_weight: 0.8884
  - to: "us/states/nj/districts/senate/24"
    rel: in-district
    area_weight: 0.1112
  - to: "us/states/nj/districts/house/23"
    rel: in-district
    area_weight: 0.8884
  - to: "us/states/nj/districts/house/24"
    rel: in-district
    area_weight: 0.1112
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nj]
timestamp: "2026-07-03"
---

# Warren County, NJ

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 110849 |
| Under 18 | 21393 |
| 18–64 | 67784 |
| 65+ | 21672 |
| Median household income | 100869 |
| Poverty rate | 8.34 |
| Homeownership rate | 75.06 |
| Unemployment rate | 5.1 |
| Median home value | 346500 |
| Gini index | 0.4146 |
| Vacancy rate | 2.99 |
| White | 85215 |
| Black | 6677 |
| Asian | 3381 |
| Native | 299 |
| Hispanic/Latino | 14378 |
| Bachelor's or higher | 39235 |

## Districts

- [NJ-07](/us/states/nj/districts/07.md) — 100% (congressional)
- [NJ Senate District 23](/us/states/nj/districts/senate/23.md) — 89% (state senate)
- [NJ Senate District 24](/us/states/nj/districts/senate/24.md) — 11% (state senate)
- [NJ House District 23](/us/states/nj/districts/house/23.md) — 89% (state house)
- [NJ House District 24](/us/states/nj/districts/house/24.md) — 11% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
