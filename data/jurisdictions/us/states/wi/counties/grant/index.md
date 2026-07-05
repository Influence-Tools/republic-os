---
type: Jurisdiction
title: "Grant County, WI"
classification: county
fips: "55043"
state: "WI"
demographics:
  population: 51770
  population_under_18: 10942
  population_18_64: 31237
  population_65_plus: 9591
  median_household_income: 66858
  poverty_rate: 12.99
  homeownership_rate: 69.81
  unemployment_rate: 3.1
  median_home_value: 200700
  gini_index: 0.4331
  vacancy_rate: 10.62
  race_white: 48488
  race_black: 853
  race_asian: 368
  race_native: 80
  hispanic: 1332
  bachelors_plus: 11655
districts:
  - to: "us/states/wi/districts/03"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/wi/districts/senate/17"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/wi/districts/house/49"
    rel: in-district
    area_weight: 0.8203
  - to: "us/states/wi/districts/house/51"
    rel: in-district
    area_weight: 0.1796
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wi]
timestamp: "2026-07-03"
---

# Grant County, WI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 51770 |
| Under 18 | 10942 |
| 18–64 | 31237 |
| 65+ | 9591 |
| Median household income | 66858 |
| Poverty rate | 12.99 |
| Homeownership rate | 69.81 |
| Unemployment rate | 3.1 |
| Median home value | 200700 |
| Gini index | 0.4331 |
| Vacancy rate | 10.62 |
| White | 48488 |
| Black | 853 |
| Asian | 368 |
| Native | 80 |
| Hispanic/Latino | 1332 |
| Bachelor's or higher | 11655 |

## Districts

- [WI-03](/us/states/wi/districts/03.md) — 100% (congressional)
- [WI Senate District 17](/us/states/wi/districts/senate/17.md) — 100% (state senate)
- [WI House District 49](/us/states/wi/districts/house/49.md) — 82% (state house)
- [WI House District 51](/us/states/wi/districts/house/51.md) — 18% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
