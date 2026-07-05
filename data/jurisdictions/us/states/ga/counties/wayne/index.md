---
type: Jurisdiction
title: "Wayne County, GA"
classification: county
fips: "13305"
state: "GA"
demographics:
  population: 30949
  population_under_18: 7410
  population_18_64: 18552
  population_65_plus: 4987
  median_household_income: 53427
  poverty_rate: 21.3
  homeownership_rate: 67.33
  unemployment_rate: 7.19
  median_home_value: 162800
  gini_index: 0.4401
  vacancy_rate: 12.93
  race_white: 21989
  race_black: 6091
  race_asian: 402
  race_native: 24
  hispanic: 1937
  bachelors_plus: 4672
districts:
  - to: "us/states/ga/districts/01"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/ga/districts/senate/19"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ga/districts/house/178"
    rel: in-district
    area_weight: 0.9044
  - to: "us/states/ga/districts/house/167"
    rel: in-district
    area_weight: 0.0955
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Wayne County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 30949 |
| Under 18 | 7410 |
| 18–64 | 18552 |
| 65+ | 4987 |
| Median household income | 53427 |
| Poverty rate | 21.3 |
| Homeownership rate | 67.33 |
| Unemployment rate | 7.19 |
| Median home value | 162800 |
| Gini index | 0.4401 |
| Vacancy rate | 12.93 |
| White | 21989 |
| Black | 6091 |
| Asian | 402 |
| Native | 24 |
| Hispanic/Latino | 1937 |
| Bachelor's or higher | 4672 |

## Districts

- [GA-01](/us/states/ga/districts/01.md) — 100% (congressional)
- [GA Senate District 19](/us/states/ga/districts/senate/19.md) — 100% (state senate)
- [GA House District 178](/us/states/ga/districts/house/178.md) — 90% (state house)
- [GA House District 167](/us/states/ga/districts/house/167.md) — 10% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
