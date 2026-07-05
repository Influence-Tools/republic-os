---
type: Jurisdiction
title: "Yuma County, AZ"
classification: county
fips: "04027"
state: "AZ"
demographics:
  population: 211741
  population_under_18: 51996
  population_18_64: 115976
  population_65_plus: 43769
  median_household_income: 62876
  poverty_rate: 15.6
  homeownership_rate: 70.97
  unemployment_rate: 6.93
  median_home_value: 217800
  gini_index: 0.4438
  vacancy_rate: 16.66
  race_white: 79485
  race_black: 3578
  race_asian: 2233
  race_native: 2965
  hispanic: 137437
  bachelors_plus: 31600
districts:
  - to: "us/states/az/districts/09"
    rel: in-district
    area_weight: 0.5624
  - to: "us/states/az/districts/07"
    rel: in-district
    area_weight: 0.4375
  - to: "us/states/az/districts/senate/25"
    rel: in-district
    area_weight: 0.5623
  - to: "us/states/az/districts/senate/23"
    rel: in-district
    area_weight: 0.4376
  - to: "us/states/az/districts/house/25"
    rel: in-district
    area_weight: 0.5623
  - to: "us/states/az/districts/house/23"
    rel: in-district
    area_weight: 0.4376
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, az]
timestamp: "2026-07-03"
---

# Yuma County, AZ

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 211741 |
| Under 18 | 51996 |
| 18–64 | 115976 |
| 65+ | 43769 |
| Median household income | 62876 |
| Poverty rate | 15.6 |
| Homeownership rate | 70.97 |
| Unemployment rate | 6.93 |
| Median home value | 217800 |
| Gini index | 0.4438 |
| Vacancy rate | 16.66 |
| White | 79485 |
| Black | 3578 |
| Asian | 2233 |
| Native | 2965 |
| Hispanic/Latino | 137437 |
| Bachelor's or higher | 31600 |

## Districts

- [AZ-09](/us/states/az/districts/09.md) — 56% (congressional)
- [AZ-07](/us/states/az/districts/07.md) — 44% (congressional)
- [AZ Senate District 25](/us/states/az/districts/senate/25.md) — 56% (state senate)
- [AZ Senate District 23](/us/states/az/districts/senate/23.md) — 44% (state senate)
- [AZ House District 25](/us/states/az/districts/house/25.md) — 56% (state house)
- [AZ House District 23](/us/states/az/districts/house/23.md) — 44% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
