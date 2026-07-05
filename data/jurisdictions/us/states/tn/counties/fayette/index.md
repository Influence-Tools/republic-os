---
type: Jurisdiction
title: "Fayette County, TN"
classification: county
fips: "47047"
state: "TN"
demographics:
  population: 43267
  population_under_18: 7763
  population_18_64: 25566
  population_65_plus: 9938
  median_household_income: 88456
  poverty_rate: 10.27
  homeownership_rate: 81.43
  unemployment_rate: 4.76
  median_home_value: 340800
  gini_index: 0.4415
  vacancy_rate: 6.94
  race_white: 28511
  race_black: 10858
  race_asian: 302
  race_native: 20
  hispanic: 1645
  bachelors_plus: 11481
districts:
  - to: "us/states/tn/districts/08"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tn/districts/senate/26"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tn/districts/house/94"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Fayette County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 43267 |
| Under 18 | 7763 |
| 18–64 | 25566 |
| 65+ | 9938 |
| Median household income | 88456 |
| Poverty rate | 10.27 |
| Homeownership rate | 81.43 |
| Unemployment rate | 4.76 |
| Median home value | 340800 |
| Gini index | 0.4415 |
| Vacancy rate | 6.94 |
| White | 28511 |
| Black | 10858 |
| Asian | 302 |
| Native | 20 |
| Hispanic/Latino | 1645 |
| Bachelor's or higher | 11481 |

## Districts

- [TN-08](/us/states/tn/districts/08.md) — 100% (congressional)
- [TN Senate District 26](/us/states/tn/districts/senate/26.md) — 100% (state senate)
- [TN House District 94](/us/states/tn/districts/house/94.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
