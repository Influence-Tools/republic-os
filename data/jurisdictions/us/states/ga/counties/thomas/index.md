---
type: Jurisdiction
title: "Thomas County, GA"
classification: county
fips: "13275"
state: "GA"
demographics:
  population: 45777
  population_under_18: 10796
  population_18_64: 26261
  population_65_plus: 8720
  median_household_income: 60736
  poverty_rate: 17.95
  homeownership_rate: 63.77
  unemployment_rate: 5.63
  median_home_value: 196700
  gini_index: 0.458
  vacancy_rate: 11.58
  race_white: 26300
  race_black: 16069
  race_asian: 404
  race_native: 188
  hispanic: 1792
  bachelors_plus: 9672
districts:
  - to: "us/states/ga/districts/02"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/ga/districts/senate/11"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ga/districts/house/173"
    rel: in-district
    area_weight: 0.8287
  - to: "us/states/ga/districts/house/172"
    rel: in-district
    area_weight: 0.1711
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Thomas County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 45777 |
| Under 18 | 10796 |
| 18–64 | 26261 |
| 65+ | 8720 |
| Median household income | 60736 |
| Poverty rate | 17.95 |
| Homeownership rate | 63.77 |
| Unemployment rate | 5.63 |
| Median home value | 196700 |
| Gini index | 0.458 |
| Vacancy rate | 11.58 |
| White | 26300 |
| Black | 16069 |
| Asian | 404 |
| Native | 188 |
| Hispanic/Latino | 1792 |
| Bachelor's or higher | 9672 |

## Districts

- [GA-02](/us/states/ga/districts/02.md) — 100% (congressional)
- [GA Senate District 11](/us/states/ga/districts/senate/11.md) — 100% (state senate)
- [GA House District 173](/us/states/ga/districts/house/173.md) — 83% (state house)
- [GA House District 172](/us/states/ga/districts/house/172.md) — 17% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
