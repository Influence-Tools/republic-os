---
type: Jurisdiction
title: "Sevier County, TN"
classification: county
fips: "47155"
state: "TN"
demographics:
  population: 99652
  population_under_18: 20757
  population_18_64: 58605
  population_65_plus: 20290
  median_household_income: 62581
  poverty_rate: 13.47
  homeownership_rate: 70.69
  unemployment_rate: 3.34
  median_home_value: 299000
  gini_index: 0.453
  vacancy_rate: 31.58
  race_white: 85838
  race_black: 1184
  race_asian: 1295
  race_native: 161
  hispanic: 9577
  bachelors_plus: 20978
districts:
  - to: "us/states/tn/districts/01"
    rel: in-district
    area_weight: 0.9973
  - to: "us/states/tn/districts/senate/9"
    rel: in-district
    area_weight: 0.583
  - to: "us/states/tn/districts/senate/8"
    rel: in-district
    area_weight: 0.4163
  - to: "us/states/tn/districts/house/12"
    rel: in-district
    area_weight: 0.738
  - to: "us/states/tn/districts/house/17"
    rel: in-district
    area_weight: 0.2613
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Sevier County, TN

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 99652 |
| Under 18 | 20757 |
| 18–64 | 58605 |
| 65+ | 20290 |
| Median household income | 62581 |
| Poverty rate | 13.47 |
| Homeownership rate | 70.69 |
| Unemployment rate | 3.34 |
| Median home value | 299000 |
| Gini index | 0.453 |
| Vacancy rate | 31.58 |
| White | 85838 |
| Black | 1184 |
| Asian | 1295 |
| Native | 161 |
| Hispanic/Latino | 9577 |
| Bachelor's or higher | 20978 |

## Districts

- [TN-01](/us/states/tn/districts/01.md) — 100% (congressional)
- [TN Senate District 9](/us/states/tn/districts/senate/9.md) — 58% (state senate)
- [TN Senate District 8](/us/states/tn/districts/senate/8.md) — 42% (state senate)
- [TN House District 12](/us/states/tn/districts/house/12.md) — 74% (state house)
- [TN House District 17](/us/states/tn/districts/house/17.md) — 26% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
