---
type: Jurisdiction
title: "Nevada County, CA"
classification: county
fips: "06057"
state: "CA"
demographics:
  population: 102481
  population_under_18: 17411
  population_18_64: 55037
  population_65_plus: 30033
  median_household_income: 89882
  poverty_rate: 11.01
  homeownership_rate: 75.45
  unemployment_rate: 5.44
  median_home_value: 621800
  gini_index: 0.4846
  vacancy_rate: 21.07
  race_white: 86049
  race_black: 387
  race_asian: 1827
  race_native: 449
  hispanic: 11001
  bachelors_plus: 44749
districts:
  - to: "us/states/ca/districts/03"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ca/districts/senate/1"
    rel: in-district
    area_weight: 0.929
  - to: "us/states/ca/districts/senate/4"
    rel: in-district
    area_weight: 0.0709
  - to: "us/states/ca/districts/house/1"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ca]
timestamp: "2026-07-03"
---

# Nevada County, CA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 102481 |
| Under 18 | 17411 |
| 18–64 | 55037 |
| 65+ | 30033 |
| Median household income | 89882 |
| Poverty rate | 11.01 |
| Homeownership rate | 75.45 |
| Unemployment rate | 5.44 |
| Median home value | 621800 |
| Gini index | 0.4846 |
| Vacancy rate | 21.07 |
| White | 86049 |
| Black | 387 |
| Asian | 1827 |
| Native | 449 |
| Hispanic/Latino | 11001 |
| Bachelor's or higher | 44749 |

## Districts

- [CA-03](/us/states/ca/districts/03.md) — 100% (congressional)
- [CA Senate District 1](/us/states/ca/districts/senate/1.md) — 93% (state senate)
- [CA Senate District 4](/us/states/ca/districts/senate/4.md) — 7% (state senate)
- [CA House District 1](/us/states/ca/districts/house/1.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
