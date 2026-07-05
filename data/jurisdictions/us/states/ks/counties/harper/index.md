---
type: Jurisdiction
title: "Harper County, KS"
classification: county
fips: "20077"
state: "KS"
demographics:
  population: 5400
  population_under_18: 1391
  population_18_64: 2838
  population_65_plus: 1171
  median_household_income: 53488
  poverty_rate: 17.3
  homeownership_rate: 75.11
  unemployment_rate: 1.97
  median_home_value: 83800
  gini_index: 0.4511
  vacancy_rate: 26.95
  race_white: 4825
  race_black: 45
  race_asian: 15
  race_native: 15
  hispanic: 436
  bachelors_plus: 1031
districts:
  - to: "us/states/ks/districts/04"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ks/districts/senate/32"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ks/districts/house/116"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Harper County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5400 |
| Under 18 | 1391 |
| 18–64 | 2838 |
| 65+ | 1171 |
| Median household income | 53488 |
| Poverty rate | 17.3 |
| Homeownership rate | 75.11 |
| Unemployment rate | 1.97 |
| Median home value | 83800 |
| Gini index | 0.4511 |
| Vacancy rate | 26.95 |
| White | 4825 |
| Black | 45 |
| Asian | 15 |
| Native | 15 |
| Hispanic/Latino | 436 |
| Bachelor's or higher | 1031 |

## Districts

- [KS-04](/us/states/ks/districts/04.md) — 100% (congressional)
- [KS Senate District 32](/us/states/ks/districts/senate/32.md) — 100% (state senate)
- [KS House District 116](/us/states/ks/districts/house/116.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
