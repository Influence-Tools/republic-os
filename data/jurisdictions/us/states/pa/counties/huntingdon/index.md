---
type: Jurisdiction
title: "Huntingdon County, PA"
classification: county
fips: "42061"
state: "PA"
demographics:
  population: 43653
  population_under_18: 7742
  population_18_64: 26252
  population_65_plus: 9659
  median_household_income: 65557
  poverty_rate: 10.64
  homeownership_rate: 79.2
  unemployment_rate: 4.64
  median_home_value: 183200
  gini_index: 0.4191
  vacancy_rate: 22.13
  race_white: 39268
  race_black: 2020
  race_asian: 239
  race_native: 49
  hispanic: 911
  bachelors_plus: 8289
districts:
  - to: "us/states/pa/districts/13"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/pa/districts/senate/30"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/pa/districts/house/81"
    rel: in-district
    area_weight: 0.931
  - to: "us/states/pa/districts/house/80"
    rel: in-district
    area_weight: 0.0688
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, pa]
timestamp: "2026-07-03"
---

# Huntingdon County, PA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 43653 |
| Under 18 | 7742 |
| 18–64 | 26252 |
| 65+ | 9659 |
| Median household income | 65557 |
| Poverty rate | 10.64 |
| Homeownership rate | 79.2 |
| Unemployment rate | 4.64 |
| Median home value | 183200 |
| Gini index | 0.4191 |
| Vacancy rate | 22.13 |
| White | 39268 |
| Black | 2020 |
| Asian | 239 |
| Native | 49 |
| Hispanic/Latino | 911 |
| Bachelor's or higher | 8289 |

## Districts

- [PA-13](/us/states/pa/districts/13.md) — 100% (congressional)
- [PA Senate District 30](/us/states/pa/districts/senate/30.md) — 100% (state senate)
- [PA House District 81](/us/states/pa/districts/house/81.md) — 93% (state house)
- [PA House District 80](/us/states/pa/districts/house/80.md) — 7% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
