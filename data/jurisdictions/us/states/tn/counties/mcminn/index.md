---
type: Jurisdiction
title: "McMinn County, TN"
classification: county
fips: "47107"
state: "TN"
demographics:
  population: 54884
  population_under_18: 11627
  population_18_64: 32118
  population_65_plus: 11139
  median_household_income: 61470
  poverty_rate: 12.96
  homeownership_rate: 75.78
  unemployment_rate: 4.86
  median_home_value: 211800
  gini_index: 0.4473
  vacancy_rate: 12.09
  race_white: 48155
  race_black: 1765
  race_asian: 450
  race_native: 21
  hispanic: 2506
  bachelors_plus: 9717
districts:
  - to: "us/states/tn/districts/03"
    rel: in-district
    area_weight: 0.9972
  - to: "us/states/tn/districts/senate/1"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tn/districts/house/23"
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

# McMinn County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 54884 |
| Under 18 | 11627 |
| 18–64 | 32118 |
| 65+ | 11139 |
| Median household income | 61470 |
| Poverty rate | 12.96 |
| Homeownership rate | 75.78 |
| Unemployment rate | 4.86 |
| Median home value | 211800 |
| Gini index | 0.4473 |
| Vacancy rate | 12.09 |
| White | 48155 |
| Black | 1765 |
| Asian | 450 |
| Native | 21 |
| Hispanic/Latino | 2506 |
| Bachelor's or higher | 9717 |

## Districts

- [TN-03](/us/states/tn/districts/03.md) — 100% (congressional)
- [TN Senate District 1](/us/states/tn/districts/senate/1.md) — 100% (state senate)
- [TN House District 23](/us/states/tn/districts/house/23.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
