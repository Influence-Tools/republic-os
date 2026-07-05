---
type: Jurisdiction
title: "Sussex County, NJ"
classification: county
fips: "34037"
state: "NJ"
demographics:
  population: 145807
  population_under_18: 28419
  population_18_64: 89732
  population_65_plus: 27656
  median_household_income: 116186
  poverty_rate: 5.54
  homeownership_rate: 83.73
  unemployment_rate: 5.12
  median_home_value: 369400
  gini_index: 0.4156
  vacancy_rate: 8.11
  race_white: 119960
  race_black: 2701
  race_asian: 2917
  race_native: 396
  hispanic: 17355
  bachelors_plus: 58169
districts:
  - to: "us/states/nj/districts/05"
    rel: in-district
    area_weight: 0.6882
  - to: "us/states/nj/districts/07"
    rel: in-district
    area_weight: 0.3108
  - to: "us/states/nj/districts/senate/24"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/nj/districts/house/24"
    rel: in-district
    area_weight: 0.9993
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nj]
timestamp: "2026-07-03"
---

# Sussex County, NJ

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 145807 |
| Under 18 | 28419 |
| 18–64 | 89732 |
| 65+ | 27656 |
| Median household income | 116186 |
| Poverty rate | 5.54 |
| Homeownership rate | 83.73 |
| Unemployment rate | 5.12 |
| Median home value | 369400 |
| Gini index | 0.4156 |
| Vacancy rate | 8.11 |
| White | 119960 |
| Black | 2701 |
| Asian | 2917 |
| Native | 396 |
| Hispanic/Latino | 17355 |
| Bachelor's or higher | 58169 |

## Districts

- [NJ-05](/us/states/nj/districts/05.md) — 69% (congressional)
- [NJ-07](/us/states/nj/districts/07.md) — 31% (congressional)
- [NJ Senate District 24](/us/states/nj/districts/senate/24.md) — 100% (state senate)
- [NJ House District 24](/us/states/nj/districts/house/24.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
