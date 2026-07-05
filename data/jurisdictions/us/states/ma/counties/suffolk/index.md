---
type: Jurisdiction
title: "Suffolk County, MA"
classification: county
fips: "25025"
state: "MA"
demographics:
  population: 785121
  population_under_18: 125812
  population_18_64: 555150
  population_65_plus: 104159
  median_household_income: 95631
  poverty_rate: 16.18
  homeownership_rate: 36.48
  unemployment_rate: 6.3
  median_home_value: 705800
  gini_index: 0.5251
  vacancy_rate: 8.43
  race_white: 362430
  race_black: 143125
  race_asian: 72712
  race_native: 2825
  hispanic: 182283
  bachelors_plus: 409219
districts:
  - to: "us/states/ma/districts/07"
    rel: in-district
    area_weight: 0.3081
  - to: "us/states/ma/districts/08"
    rel: in-district
    area_weight: 0.1782
  - to: "us/states/ma/districts/05"
    rel: in-district
    area_weight: 0.0832
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ma]
timestamp: "2026-07-03"
---

# Suffolk County, MA

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 785121 |
| Under 18 | 125812 |
| 18–64 | 555150 |
| 65+ | 104159 |
| Median household income | 95631 |
| Poverty rate | 16.18 |
| Homeownership rate | 36.48 |
| Unemployment rate | 6.3 |
| Median home value | 705800 |
| Gini index | 0.5251 |
| Vacancy rate | 8.43 |
| White | 362430 |
| Black | 143125 |
| Asian | 72712 |
| Native | 2825 |
| Hispanic/Latino | 182283 |
| Bachelor's or higher | 409219 |

## Districts

- [MA-07](/us/states/ma/districts/07.md) — 31% (congressional)
- [MA-08](/us/states/ma/districts/08.md) — 18% (congressional)
- [MA-05](/us/states/ma/districts/05.md) — 8% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
