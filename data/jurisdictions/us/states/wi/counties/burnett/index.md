---
type: Jurisdiction
title: "Burnett County, WI"
classification: county
fips: "55013"
state: "WI"
demographics:
  population: 16916
  population_under_18: 2649
  population_18_64: 8807
  population_65_plus: 5460
  median_household_income: 62819
  poverty_rate: 12.76
  homeownership_rate: 85.85
  unemployment_rate: 4.88
  median_home_value: 231300
  gini_index: 0.466
  vacancy_rate: 53.31
  race_white: 15226
  race_black: 148
  race_asian: 92
  race_native: 518
  hispanic: 333
  bachelors_plus: 3954
districts:
  - to: "us/states/wi/districts/07"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/wi/districts/senate/25"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/wi/districts/house/75"
    rel: in-district
    area_weight: 0.809
  - to: "us/states/wi/districts/house/74"
    rel: in-district
    area_weight: 0.1908
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wi]
timestamp: "2026-07-03"
---

# Burnett County, WI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 16916 |
| Under 18 | 2649 |
| 18–64 | 8807 |
| 65+ | 5460 |
| Median household income | 62819 |
| Poverty rate | 12.76 |
| Homeownership rate | 85.85 |
| Unemployment rate | 4.88 |
| Median home value | 231300 |
| Gini index | 0.466 |
| Vacancy rate | 53.31 |
| White | 15226 |
| Black | 148 |
| Asian | 92 |
| Native | 518 |
| Hispanic/Latino | 333 |
| Bachelor's or higher | 3954 |

## Districts

- [WI-07](/us/states/wi/districts/07.md) — 100% (congressional)
- [WI Senate District 25](/us/states/wi/districts/senate/25.md) — 100% (state senate)
- [WI House District 75](/us/states/wi/districts/house/75.md) — 81% (state house)
- [WI House District 74](/us/states/wi/districts/house/74.md) — 19% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
