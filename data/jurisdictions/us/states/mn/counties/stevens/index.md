---
type: Jurisdiction
title: "Stevens County, MN"
classification: county
fips: "27149"
state: "MN"
demographics:
  population: 9739
  population_under_18: 2174
  population_18_64: 5925
  population_65_plus: 1640
  median_household_income: 75733
  poverty_rate: 11.13
  homeownership_rate: 63.38
  unemployment_rate: 1.95
  median_home_value: 202800
  gini_index: 0.4895
  vacancy_rate: 7.01
  race_white: 7936
  race_black: 104
  race_asian: 175
  race_native: 135
  hispanic: 1152
  bachelors_plus: 2310
districts:
  - to: "us/states/mn/districts/07"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mn/districts/senate/12"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mn/districts/house/12a"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Stevens County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9739 |
| Under 18 | 2174 |
| 18–64 | 5925 |
| 65+ | 1640 |
| Median household income | 75733 |
| Poverty rate | 11.13 |
| Homeownership rate | 63.38 |
| Unemployment rate | 1.95 |
| Median home value | 202800 |
| Gini index | 0.4895 |
| Vacancy rate | 7.01 |
| White | 7936 |
| Black | 104 |
| Asian | 175 |
| Native | 135 |
| Hispanic/Latino | 1152 |
| Bachelor's or higher | 2310 |

## Districts

- [MN-07](/us/states/mn/districts/07.md) — 100% (congressional)
- [MN Senate District 12](/us/states/mn/districts/senate/12.md) — 100% (state senate)
- [MN House District 12A](/us/states/mn/districts/house/12a.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
