---
type: Jurisdiction
title: "Clare County, MI"
classification: county
fips: "26035"
state: "MI"
demographics:
  population: 31218
  population_under_18: 6014
  population_18_64: 17216
  population_65_plus: 7988
  median_household_income: 49384
  poverty_rate: 21.64
  homeownership_rate: 86.88
  unemployment_rate: 9.47
  median_home_value: 133800
  gini_index: 0.4614
  vacancy_rate: 43.11
  race_white: 29185
  race_black: 356
  race_asian: 102
  race_native: 119
  hispanic: 715
  bachelors_plus: 4226
districts:
  - to: "us/states/mi/districts/02"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mi/districts/senate/34"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mi/districts/house/100"
    rel: in-district
    area_weight: 0.7488
  - to: "us/states/mi/districts/house/99"
    rel: in-district
    area_weight: 0.251
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Clare County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 31218 |
| Under 18 | 6014 |
| 18–64 | 17216 |
| 65+ | 7988 |
| Median household income | 49384 |
| Poverty rate | 21.64 |
| Homeownership rate | 86.88 |
| Unemployment rate | 9.47 |
| Median home value | 133800 |
| Gini index | 0.4614 |
| Vacancy rate | 43.11 |
| White | 29185 |
| Black | 356 |
| Asian | 102 |
| Native | 119 |
| Hispanic/Latino | 715 |
| Bachelor's or higher | 4226 |

## Districts

- [MI-02](/us/states/mi/districts/02.md) — 100% (congressional)
- [MI Senate District 34](/us/states/mi/districts/senate/34.md) — 100% (state senate)
- [MI House District 100](/us/states/mi/districts/house/100.md) — 75% (state house)
- [MI House District 99](/us/states/mi/districts/house/99.md) — 25% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
