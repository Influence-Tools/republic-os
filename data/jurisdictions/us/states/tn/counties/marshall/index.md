---
type: Jurisdiction
title: "Marshall County, TN"
classification: county
fips: "47117"
state: "TN"
demographics:
  population: 36049
  population_under_18: 8442
  population_18_64: 21517
  population_65_plus: 6090
  median_household_income: 71049
  poverty_rate: 11.78
  homeownership_rate: 76.81
  unemployment_rate: 3.92
  median_home_value: 279800
  gini_index: 0.4536
  vacancy_rate: 7.64
  race_white: 31052
  race_black: 1347
  race_asian: 250
  race_native: 30
  hispanic: 2542
  bachelors_plus: 7265
districts:
  - to: "us/states/tn/districts/05"
    rel: in-district
    area_weight: 0.9934
  - to: "us/states/tn/districts/04"
    rel: in-district
    area_weight: 0.0066
  - to: "us/states/tn/districts/senate/28"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tn/districts/house/92"
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

# Marshall County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 36049 |
| Under 18 | 8442 |
| 18–64 | 21517 |
| 65+ | 6090 |
| Median household income | 71049 |
| Poverty rate | 11.78 |
| Homeownership rate | 76.81 |
| Unemployment rate | 3.92 |
| Median home value | 279800 |
| Gini index | 0.4536 |
| Vacancy rate | 7.64 |
| White | 31052 |
| Black | 1347 |
| Asian | 250 |
| Native | 30 |
| Hispanic/Latino | 2542 |
| Bachelor's or higher | 7265 |

## Districts

- [TN-05](/us/states/tn/districts/05.md) — 99% (congressional)
- [TN-04](/us/states/tn/districts/04.md) — 1% (congressional)
- [TN Senate District 28](/us/states/tn/districts/senate/28.md) — 100% (state senate)
- [TN House District 92](/us/states/tn/districts/house/92.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
