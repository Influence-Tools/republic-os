---
type: Jurisdiction
title: "Mariposa County, CA"
classification: county
fips: "06043"
state: "CA"
demographics:
  population: 17082
  population_under_18: 2941
  population_18_64: 9068
  population_65_plus: 5073
  median_household_income: 68412
  poverty_rate: 14.04
  homeownership_rate: 74.73
  unemployment_rate: 5.96
  median_home_value: 387900
  gini_index: 0.4342
  vacancy_rate: 23.67
  race_white: 13189
  race_black: 182
  race_asian: 326
  race_native: 285
  hispanic: 2508
  bachelors_plus: 6005
districts:
  - to: "us/states/ca/districts/05"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/ca/districts/senate/4"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ca/districts/house/8"
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

# Mariposa County, CA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 17082 |
| Under 18 | 2941 |
| 18–64 | 9068 |
| 65+ | 5073 |
| Median household income | 68412 |
| Poverty rate | 14.04 |
| Homeownership rate | 74.73 |
| Unemployment rate | 5.96 |
| Median home value | 387900 |
| Gini index | 0.4342 |
| Vacancy rate | 23.67 |
| White | 13189 |
| Black | 182 |
| Asian | 326 |
| Native | 285 |
| Hispanic/Latino | 2508 |
| Bachelor's or higher | 6005 |

## Districts

- [CA-05](/us/states/ca/districts/05.md) — 100% (congressional)
- [CA Senate District 4](/us/states/ca/districts/senate/4.md) — 100% (state senate)
- [CA House District 8](/us/states/ca/districts/house/8.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
