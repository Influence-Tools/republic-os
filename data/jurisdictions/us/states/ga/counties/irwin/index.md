---
type: Jurisdiction
title: "Irwin County, GA"
classification: county
fips: "13155"
state: "GA"
demographics:
  population: 9285
  population_under_18: 2107
  population_18_64: 5497
  population_65_plus: 1681
  median_household_income: 51384
  poverty_rate: 22.42
  homeownership_rate: 70.44
  unemployment_rate: 4.03
  median_home_value: 105600
  gini_index: 0.4544
  vacancy_rate: 15.01
  race_white: 6442
  race_black: 2241
  race_asian: 9
  race_native: 0
  hispanic: 673
  bachelors_plus: 1366
districts:
  - to: "us/states/ga/districts/08"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ga/districts/senate/13"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ga/districts/house/169"
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

# Irwin County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9285 |
| Under 18 | 2107 |
| 18–64 | 5497 |
| 65+ | 1681 |
| Median household income | 51384 |
| Poverty rate | 22.42 |
| Homeownership rate | 70.44 |
| Unemployment rate | 4.03 |
| Median home value | 105600 |
| Gini index | 0.4544 |
| Vacancy rate | 15.01 |
| White | 6442 |
| Black | 2241 |
| Asian | 9 |
| Native | 0 |
| Hispanic/Latino | 673 |
| Bachelor's or higher | 1366 |

## Districts

- [GA-08](/us/states/ga/districts/08.md) — 100% (congressional)
- [GA Senate District 13](/us/states/ga/districts/senate/13.md) — 100% (state senate)
- [GA House District 169](/us/states/ga/districts/house/169.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
