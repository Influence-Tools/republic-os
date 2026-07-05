---
type: Jurisdiction
title: "Madison County, AR"
classification: county
fips: "05087"
state: "AR"
demographics:
  population: 17329
  population_under_18: 3952
  population_18_64: 9962
  population_65_plus: 3415
  median_household_income: 56798
  poverty_rate: 14.06
  homeownership_rate: 79.51
  unemployment_rate: 5.3
  median_home_value: 178100
  gini_index: 0.4405
  vacancy_rate: 16.54
  race_white: 12100
  race_black: 22
  race_asian: 128
  race_native: 272
  hispanic: 1125
  bachelors_plus: 2137
districts:
  - to: "us/states/ar/districts/03"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ar/districts/senate/28"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ar/districts/house/26"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Madison County, AR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 17329 |
| Under 18 | 3952 |
| 18–64 | 9962 |
| 65+ | 3415 |
| Median household income | 56798 |
| Poverty rate | 14.06 |
| Homeownership rate | 79.51 |
| Unemployment rate | 5.3 |
| Median home value | 178100 |
| Gini index | 0.4405 |
| Vacancy rate | 16.54 |
| White | 12100 |
| Black | 22 |
| Asian | 128 |
| Native | 272 |
| Hispanic/Latino | 1125 |
| Bachelor's or higher | 2137 |

## Districts

- [AR-03](/us/states/ar/districts/03.md) — 100% (congressional)
- [AR Senate District 28](/us/states/ar/districts/senate/28.md) — 100% (state senate)
- [AR House District 26](/us/states/ar/districts/house/26.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
