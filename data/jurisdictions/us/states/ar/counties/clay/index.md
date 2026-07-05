---
type: Jurisdiction
title: "Clay County, AR"
classification: county
fips: "05021"
state: "AR"
demographics:
  population: 14280
  population_under_18: 3067
  population_18_64: 8101
  population_65_plus: 3112
  median_household_income: 51481
  poverty_rate: 17.19
  homeownership_rate: 74.72
  unemployment_rate: 6.3
  median_home_value: 94600
  gini_index: 0.4218
  vacancy_rate: 19.63
  race_white: 13353
  race_black: 10
  race_asian: 4
  race_native: 57
  hispanic: 158
  bachelors_plus: 2128
districts:
  - to: "us/states/ar/districts/01"
    rel: in-district
    area_weight: 0.9979
  - to: "us/states/ar/districts/senate/21"
    rel: in-district
    area_weight: 0.999
  - to: "us/states/ar/districts/house/1"
    rel: in-district
    area_weight: 0.999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Clay County, AR

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 14280 |
| Under 18 | 3067 |
| 18–64 | 8101 |
| 65+ | 3112 |
| Median household income | 51481 |
| Poverty rate | 17.19 |
| Homeownership rate | 74.72 |
| Unemployment rate | 6.3 |
| Median home value | 94600 |
| Gini index | 0.4218 |
| Vacancy rate | 19.63 |
| White | 13353 |
| Black | 10 |
| Asian | 4 |
| Native | 57 |
| Hispanic/Latino | 158 |
| Bachelor's or higher | 2128 |

## Districts

- [AR-01](/us/states/ar/districts/01.md) — 100% (congressional)
- [AR Senate District 21](/us/states/ar/districts/senate/21.md) — 100% (state senate)
- [AR House District 1](/us/states/ar/districts/house/1.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
