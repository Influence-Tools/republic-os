---
type: Jurisdiction
title: "Grant County, MN"
classification: county
fips: "27051"
state: "MN"
demographics:
  population: 6127
  population_under_18: 1422
  population_18_64: 3260
  population_65_plus: 1445
  median_household_income: 73917
  poverty_rate: 11.61
  homeownership_rate: 79.16
  unemployment_rate: 2.75
  median_home_value: 191000
  gini_index: 0.4685
  vacancy_rate: 20.62
  race_white: 5759
  race_black: 40
  race_asian: 4
  race_native: 23
  hispanic: 164
  bachelors_plus: 1170
districts:
  - to: "us/states/mn/districts/07"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mn/districts/senate/9"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mn/districts/house/9a"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Grant County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 6127 |
| Under 18 | 1422 |
| 18–64 | 3260 |
| 65+ | 1445 |
| Median household income | 73917 |
| Poverty rate | 11.61 |
| Homeownership rate | 79.16 |
| Unemployment rate | 2.75 |
| Median home value | 191000 |
| Gini index | 0.4685 |
| Vacancy rate | 20.62 |
| White | 5759 |
| Black | 40 |
| Asian | 4 |
| Native | 23 |
| Hispanic/Latino | 164 |
| Bachelor's or higher | 1170 |

## Districts

- [MN-07](/us/states/mn/districts/07.md) — 100% (congressional)
- [MN Senate District 9](/us/states/mn/districts/senate/9.md) — 100% (state senate)
- [MN House District 9A](/us/states/mn/districts/house/9a.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
