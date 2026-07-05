---
type: Jurisdiction
title: "Sioux County, IA"
classification: county
fips: "19167"
state: "IA"
demographics:
  population: 36212
  population_under_18: 9837
  population_18_64: 20509
  population_65_plus: 5866
  median_household_income: 86098
  poverty_rate: 6.67
  homeownership_rate: 76.13
  unemployment_rate: 1.52
  median_home_value: 250100
  gini_index: 0.4094
  vacancy_rate: 4.48
  race_white: 30791
  race_black: 214
  race_asian: 197
  race_native: 130
  hispanic: 5193
  bachelors_plus: 8344
districts:
  - to: "us/states/ia/districts/04"
    rel: in-district
    area_weight: 0.9992
  - to: "us/states/ia/districts/senate/2"
    rel: in-district
    area_weight: 0.9991
  - to: "us/states/ia/districts/house/3"
    rel: in-district
    area_weight: 0.5525
  - to: "us/states/ia/districts/house/4"
    rel: in-district
    area_weight: 0.4466
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Sioux County, IA

County jurisdiction — 5 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 36212 |
| Under 18 | 9837 |
| 18–64 | 20509 |
| 65+ | 5866 |
| Median household income | 86098 |
| Poverty rate | 6.67 |
| Homeownership rate | 76.13 |
| Unemployment rate | 1.52 |
| Median home value | 250100 |
| Gini index | 0.4094 |
| Vacancy rate | 4.48 |
| White | 30791 |
| Black | 214 |
| Asian | 197 |
| Native | 130 |
| Hispanic/Latino | 5193 |
| Bachelor's or higher | 8344 |

## Districts

- [IA-04](/us/states/ia/districts/04.md) — 100% (congressional)
- [IA Senate District 2](/us/states/ia/districts/senate/2.md) — 100% (state senate)
- [IA House District 3](/us/states/ia/districts/house/3.md) — 55% (state house)
- [IA House District 4](/us/states/ia/districts/house/4.md) — 45% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
