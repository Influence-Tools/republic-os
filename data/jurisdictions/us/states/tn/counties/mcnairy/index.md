---
type: Jurisdiction
title: "McNairy County, TN"
classification: county
fips: "47109"
state: "TN"
demographics:
  population: 25970
  population_under_18: 5600
  population_18_64: 14960
  population_65_plus: 5410
  median_household_income: 53473
  poverty_rate: 16.52
  homeownership_rate: 79.74
  unemployment_rate: 5.81
  median_home_value: 161800
  gini_index: 0.437
  vacancy_rate: 19.37
  race_white: 23420
  race_black: 1394
  race_asian: 108
  race_native: 57
  hispanic: 561
  bachelors_plus: 3183
districts:
  - to: "us/states/tn/districts/08"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/tn/districts/senate/26"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/tn/districts/house/94"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# McNairy County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 25970 |
| Under 18 | 5600 |
| 18–64 | 14960 |
| 65+ | 5410 |
| Median household income | 53473 |
| Poverty rate | 16.52 |
| Homeownership rate | 79.74 |
| Unemployment rate | 5.81 |
| Median home value | 161800 |
| Gini index | 0.437 |
| Vacancy rate | 19.37 |
| White | 23420 |
| Black | 1394 |
| Asian | 108 |
| Native | 57 |
| Hispanic/Latino | 561 |
| Bachelor's or higher | 3183 |

## Districts

- [TN-08](/us/states/tn/districts/08.md) — 100% (congressional)
- [TN Senate District 26](/us/states/tn/districts/senate/26.md) — 100% (state senate)
- [TN House District 94](/us/states/tn/districts/house/94.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
