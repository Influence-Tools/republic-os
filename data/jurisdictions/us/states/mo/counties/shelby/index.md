---
type: Jurisdiction
title: "Shelby County, MO"
classification: county
fips: "29205"
state: "MO"
demographics:
  population: 5986
  population_under_18: 1434
  population_18_64: 3220
  population_65_plus: 1332
  median_household_income: 51594
  poverty_rate: 15.92
  homeownership_rate: 77.5
  unemployment_rate: 1.77
  median_home_value: 99900
  gini_index: 0.4498
  vacancy_rate: 18.95
  race_white: 5625
  race_black: 98
  race_asian: 21
  race_native: 2
  hispanic: 139
  bachelors_plus: 964
districts:
  - to: "us/states/mo/districts/06"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mo/districts/senate/18"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mo/districts/house/4"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Shelby County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5986 |
| Under 18 | 1434 |
| 18–64 | 3220 |
| 65+ | 1332 |
| Median household income | 51594 |
| Poverty rate | 15.92 |
| Homeownership rate | 77.5 |
| Unemployment rate | 1.77 |
| Median home value | 99900 |
| Gini index | 0.4498 |
| Vacancy rate | 18.95 |
| White | 5625 |
| Black | 98 |
| Asian | 21 |
| Native | 2 |
| Hispanic/Latino | 139 |
| Bachelor's or higher | 964 |

## Districts

- [MO-06](/us/states/mo/districts/06.md) — 100% (congressional)
- [MO Senate District 18](/us/states/mo/districts/senate/18.md) — 100% (state senate)
- [MO House District 4](/us/states/mo/districts/house/4.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
