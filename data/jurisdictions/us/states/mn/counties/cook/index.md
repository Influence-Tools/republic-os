---
type: Jurisdiction
title: "Cook County, MN"
classification: county
fips: "27031"
state: "MN"
demographics:
  population: 5635
  population_under_18: 815
  population_18_64: 3063
  population_65_plus: 1757
  median_household_income: 72638
  poverty_rate: 10.17
  homeownership_rate: 77.68
  unemployment_rate: 2.22
  median_home_value: 336200
  gini_index: 0.4123
  vacancy_rate: 55.42
  race_white: 4742
  race_black: 76
  race_asian: 32
  race_native: 347
  hispanic: 176
  bachelors_plus: 3023
districts:
  - to: "us/states/mn/districts/08"
    rel: in-district
    area_weight: 0.4847
  - to: "us/states/mn/districts/senate/3"
    rel: in-district
    area_weight: 0.4825
  - to: "us/states/mn/districts/house/3a"
    rel: in-district
    area_weight: 0.4825
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Cook County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5635 |
| Under 18 | 815 |
| 18–64 | 3063 |
| 65+ | 1757 |
| Median household income | 72638 |
| Poverty rate | 10.17 |
| Homeownership rate | 77.68 |
| Unemployment rate | 2.22 |
| Median home value | 336200 |
| Gini index | 0.4123 |
| Vacancy rate | 55.42 |
| White | 4742 |
| Black | 76 |
| Asian | 32 |
| Native | 347 |
| Hispanic/Latino | 176 |
| Bachelor's or higher | 3023 |

## Districts

- [MN-08](/us/states/mn/districts/08.md) — 48% (congressional)
- [MN Senate District 3](/us/states/mn/districts/senate/3.md) — 48% (state senate)
- [MN House District 3A](/us/states/mn/districts/house/3a.md) — 48% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
