---
type: Jurisdiction
title: "Towns County, GA"
classification: county
fips: "13281"
state: "GA"
demographics:
  population: 12913
  population_under_18: 1619
  population_18_64: 6525
  population_65_plus: 4769
  median_household_income: 59135
  poverty_rate: 13.29
  homeownership_rate: 82.29
  unemployment_rate: 4.64
  median_home_value: 316100
  gini_index: 0.5399
  vacancy_rate: 32.74
  race_white: 12022
  race_black: 190
  race_asian: 6
  race_native: 26
  hispanic: 421
  bachelors_plus: 4581
districts:
  - to: "us/states/ga/districts/09"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ga/districts/senate/50"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/ga/districts/house/8"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Towns County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 12913 |
| Under 18 | 1619 |
| 18–64 | 6525 |
| 65+ | 4769 |
| Median household income | 59135 |
| Poverty rate | 13.29 |
| Homeownership rate | 82.29 |
| Unemployment rate | 4.64 |
| Median home value | 316100 |
| Gini index | 0.5399 |
| Vacancy rate | 32.74 |
| White | 12022 |
| Black | 190 |
| Asian | 6 |
| Native | 26 |
| Hispanic/Latino | 421 |
| Bachelor's or higher | 4581 |

## Districts

- [GA-09](/us/states/ga/districts/09.md) — 100% (congressional)
- [GA Senate District 50](/us/states/ga/districts/senate/50.md) — 100% (state senate)
- [GA House District 8](/us/states/ga/districts/house/8.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
