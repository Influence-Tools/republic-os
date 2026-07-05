---
type: Jurisdiction
title: "Renville County, MN"
classification: county
fips: "27129"
state: "MN"
demographics:
  population: 14558
  population_under_18: 3392
  population_18_64: 7937
  population_65_plus: 3229
  median_household_income: 70625
  poverty_rate: 11.04
  homeownership_rate: 80.17
  unemployment_rate: 2.55
  median_home_value: 163200
  gini_index: 0.4199
  vacancy_rate: 12.43
  race_white: 12659
  race_black: 124
  race_asian: 97
  race_native: 123
  hispanic: 1489
  bachelors_plus: 2195
districts:
  - to: "us/states/mn/districts/07"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/mn/districts/senate/16"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mn/districts/house/16a"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Renville County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 14558 |
| Under 18 | 3392 |
| 18–64 | 7937 |
| 65+ | 3229 |
| Median household income | 70625 |
| Poverty rate | 11.04 |
| Homeownership rate | 80.17 |
| Unemployment rate | 2.55 |
| Median home value | 163200 |
| Gini index | 0.4199 |
| Vacancy rate | 12.43 |
| White | 12659 |
| Black | 124 |
| Asian | 97 |
| Native | 123 |
| Hispanic/Latino | 1489 |
| Bachelor's or higher | 2195 |

## Districts

- [MN-07](/us/states/mn/districts/07.md) — 100% (congressional)
- [MN Senate District 16](/us/states/mn/districts/senate/16.md) — 100% (state senate)
- [MN House District 16A](/us/states/mn/districts/house/16a.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
