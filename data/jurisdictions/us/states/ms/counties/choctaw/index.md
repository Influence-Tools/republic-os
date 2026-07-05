---
type: Jurisdiction
title: "Choctaw County, MS"
classification: county
fips: "28019"
state: "MS"
demographics:
  population: 8118
  population_under_18: 1737
  population_18_64: 4498
  population_65_plus: 1883
  median_household_income: 50919
  poverty_rate: 18.45
  homeownership_rate: 79.45
  unemployment_rate: 9.83
  median_home_value: 117200
  gini_index: 0.4158
  vacancy_rate: 20.82
  race_white: 5455
  race_black: 2255
  race_asian: 75
  race_native: 13
  hispanic: 154
  bachelors_plus: 1589
districts:
  - to: "us/states/ms/districts/01"
    rel: in-district
    area_weight: 0.999
  - to: "us/states/ms/districts/senate/15"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ms/districts/house/35"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Choctaw County, MS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8118 |
| Under 18 | 1737 |
| 18–64 | 4498 |
| 65+ | 1883 |
| Median household income | 50919 |
| Poverty rate | 18.45 |
| Homeownership rate | 79.45 |
| Unemployment rate | 9.83 |
| Median home value | 117200 |
| Gini index | 0.4158 |
| Vacancy rate | 20.82 |
| White | 5455 |
| Black | 2255 |
| Asian | 75 |
| Native | 13 |
| Hispanic/Latino | 154 |
| Bachelor's or higher | 1589 |

## Districts

- [MS-01](/us/states/ms/districts/01.md) — 100% (congressional)
- [MS Senate District 15](/us/states/ms/districts/senate/15.md) — 100% (state senate)
- [MS House District 35](/us/states/ms/districts/house/35.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
