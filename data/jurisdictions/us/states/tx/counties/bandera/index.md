---
type: Jurisdiction
title: "Bandera County, TX"
classification: county
fips: "48019"
state: "TX"
demographics:
  population: 22021
  population_under_18: 3651
  population_18_64: 11816
  population_65_plus: 6554
  median_household_income: 75813
  poverty_rate: 13.47
  homeownership_rate: 85.89
  unemployment_rate: 8.74
  median_home_value: 278400
  gini_index: 0.4527
  vacancy_rate: 20.11
  race_white: 16998
  race_black: 274
  race_asian: 110
  race_native: 131
  hispanic: 4619
  bachelors_plus: 6494
districts:
  - to: "us/states/tx/districts/21"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/tx/districts/senate/24"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/53"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Bandera County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 22021 |
| Under 18 | 3651 |
| 18–64 | 11816 |
| 65+ | 6554 |
| Median household income | 75813 |
| Poverty rate | 13.47 |
| Homeownership rate | 85.89 |
| Unemployment rate | 8.74 |
| Median home value | 278400 |
| Gini index | 0.4527 |
| Vacancy rate | 20.11 |
| White | 16998 |
| Black | 274 |
| Asian | 110 |
| Native | 131 |
| Hispanic/Latino | 4619 |
| Bachelor's or higher | 6494 |

## Districts

- [TX-21](/us/states/tx/districts/21.md) — 100% (congressional)
- [TX Senate District 24](/us/states/tx/districts/senate/24.md) — 100% (state senate)
- [TX House District 53](/us/states/tx/districts/house/53.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
