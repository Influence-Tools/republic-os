---
type: Jurisdiction
title: "Shelby County, IA"
classification: county
fips: "19165"
state: "IA"
demographics:
  population: 11778
  population_under_18: 2699
  population_18_64: 6355
  population_65_plus: 2724
  median_household_income: 72738
  poverty_rate: 7.63
  homeownership_rate: 77.8
  unemployment_rate: 3.19
  median_home_value: 164000
  gini_index: 0.447
  vacancy_rate: 10.27
  race_white: 10854
  race_black: 37
  race_asian: 56
  race_native: 101
  hispanic: 518
  bachelors_plus: 2648
districts:
  - to: "us/states/ia/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ia/districts/senate/6"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ia/districts/house/11"
    rel: in-district
    area_weight: 0.5093
  - to: "us/states/ia/districts/house/12"
    rel: in-district
    area_weight: 0.4907
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Shelby County, IA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 11778 |
| Under 18 | 2699 |
| 18–64 | 6355 |
| 65+ | 2724 |
| Median household income | 72738 |
| Poverty rate | 7.63 |
| Homeownership rate | 77.8 |
| Unemployment rate | 3.19 |
| Median home value | 164000 |
| Gini index | 0.447 |
| Vacancy rate | 10.27 |
| White | 10854 |
| Black | 37 |
| Asian | 56 |
| Native | 101 |
| Hispanic/Latino | 518 |
| Bachelor's or higher | 2648 |

## Districts

- [IA-04](/us/states/ia/districts/04.md) — 100% (congressional)
- [IA Senate District 6](/us/states/ia/districts/senate/6.md) — 100% (state senate)
- [IA House District 11](/us/states/ia/districts/house/11.md) — 51% (state house)
- [IA House District 12](/us/states/ia/districts/house/12.md) — 49% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
