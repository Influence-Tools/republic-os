---
type: Jurisdiction
title: "Lake of the Woods County, MN"
classification: county
fips: "27077"
state: "MN"
demographics:
  population: 3821
  population_under_18: 704
  population_18_64: 2091
  population_65_plus: 1026
  median_household_income: 77546
  poverty_rate: 6.35
  homeownership_rate: 81.78
  unemployment_rate: 1.47
  median_home_value: 216100
  gini_index: 0.4118
  vacancy_rate: 48.04
  race_white: 3350
  race_black: 11
  race_asian: 7
  race_native: 76
  hispanic: 60
  bachelors_plus: 941
districts:
  - to: "us/states/mn/districts/08"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/mn/districts/senate/2"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/mn/districts/house/2a"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Lake of the Woods County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3821 |
| Under 18 | 704 |
| 18–64 | 2091 |
| 65+ | 1026 |
| Median household income | 77546 |
| Poverty rate | 6.35 |
| Homeownership rate | 81.78 |
| Unemployment rate | 1.47 |
| Median home value | 216100 |
| Gini index | 0.4118 |
| Vacancy rate | 48.04 |
| White | 3350 |
| Black | 11 |
| Asian | 7 |
| Native | 76 |
| Hispanic/Latino | 60 |
| Bachelor's or higher | 941 |

## Districts

- [MN-08](/us/states/mn/districts/08.md) — 100% (congressional)
- [MN Senate District 2](/us/states/mn/districts/senate/2.md) — 100% (state senate)
- [MN House District 2A](/us/states/mn/districts/house/2a.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
