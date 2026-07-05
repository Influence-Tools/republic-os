---
type: Jurisdiction
title: "Powell County, MT"
classification: county
fips: "30077"
state: "MT"
demographics:
  population: 7053
  population_under_18: 935
  population_18_64: 4646
  population_65_plus: 1472
  median_household_income: 66923
  poverty_rate: 5.56
  homeownership_rate: 72.53
  unemployment_rate: 2.35
  median_home_value: 306500
  gini_index: 0.4314
  vacancy_rate: 19.1
  race_white: 6148
  race_black: 28
  race_asian: 107
  race_native: 356
  hispanic: 190
  bachelors_plus: 1384
districts:
  - to: "us/states/mt/districts/01"
    rel: in-district
    area_weight: 0.9989
  - to: "us/states/mt/districts/senate/38"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mt/districts/house/76"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mt]
timestamp: "2026-07-03"
---

# Powell County, MT

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7053 |
| Under 18 | 935 |
| 18–64 | 4646 |
| 65+ | 1472 |
| Median household income | 66923 |
| Poverty rate | 5.56 |
| Homeownership rate | 72.53 |
| Unemployment rate | 2.35 |
| Median home value | 306500 |
| Gini index | 0.4314 |
| Vacancy rate | 19.1 |
| White | 6148 |
| Black | 28 |
| Asian | 107 |
| Native | 356 |
| Hispanic/Latino | 190 |
| Bachelor's or higher | 1384 |

## Districts

- [MT-01](/us/states/mt/districts/01.md) — 100% (congressional)
- [MT Senate District 38](/us/states/mt/districts/senate/38.md) — 100% (state senate)
- [MT House District 76](/us/states/mt/districts/house/76.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
