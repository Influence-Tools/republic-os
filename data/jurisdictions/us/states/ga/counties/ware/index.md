---
type: Jurisdiction
title: "Ware County, GA"
classification: county
fips: "13299"
state: "GA"
demographics:
  population: 35976
  population_under_18: 8934
  population_18_64: 20875
  population_65_plus: 6167
  median_household_income: 47448
  poverty_rate: 21.53
  homeownership_rate: 63.07
  unemployment_rate: 5.87
  median_home_value: 109500
  gini_index: 0.4491
  vacancy_rate: 18.73
  race_white: 22209
  race_black: 10880
  race_asian: 462
  race_native: 77
  hispanic: 1828
  bachelors_plus: 4900
districts:
  - to: "us/states/ga/districts/01"
    rel: in-district
    area_weight: 0.9989
  - to: "us/states/ga/districts/senate/8"
    rel: in-district
    area_weight: 0.7971
  - to: "us/states/ga/districts/senate/3"
    rel: in-district
    area_weight: 0.2029
  - to: "us/states/ga/districts/house/174"
    rel: in-district
    area_weight: 0.6442
  - to: "us/states/ga/districts/house/176"
    rel: in-district
    area_weight: 0.3556
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Ware County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 35976 |
| Under 18 | 8934 |
| 18–64 | 20875 |
| 65+ | 6167 |
| Median household income | 47448 |
| Poverty rate | 21.53 |
| Homeownership rate | 63.07 |
| Unemployment rate | 5.87 |
| Median home value | 109500 |
| Gini index | 0.4491 |
| Vacancy rate | 18.73 |
| White | 22209 |
| Black | 10880 |
| Asian | 462 |
| Native | 77 |
| Hispanic/Latino | 1828 |
| Bachelor's or higher | 4900 |

## Districts

- [GA-01](/us/states/ga/districts/01.md) — 100% (congressional)
- [GA Senate District 8](/us/states/ga/districts/senate/8.md) — 80% (state senate)
- [GA Senate District 3](/us/states/ga/districts/senate/3.md) — 20% (state senate)
- [GA House District 174](/us/states/ga/districts/house/174.md) — 64% (state house)
- [GA House District 176](/us/states/ga/districts/house/176.md) — 36% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
