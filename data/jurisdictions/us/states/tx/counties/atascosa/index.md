---
type: Jurisdiction
title: "Atascosa County, TX"
classification: county
fips: "48013"
state: "TX"
demographics:
  population: 51008
  population_under_18: 13541
  population_18_64: 29699
  population_65_plus: 7768
  median_household_income: 70770
  poverty_rate: 15.83
  homeownership_rate: 77.36
  unemployment_rate: 4.09
  median_home_value: 174800
  gini_index: 0.4472
  vacancy_rate: 12.64
  race_white: 23692
  race_black: 627
  race_asian: 318
  race_native: 441
  hispanic: 33363
  bachelors_plus: 6427
districts:
  - to: "us/states/tx/districts/28"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/tx/districts/senate/19"
    rel: in-district
    area_weight: 0.7563
  - to: "us/states/tx/districts/senate/24"
    rel: in-district
    area_weight: 0.2436
  - to: "us/states/tx/districts/house/80"
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

# Atascosa County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 51008 |
| Under 18 | 13541 |
| 18–64 | 29699 |
| 65+ | 7768 |
| Median household income | 70770 |
| Poverty rate | 15.83 |
| Homeownership rate | 77.36 |
| Unemployment rate | 4.09 |
| Median home value | 174800 |
| Gini index | 0.4472 |
| Vacancy rate | 12.64 |
| White | 23692 |
| Black | 627 |
| Asian | 318 |
| Native | 441 |
| Hispanic/Latino | 33363 |
| Bachelor's or higher | 6427 |

## Districts

- [TX-28](/us/states/tx/districts/28.md) — 100% (congressional)
- [TX Senate District 19](/us/states/tx/districts/senate/19.md) — 76% (state senate)
- [TX Senate District 24](/us/states/tx/districts/senate/24.md) — 24% (state senate)
- [TX House District 80](/us/states/tx/districts/house/80.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
