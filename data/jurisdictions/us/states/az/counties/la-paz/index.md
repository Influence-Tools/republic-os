---
type: Jurisdiction
title: "La Paz County, AZ"
classification: county
fips: "04012"
state: "AZ"
demographics:
  population: 16664
  population_under_18: 2489
  population_18_64: 6986
  population_65_plus: 7189
  median_household_income: 49478
  poverty_rate: 17.45
  homeownership_rate: 72.1
  unemployment_rate: 10.04
  median_home_value: 135800
  gini_index: 0.4634
  vacancy_rate: 34.47
  race_white: 9848
  race_black: 238
  race_asian: 238
  race_native: 2202
  hispanic: 4263
  bachelors_plus: 2285
districts:
  - to: "us/states/az/districts/09"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/az/districts/senate/30"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/az/districts/house/30"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, az]
timestamp: "2026-07-03"
---

# La Paz County, AZ

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 16664 |
| Under 18 | 2489 |
| 18–64 | 6986 |
| 65+ | 7189 |
| Median household income | 49478 |
| Poverty rate | 17.45 |
| Homeownership rate | 72.1 |
| Unemployment rate | 10.04 |
| Median home value | 135800 |
| Gini index | 0.4634 |
| Vacancy rate | 34.47 |
| White | 9848 |
| Black | 238 |
| Asian | 238 |
| Native | 2202 |
| Hispanic/Latino | 4263 |
| Bachelor's or higher | 2285 |

## Districts

- [AZ-09](/us/states/az/districts/09.md) — 100% (congressional)
- [AZ Senate District 30](/us/states/az/districts/senate/30.md) — 100% (state senate)
- [AZ House District 30](/us/states/az/districts/house/30.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
