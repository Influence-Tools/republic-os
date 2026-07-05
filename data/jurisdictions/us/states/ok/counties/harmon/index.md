---
type: Jurisdiction
title: "Harmon County, OK"
classification: county
fips: "40057"
state: "OK"
demographics:
  population: 2406
  population_under_18: 587
  population_18_64: 1303
  population_65_plus: 516
  median_household_income: 43333
  poverty_rate: 22.72
  homeownership_rate: 69.71
  unemployment_rate: 7.21
  median_home_value: 79700
  gini_index: 0.5205
  vacancy_rate: 28.8
  race_white: 1615
  race_black: 217
  race_asian: 25
  race_native: 45
  hispanic: 773
  bachelors_plus: 325
districts:
  - to: "us/states/ok/districts/03"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ok/districts/senate/38"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ok/districts/house/52"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Harmon County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2406 |
| Under 18 | 587 |
| 18–64 | 1303 |
| 65+ | 516 |
| Median household income | 43333 |
| Poverty rate | 22.72 |
| Homeownership rate | 69.71 |
| Unemployment rate | 7.21 |
| Median home value | 79700 |
| Gini index | 0.5205 |
| Vacancy rate | 28.8 |
| White | 1615 |
| Black | 217 |
| Asian | 25 |
| Native | 45 |
| Hispanic/Latino | 773 |
| Bachelor's or higher | 325 |

## Districts

- [OK-03](/us/states/ok/districts/03.md) — 100% (congressional)
- [OK Senate District 38](/us/states/ok/districts/senate/38.md) — 100% (state senate)
- [OK House District 52](/us/states/ok/districts/house/52.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
