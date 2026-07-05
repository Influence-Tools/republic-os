---
type: Jurisdiction
title: "Clay County, TX"
classification: county
fips: "48077"
state: "TX"
demographics:
  population: 10495
  population_under_18: 2038
  population_18_64: 6002
  population_65_plus: 2455
  median_household_income: 80114
  poverty_rate: 8.39
  homeownership_rate: 83.98
  unemployment_rate: 1.95
  median_home_value: 171500
  gini_index: 0.4031
  vacancy_rate: 16.93
  race_white: 9426
  race_black: 104
  race_asian: 84
  race_native: 61
  hispanic: 746
  bachelors_plus: 2173
districts:
  - to: "us/states/tx/districts/13"
    rel: in-district
    area_weight: 0.9976
  - to: "us/states/tx/districts/senate/30"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/tx/districts/house/69"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Clay County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 10495 |
| Under 18 | 2038 |
| 18–64 | 6002 |
| 65+ | 2455 |
| Median household income | 80114 |
| Poverty rate | 8.39 |
| Homeownership rate | 83.98 |
| Unemployment rate | 1.95 |
| Median home value | 171500 |
| Gini index | 0.4031 |
| Vacancy rate | 16.93 |
| White | 9426 |
| Black | 104 |
| Asian | 84 |
| Native | 61 |
| Hispanic/Latino | 746 |
| Bachelor's or higher | 2173 |

## Districts

- [TX-13](/us/states/tx/districts/13.md) — 100% (congressional)
- [TX Senate District 30](/us/states/tx/districts/senate/30.md) — 100% (state senate)
- [TX House District 69](/us/states/tx/districts/house/69.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
