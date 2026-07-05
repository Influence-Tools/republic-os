---
type: Jurisdiction
title: "Jefferson County, TN"
classification: county
fips: "47089"
state: "TN"
demographics:
  population: 56864
  population_under_18: 10933
  population_18_64: 34167
  population_65_plus: 11764
  median_household_income: 66114
  poverty_rate: 11.39
  homeownership_rate: 75.82
  unemployment_rate: 4.59
  median_home_value: 229300
  gini_index: 0.4546
  vacancy_rate: 14.88
  race_white: 51517
  race_black: 844
  race_asian: 318
  race_native: 36
  hispanic: 2648
  bachelors_plus: 11781
districts:
  - to: "us/states/tn/districts/01"
    rel: in-district
    area_weight: 0.9685
  - to: "us/states/tn/districts/02"
    rel: in-district
    area_weight: 0.0315
  - to: "us/states/tn/districts/senate/8"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/tn/districts/house/17"
    rel: in-district
    area_weight: 0.6443
  - to: "us/states/tn/districts/house/11"
    rel: in-district
    area_weight: 0.3554
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Jefferson County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 56864 |
| Under 18 | 10933 |
| 18–64 | 34167 |
| 65+ | 11764 |
| Median household income | 66114 |
| Poverty rate | 11.39 |
| Homeownership rate | 75.82 |
| Unemployment rate | 4.59 |
| Median home value | 229300 |
| Gini index | 0.4546 |
| Vacancy rate | 14.88 |
| White | 51517 |
| Black | 844 |
| Asian | 318 |
| Native | 36 |
| Hispanic/Latino | 2648 |
| Bachelor's or higher | 11781 |

## Districts

- [TN-01](/us/states/tn/districts/01.md) — 97% (congressional)
- [TN-02](/us/states/tn/districts/02.md) — 3% (congressional)
- [TN Senate District 8](/us/states/tn/districts/senate/8.md) — 100% (state senate)
- [TN House District 17](/us/states/tn/districts/house/17.md) — 64% (state house)
- [TN House District 11](/us/states/tn/districts/house/11.md) — 36% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
