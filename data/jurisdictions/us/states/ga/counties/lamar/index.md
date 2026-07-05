---
type: Jurisdiction
title: "Lamar County, GA"
classification: county
fips: "13171"
state: "GA"
demographics:
  population: 19571
  population_under_18: 4000
  population_18_64: 12115
  population_65_plus: 3456
  median_household_income: 67062
  poverty_rate: 9.59
  homeownership_rate: 75.66
  unemployment_rate: 4.05
  median_home_value: 216500
  gini_index: 0.4128
  vacancy_rate: 9.32
  race_white: 13382
  race_black: 5304
  race_asian: 140
  race_native: 16
  hispanic: 661
  bachelors_plus: 3594
districts:
  - to: "us/states/ga/districts/03"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ga/districts/senate/16"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ga/districts/house/135"
    rel: in-district
    area_weight: 0.5911
  - to: "us/states/ga/districts/house/134"
    rel: in-district
    area_weight: 0.4088
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Lamar County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 19571 |
| Under 18 | 4000 |
| 18–64 | 12115 |
| 65+ | 3456 |
| Median household income | 67062 |
| Poverty rate | 9.59 |
| Homeownership rate | 75.66 |
| Unemployment rate | 4.05 |
| Median home value | 216500 |
| Gini index | 0.4128 |
| Vacancy rate | 9.32 |
| White | 13382 |
| Black | 5304 |
| Asian | 140 |
| Native | 16 |
| Hispanic/Latino | 661 |
| Bachelor's or higher | 3594 |

## Districts

- [GA-03](/us/states/ga/districts/03.md) — 100% (congressional)
- [GA Senate District 16](/us/states/ga/districts/senate/16.md) — 100% (state senate)
- [GA House District 135](/us/states/ga/districts/house/135.md) — 59% (state house)
- [GA House District 134](/us/states/ga/districts/house/134.md) — 41% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
