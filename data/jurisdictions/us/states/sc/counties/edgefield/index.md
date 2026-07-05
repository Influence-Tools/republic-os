---
type: Jurisdiction
title: "Edgefield County, SC"
classification: county
fips: "45037"
state: "SC"
demographics:
  population: 27476
  population_under_18: 4557
  population_18_64: 17498
  population_65_plus: 5421
  median_household_income: 73029
  poverty_rate: 17.77
  homeownership_rate: 80.1
  unemployment_rate: 4.78
  median_home_value: 202700
  gini_index: 0.4522
  vacancy_rate: 15.16
  race_white: 15993
  race_black: 8432
  race_asian: 111
  race_native: 35
  hispanic: 1976
  bachelors_plus: 6362
districts:
  - to: "us/states/sc/districts/03"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/sc/districts/senate/25"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/sc/districts/house/82"
    rel: in-district
    area_weight: 0.6629
  - to: "us/states/sc/districts/house/83"
    rel: in-district
    area_weight: 0.3368
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sc]
timestamp: "2026-07-03"
---

# Edgefield County, SC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 27476 |
| Under 18 | 4557 |
| 18–64 | 17498 |
| 65+ | 5421 |
| Median household income | 73029 |
| Poverty rate | 17.77 |
| Homeownership rate | 80.1 |
| Unemployment rate | 4.78 |
| Median home value | 202700 |
| Gini index | 0.4522 |
| Vacancy rate | 15.16 |
| White | 15993 |
| Black | 8432 |
| Asian | 111 |
| Native | 35 |
| Hispanic/Latino | 1976 |
| Bachelor's or higher | 6362 |

## Districts

- [SC-03](/us/states/sc/districts/03.md) — 100% (congressional)
- [SC Senate District 25](/us/states/sc/districts/senate/25.md) — 100% (state senate)
- [SC House District 82](/us/states/sc/districts/house/82.md) — 66% (state house)
- [SC House District 83](/us/states/sc/districts/house/83.md) — 34% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
