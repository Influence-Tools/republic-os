---
type: Jurisdiction
title: "Coffee County, TN"
classification: county
fips: "47031"
state: "TN"
demographics:
  population: 59710
  population_under_18: 15644
  population_18_64: 18408
  population_65_plus: 25658
  median_household_income: 61505
  poverty_rate: 17.37
  homeownership_rate: 69.0
  unemployment_rate: 3.56
  median_home_value: 246800
  gini_index: 0.4245
  vacancy_rate: 9.31
  race_white: 51977
  race_black: 2526
  race_asian: 764
  race_native: 14
  hispanic: 3770
  bachelors_plus: 12422
districts:
  - to: "us/states/tn/districts/04"
    rel: in-district
    area_weight: 0.9985
  - to: "us/states/tn/districts/senate/16"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tn/districts/house/47"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Coffee County, TN

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 59710 |
| Under 18 | 15644 |
| 18–64 | 18408 |
| 65+ | 25658 |
| Median household income | 61505 |
| Poverty rate | 17.37 |
| Homeownership rate | 69.0 |
| Unemployment rate | 3.56 |
| Median home value | 246800 |
| Gini index | 0.4245 |
| Vacancy rate | 9.31 |
| White | 51977 |
| Black | 2526 |
| Asian | 764 |
| Native | 14 |
| Hispanic/Latino | 3770 |
| Bachelor's or higher | 12422 |

## Districts

- [TN-04](/us/states/tn/districts/04.md) — 100% (congressional)
- [TN Senate District 16](/us/states/tn/districts/senate/16.md) — 100% (state senate)
- [TN House District 47](/us/states/tn/districts/house/47.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
