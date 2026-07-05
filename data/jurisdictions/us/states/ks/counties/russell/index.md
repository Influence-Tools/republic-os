---
type: Jurisdiction
title: "Russell County, KS"
classification: county
fips: "20167"
state: "KS"
demographics:
  population: 6679
  population_under_18: 1460
  population_18_64: 3478
  population_65_plus: 1741
  median_household_income: 62392
  poverty_rate: 14.69
  homeownership_rate: 75.06
  unemployment_rate: 1.84
  median_home_value: 119000
  gini_index: 0.445
  vacancy_rate: 15.62
  race_white: 6036
  race_black: 24
  race_asian: 24
  race_native: 13
  hispanic: 277
  bachelors_plus: 1266
districts:
  - to: "us/states/ks/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/senate/36"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ks/districts/house/109"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Russell County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 6679 |
| Under 18 | 1460 |
| 18–64 | 3478 |
| 65+ | 1741 |
| Median household income | 62392 |
| Poverty rate | 14.69 |
| Homeownership rate | 75.06 |
| Unemployment rate | 1.84 |
| Median home value | 119000 |
| Gini index | 0.445 |
| Vacancy rate | 15.62 |
| White | 6036 |
| Black | 24 |
| Asian | 24 |
| Native | 13 |
| Hispanic/Latino | 277 |
| Bachelor's or higher | 1266 |

## Districts

- [KS-01](/us/states/ks/districts/01.md) — 100% (congressional)
- [KS Senate District 36](/us/states/ks/districts/senate/36.md) — 100% (state senate)
- [KS House District 109](/us/states/ks/districts/house/109.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
