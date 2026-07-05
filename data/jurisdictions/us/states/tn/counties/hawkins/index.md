---
type: Jurisdiction
title: "Hawkins County, TN"
classification: county
fips: "47073"
state: "TN"
demographics:
  population: 57964
  population_under_18: 11113
  population_18_64: 34221
  population_65_plus: 12630
  median_household_income: 56936
  poverty_rate: 15.17
  homeownership_rate: 80.12
  unemployment_rate: 7.31
  median_home_value: 176300
  gini_index: 0.4323
  vacancy_rate: 14.13
  race_white: 54392
  race_black: 722
  race_asian: 344
  race_native: 36
  hispanic: 1181
  bachelors_plus: 9344
districts:
  - to: "us/states/tn/districts/01"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/tn/districts/senate/4"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/tn/districts/house/9"
    rel: in-district
    area_weight: 0.8087
  - to: "us/states/tn/districts/house/3"
    rel: in-district
    area_weight: 0.191
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Hawkins County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 57964 |
| Under 18 | 11113 |
| 18–64 | 34221 |
| 65+ | 12630 |
| Median household income | 56936 |
| Poverty rate | 15.17 |
| Homeownership rate | 80.12 |
| Unemployment rate | 7.31 |
| Median home value | 176300 |
| Gini index | 0.4323 |
| Vacancy rate | 14.13 |
| White | 54392 |
| Black | 722 |
| Asian | 344 |
| Native | 36 |
| Hispanic/Latino | 1181 |
| Bachelor's or higher | 9344 |

## Districts

- [TN-01](/us/states/tn/districts/01.md) — 100% (congressional)
- [TN Senate District 4](/us/states/tn/districts/senate/4.md) — 100% (state senate)
- [TN House District 9](/us/states/tn/districts/house/9.md) — 81% (state house)
- [TN House District 3](/us/states/tn/districts/house/3.md) — 19% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
