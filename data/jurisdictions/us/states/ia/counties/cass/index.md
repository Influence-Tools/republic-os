---
type: Jurisdiction
title: "Cass County, IA"
classification: county
fips: "19029"
state: "IA"
demographics:
  population: 13096
  population_under_18: 3035
  population_18_64: 7000
  population_65_plus: 3061
  median_household_income: 63013
  poverty_rate: 14.25
  homeownership_rate: 71.56
  unemployment_rate: 1.4
  median_home_value: 150300
  gini_index: 0.465
  vacancy_rate: 8.59
  race_white: 12384
  race_black: 118
  race_asian: 68
  race_native: 43
  hispanic: 357
  bachelors_plus: 2511
districts:
  - to: "us/states/ia/districts/03"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ia/districts/senate/9"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ia/districts/house/18"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Cass County, IA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 13096 |
| Under 18 | 3035 |
| 18–64 | 7000 |
| 65+ | 3061 |
| Median household income | 63013 |
| Poverty rate | 14.25 |
| Homeownership rate | 71.56 |
| Unemployment rate | 1.4 |
| Median home value | 150300 |
| Gini index | 0.465 |
| Vacancy rate | 8.59 |
| White | 12384 |
| Black | 118 |
| Asian | 68 |
| Native | 43 |
| Hispanic/Latino | 357 |
| Bachelor's or higher | 2511 |

## Districts

- [IA-03](/us/states/ia/districts/03.md) — 100% (congressional)
- [IA Senate District 9](/us/states/ia/districts/senate/9.md) — 100% (state senate)
- [IA House District 18](/us/states/ia/districts/house/18.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
