---
type: Jurisdiction
title: "Montgomery County, GA"
classification: county
fips: "13209"
state: "GA"
demographics:
  population: 8640
  population_under_18: 1750
  population_18_64: 5349
  population_65_plus: 1541
  median_household_income: 51941
  poverty_rate: 20.56
  homeownership_rate: 76.2
  unemployment_rate: 7.52
  median_home_value: 115500
  gini_index: 0.4848
  vacancy_rate: 17.16
  race_white: 5803
  race_black: 2019
  race_asian: 53
  race_native: 23
  hispanic: 646
  bachelors_plus: 1660
districts:
  - to: "us/states/ga/districts/12"
    rel: in-district
    area_weight: 0.9984
  - to: "us/states/ga/districts/senate/19"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ga/districts/house/156"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Montgomery County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8640 |
| Under 18 | 1750 |
| 18–64 | 5349 |
| 65+ | 1541 |
| Median household income | 51941 |
| Poverty rate | 20.56 |
| Homeownership rate | 76.2 |
| Unemployment rate | 7.52 |
| Median home value | 115500 |
| Gini index | 0.4848 |
| Vacancy rate | 17.16 |
| White | 5803 |
| Black | 2019 |
| Asian | 53 |
| Native | 23 |
| Hispanic/Latino | 646 |
| Bachelor's or higher | 1660 |

## Districts

- [GA-12](/us/states/ga/districts/12.md) — 100% (congressional)
- [GA Senate District 19](/us/states/ga/districts/senate/19.md) — 100% (state senate)
- [GA House District 156](/us/states/ga/districts/house/156.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
