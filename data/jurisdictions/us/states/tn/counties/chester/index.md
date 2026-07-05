---
type: Jurisdiction
title: "Chester County, TN"
classification: county
fips: "47023"
state: "TN"
demographics:
  population: 17611
  population_under_18: 4398
  population_18_64: 5801
  population_65_plus: 7412
  median_household_income: 59341
  poverty_rate: 16.05
  homeownership_rate: 75.43
  unemployment_rate: 4.13
  median_home_value: 164400
  gini_index: 0.4551
  vacancy_rate: 11.66
  race_white: 14928
  race_black: 1667
  race_asian: 29
  race_native: 29
  hispanic: 593
  bachelors_plus: 3493
districts:
  - to: "us/states/tn/districts/08"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tn/districts/senate/26"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tn/districts/house/72"
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

# Chester County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 17611 |
| Under 18 | 4398 |
| 18–64 | 5801 |
| 65+ | 7412 |
| Median household income | 59341 |
| Poverty rate | 16.05 |
| Homeownership rate | 75.43 |
| Unemployment rate | 4.13 |
| Median home value | 164400 |
| Gini index | 0.4551 |
| Vacancy rate | 11.66 |
| White | 14928 |
| Black | 1667 |
| Asian | 29 |
| Native | 29 |
| Hispanic/Latino | 593 |
| Bachelor's or higher | 3493 |

## Districts

- [TN-08](/us/states/tn/districts/08.md) — 100% (congressional)
- [TN Senate District 26](/us/states/tn/districts/senate/26.md) — 100% (state senate)
- [TN House District 72](/us/states/tn/districts/house/72.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
