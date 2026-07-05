---
type: Jurisdiction
title: "Logan County, OH"
classification: county
fips: "39091"
state: "OH"
demographics:
  population: 46089
  population_under_18: 10476
  population_18_64: 26681
  population_65_plus: 8932
  median_household_income: 71551
  poverty_rate: 11.08
  homeownership_rate: 77.59
  unemployment_rate: 4.07
  median_home_value: 203200
  gini_index: 0.4449
  vacancy_rate: 18.04
  race_white: 42343
  race_black: 789
  race_asian: 267
  race_native: 42
  hispanic: 1084
  bachelors_plus: 7963
districts:
  - to: "us/states/oh/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/oh/districts/senate/12"
    rel: in-district
    area_weight: 0.5166
  - to: "us/states/oh/districts/senate/1"
    rel: in-district
    area_weight: 0.4834
  - to: "us/states/oh/districts/house/85"
    rel: in-district
    area_weight: 0.5165
  - to: "us/states/oh/districts/house/83"
    rel: in-district
    area_weight: 0.4834
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, oh]
timestamp: "2026-07-03"
---

# Logan County, OH

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 46089 |
| Under 18 | 10476 |
| 18–64 | 26681 |
| 65+ | 8932 |
| Median household income | 71551 |
| Poverty rate | 11.08 |
| Homeownership rate | 77.59 |
| Unemployment rate | 4.07 |
| Median home value | 203200 |
| Gini index | 0.4449 |
| Vacancy rate | 18.04 |
| White | 42343 |
| Black | 789 |
| Asian | 267 |
| Native | 42 |
| Hispanic/Latino | 1084 |
| Bachelor's or higher | 7963 |

## Districts

- [OH-04](/us/states/oh/districts/04.md) — 100% (congressional)
- [OH Senate District 12](/us/states/oh/districts/senate/12.md) — 52% (state senate)
- [OH Senate District 1](/us/states/oh/districts/senate/1.md) — 48% (state senate)
- [OH House District 85](/us/states/oh/districts/house/85.md) — 52% (state house)
- [OH House District 83](/us/states/oh/districts/house/83.md) — 48% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
