---
type: Jurisdiction
title: "Wood County, WI"
classification: county
fips: "55141"
state: "WI"
demographics:
  population: 74004
  population_under_18: 15845
  population_18_64: 42035
  population_65_plus: 16124
  median_household_income: 67989
  poverty_rate: 10.77
  homeownership_rate: 72.58
  unemployment_rate: 4.0
  median_home_value: 175600
  gini_index: 0.4319
  vacancy_rate: 7.2
  race_white: 67397
  race_black: 541
  race_asian: 1293
  race_native: 205
  hispanic: 2763
  bachelors_plus: 14860
districts:
  - to: "us/states/wi/districts/07"
    rel: in-district
    area_weight: 0.5629
  - to: "us/states/wi/districts/03"
    rel: in-district
    area_weight: 0.4371
  - to: "us/states/wi/districts/senate/29"
    rel: in-district
    area_weight: 0.5569
  - to: "us/states/wi/districts/senate/24"
    rel: in-district
    area_weight: 0.4431
  - to: "us/states/wi/districts/house/86"
    rel: in-district
    area_weight: 0.5569
  - to: "us/states/wi/districts/house/72"
    rel: in-district
    area_weight: 0.4431
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wi]
timestamp: "2026-07-03"
---

# Wood County, WI

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 74004 |
| Under 18 | 15845 |
| 18–64 | 42035 |
| 65+ | 16124 |
| Median household income | 67989 |
| Poverty rate | 10.77 |
| Homeownership rate | 72.58 |
| Unemployment rate | 4.0 |
| Median home value | 175600 |
| Gini index | 0.4319 |
| Vacancy rate | 7.2 |
| White | 67397 |
| Black | 541 |
| Asian | 1293 |
| Native | 205 |
| Hispanic/Latino | 2763 |
| Bachelor's or higher | 14860 |

## Districts

- [WI-07](/us/states/wi/districts/07.md) — 56% (congressional)
- [WI-03](/us/states/wi/districts/03.md) — 44% (congressional)
- [WI Senate District 29](/us/states/wi/districts/senate/29.md) — 56% (state senate)
- [WI Senate District 24](/us/states/wi/districts/senate/24.md) — 44% (state senate)
- [WI House District 86](/us/states/wi/districts/house/86.md) — 56% (state house)
- [WI House District 72](/us/states/wi/districts/house/72.md) — 44% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
