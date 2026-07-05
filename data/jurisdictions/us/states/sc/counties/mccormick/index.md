---
type: Jurisdiction
title: "McCormick County, SC"
classification: county
fips: "45065"
state: "SC"
demographics:
  population: 9760
  population_under_18: 992
  population_18_64: 4916
  population_65_plus: 3852
  median_household_income: 55798
  poverty_rate: 17.61
  homeownership_rate: 87.9
  unemployment_rate: 4.36
  median_home_value: 168700
  gini_index: 0.4617
  vacancy_rate: 26.01
  race_white: 5477
  race_black: 3913
  race_asian: 16
  race_native: 4
  hispanic: 80
  bachelors_plus: 2562
districts:
  - to: "us/states/sc/districts/03"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/sc/districts/senate/25"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/sc/districts/house/12"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sc]
timestamp: "2026-07-03"
---

# McCormick County, SC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9760 |
| Under 18 | 992 |
| 18–64 | 4916 |
| 65+ | 3852 |
| Median household income | 55798 |
| Poverty rate | 17.61 |
| Homeownership rate | 87.9 |
| Unemployment rate | 4.36 |
| Median home value | 168700 |
| Gini index | 0.4617 |
| Vacancy rate | 26.01 |
| White | 5477 |
| Black | 3913 |
| Asian | 16 |
| Native | 4 |
| Hispanic/Latino | 80 |
| Bachelor's or higher | 2562 |

## Districts

- [SC-03](/us/states/sc/districts/03.md) — 100% (congressional)
- [SC Senate District 25](/us/states/sc/districts/senate/25.md) — 100% (state senate)
- [SC House District 12](/us/states/sc/districts/house/12.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
