---
type: Jurisdiction
title: "Beadle County, SD"
classification: county
fips: "46005"
state: "SD"
demographics:
  population: 19309
  population_under_18: 5397
  population_18_64: 10351
  population_65_plus: 3561
  median_household_income: 67681
  poverty_rate: 13.61
  homeownership_rate: 72.9
  unemployment_rate: 1.91
  median_home_value: 175100
  gini_index: 0.4485
  vacancy_rate: 11.07
  race_white: 13797
  race_black: 190
  race_asian: 1892
  race_native: 290
  hispanic: 2878
  bachelors_plus: 4403
districts:
  - to: "us/states/sd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/sd/districts/senate/22"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/sd/districts/house/22"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sd]
timestamp: "2026-07-03"
---

# Beadle County, SD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 19309 |
| Under 18 | 5397 |
| 18–64 | 10351 |
| 65+ | 3561 |
| Median household income | 67681 |
| Poverty rate | 13.61 |
| Homeownership rate | 72.9 |
| Unemployment rate | 1.91 |
| Median home value | 175100 |
| Gini index | 0.4485 |
| Vacancy rate | 11.07 |
| White | 13797 |
| Black | 190 |
| Asian | 1892 |
| Native | 290 |
| Hispanic/Latino | 2878 |
| Bachelor's or higher | 4403 |

## Districts

- [SD-00](/us/states/sd/districts/00.md) — 100% (congressional)
- [SD Senate District 22](/us/states/sd/districts/senate/22.md) — 100% (state senate)
- [SD House District 22](/us/states/sd/districts/house/22.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
