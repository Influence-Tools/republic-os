---
type: Jurisdiction
title: "San Saba County, TX"
classification: county
fips: "48411"
state: "TX"
demographics:
  population: 5696
  population_under_18: 1090
  population_18_64: 3323
  population_65_plus: 1283
  median_household_income: 55819
  poverty_rate: 10.73
  homeownership_rate: 71.67
  unemployment_rate: 3.09
  median_home_value: 168700
  gini_index: 0.4222
  vacancy_rate: 26.28
  race_white: 4128
  race_black: 141
  race_asian: 14
  race_native: 18
  hispanic: 1746
  bachelors_plus: 1316
districts:
  - to: "us/states/tx/districts/11"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/tx/districts/senate/28"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/68"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# San Saba County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5696 |
| Under 18 | 1090 |
| 18–64 | 3323 |
| 65+ | 1283 |
| Median household income | 55819 |
| Poverty rate | 10.73 |
| Homeownership rate | 71.67 |
| Unemployment rate | 3.09 |
| Median home value | 168700 |
| Gini index | 0.4222 |
| Vacancy rate | 26.28 |
| White | 4128 |
| Black | 141 |
| Asian | 14 |
| Native | 18 |
| Hispanic/Latino | 1746 |
| Bachelor's or higher | 1316 |

## Districts

- [TX-11](/us/states/tx/districts/11.md) — 100% (congressional)
- [TX Senate District 28](/us/states/tx/districts/senate/28.md) — 100% (state senate)
- [TX House District 68](/us/states/tx/districts/house/68.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
