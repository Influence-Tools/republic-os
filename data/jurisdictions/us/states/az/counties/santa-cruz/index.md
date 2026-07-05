---
type: Jurisdiction
title: "Santa Cruz County, AZ"
classification: county
fips: "04023"
state: "AZ"
demographics:
  population: 48926
  population_under_18: 12606
  population_18_64: 26893
  population_65_plus: 9427
  median_household_income: 55217
  poverty_rate: 20.18
  homeownership_rate: 69.25
  unemployment_rate: 12.18
  median_home_value: 233000
  gini_index: 0.4363
  vacancy_rate: 11.78
  race_white: 13936
  race_black: 119
  race_asian: 143
  race_native: 282
  hispanic: 40367
  bachelors_plus: 10260
districts:
  - to: "us/states/az/districts/07"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/az/districts/senate/21"
    rel: in-district
    area_weight: 0.6238
  - to: "us/states/az/districts/senate/19"
    rel: in-district
    area_weight: 0.376
  - to: "us/states/az/districts/house/21"
    rel: in-district
    area_weight: 0.6238
  - to: "us/states/az/districts/house/19"
    rel: in-district
    area_weight: 0.376
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, az]
timestamp: "2026-07-03"
---

# Santa Cruz County, AZ

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 48926 |
| Under 18 | 12606 |
| 18–64 | 26893 |
| 65+ | 9427 |
| Median household income | 55217 |
| Poverty rate | 20.18 |
| Homeownership rate | 69.25 |
| Unemployment rate | 12.18 |
| Median home value | 233000 |
| Gini index | 0.4363 |
| Vacancy rate | 11.78 |
| White | 13936 |
| Black | 119 |
| Asian | 143 |
| Native | 282 |
| Hispanic/Latino | 40367 |
| Bachelor's or higher | 10260 |

## Districts

- [AZ-07](/us/states/az/districts/07.md) — 100% (congressional)
- [AZ Senate District 21](/us/states/az/districts/senate/21.md) — 62% (state senate)
- [AZ Senate District 19](/us/states/az/districts/senate/19.md) — 38% (state senate)
- [AZ House District 21](/us/states/az/districts/house/21.md) — 62% (state house)
- [AZ House District 19](/us/states/az/districts/house/19.md) — 38% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
