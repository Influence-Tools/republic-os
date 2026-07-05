---
type: Jurisdiction
title: "Gilmer County, GA"
classification: county
fips: "13123"
state: "GA"
demographics:
  population: 32426
  population_under_18: 5936
  population_18_64: 17724
  population_65_plus: 8766
  median_household_income: 74499
  poverty_rate: 15.97
  homeownership_rate: 80.72
  unemployment_rate: 2.73
  median_home_value: 314000
  gini_index: 0.4229
  vacancy_rate: 29.68
  race_white: 27690
  race_black: 90
  race_asian: 173
  race_native: 421
  hispanic: 3989
  bachelors_plus: 8247
districts:
  - to: "us/states/ga/districts/09"
    rel: in-district
    area_weight: 0.9981
  - to: "us/states/ga/districts/senate/51"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ga/districts/house/7"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Gilmer County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 32426 |
| Under 18 | 5936 |
| 18–64 | 17724 |
| 65+ | 8766 |
| Median household income | 74499 |
| Poverty rate | 15.97 |
| Homeownership rate | 80.72 |
| Unemployment rate | 2.73 |
| Median home value | 314000 |
| Gini index | 0.4229 |
| Vacancy rate | 29.68 |
| White | 27690 |
| Black | 90 |
| Asian | 173 |
| Native | 421 |
| Hispanic/Latino | 3989 |
| Bachelor's or higher | 8247 |

## Districts

- [GA-09](/us/states/ga/districts/09.md) — 100% (congressional)
- [GA Senate District 51](/us/states/ga/districts/senate/51.md) — 100% (state senate)
- [GA House District 7](/us/states/ga/districts/house/7.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
