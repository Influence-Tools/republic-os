---
type: Jurisdiction
title: "Cherokee County, IA"
classification: county
fips: "19035"
state: "IA"
demographics:
  population: 11600
  population_under_18: 2575
  population_18_64: 6140
  population_65_plus: 2885
  median_household_income: 71269
  poverty_rate: 12.1
  homeownership_rate: 75.52
  unemployment_rate: 2.49
  median_home_value: 158700
  gini_index: 0.4514
  vacancy_rate: 9.21
  race_white: 10394
  race_black: 202
  race_asian: 43
  race_native: 0
  hispanic: 621
  bachelors_plus: 2638
districts:
  - to: "us/states/ia/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ia/districts/senate/3"
    rel: in-district
    area_weight: 0.5606
  - to: "us/states/ia/districts/senate/7"
    rel: in-district
    area_weight: 0.4394
  - to: "us/states/ia/districts/house/5"
    rel: in-district
    area_weight: 0.5606
  - to: "us/states/ia/districts/house/13"
    rel: in-district
    area_weight: 0.4394
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Cherokee County, IA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 11600 |
| Under 18 | 2575 |
| 18–64 | 6140 |
| 65+ | 2885 |
| Median household income | 71269 |
| Poverty rate | 12.1 |
| Homeownership rate | 75.52 |
| Unemployment rate | 2.49 |
| Median home value | 158700 |
| Gini index | 0.4514 |
| Vacancy rate | 9.21 |
| White | 10394 |
| Black | 202 |
| Asian | 43 |
| Native | 0 |
| Hispanic/Latino | 621 |
| Bachelor's or higher | 2638 |

## Districts

- [IA-04](/us/states/ia/districts/04.md) — 100% (congressional)
- [IA Senate District 3](/us/states/ia/districts/senate/3.md) — 56% (state senate)
- [IA Senate District 7](/us/states/ia/districts/senate/7.md) — 44% (state senate)
- [IA House District 5](/us/states/ia/districts/house/5.md) — 56% (state house)
- [IA House District 13](/us/states/ia/districts/house/13.md) — 44% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
