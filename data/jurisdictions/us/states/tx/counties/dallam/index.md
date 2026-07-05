---
type: Jurisdiction
title: "Dallam County, TX"
classification: county
fips: "48111"
state: "TX"
demographics:
  population: 7298
  population_under_18: 2391
  population_18_64: 4092
  population_65_plus: 815
  median_household_income: 71500
  poverty_rate: 11.47
  homeownership_rate: 63.96
  unemployment_rate: 2.34
  median_home_value: 151400
  gini_index: 0.3149
  vacancy_rate: 15.27
  race_white: 3717
  race_black: 15
  race_asian: 3
  race_native: 264
  hispanic: 3965
  bachelors_plus: 662
districts:
  - to: "us/states/tx/districts/13"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tx/districts/senate/31"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tx/districts/house/86"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Dallam County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7298 |
| Under 18 | 2391 |
| 18–64 | 4092 |
| 65+ | 815 |
| Median household income | 71500 |
| Poverty rate | 11.47 |
| Homeownership rate | 63.96 |
| Unemployment rate | 2.34 |
| Median home value | 151400 |
| Gini index | 0.3149 |
| Vacancy rate | 15.27 |
| White | 3717 |
| Black | 15 |
| Asian | 3 |
| Native | 264 |
| Hispanic/Latino | 3965 |
| Bachelor's or higher | 662 |

## Districts

- [TX-13](/us/states/tx/districts/13.md) — 100% (congressional)
- [TX Senate District 31](/us/states/tx/districts/senate/31.md) — 100% (state senate)
- [TX House District 86](/us/states/tx/districts/house/86.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
