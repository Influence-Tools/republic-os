---
type: Jurisdiction
title: "Greene County, TN"
classification: county
fips: "47059"
state: "TN"
demographics:
  population: 71628
  population_under_18: 13591
  population_18_64: 42199
  population_65_plus: 15838
  median_household_income: 56194
  poverty_rate: 15.36
  homeownership_rate: 77.11
  unemployment_rate: 5.73
  median_home_value: 207500
  gini_index: 0.4691
  vacancy_rate: 13.14
  race_white: 65436
  race_black: 1253
  race_asian: 365
  race_native: 152
  hispanic: 2773
  bachelors_plus: 13394
districts:
  - to: "us/states/tn/districts/01"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/tn/districts/senate/9"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/tn/districts/house/5"
    rel: in-district
    area_weight: 0.9993
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Greene County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 71628 |
| Under 18 | 13591 |
| 18–64 | 42199 |
| 65+ | 15838 |
| Median household income | 56194 |
| Poverty rate | 15.36 |
| Homeownership rate | 77.11 |
| Unemployment rate | 5.73 |
| Median home value | 207500 |
| Gini index | 0.4691 |
| Vacancy rate | 13.14 |
| White | 65436 |
| Black | 1253 |
| Asian | 365 |
| Native | 152 |
| Hispanic/Latino | 2773 |
| Bachelor's or higher | 13394 |

## Districts

- [TN-01](/us/states/tn/districts/01.md) — 100% (congressional)
- [TN Senate District 9](/us/states/tn/districts/senate/9.md) — 100% (state senate)
- [TN House District 5](/us/states/tn/districts/house/5.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
