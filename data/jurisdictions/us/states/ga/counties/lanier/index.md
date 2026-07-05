---
type: Jurisdiction
title: "Lanier County, GA"
classification: county
fips: "13173"
state: "GA"
demographics:
  population: 10221
  population_under_18: 2303
  population_18_64: 6365
  population_65_plus: 1553
  median_household_income: 47186
  poverty_rate: 26.15
  homeownership_rate: 73.21
  unemployment_rate: 3.99
  median_home_value: 162300
  gini_index: 0.4853
  vacancy_rate: 16.51
  race_white: 6684
  race_black: 2476
  race_asian: 129
  race_native: 9
  hispanic: 758
  bachelors_plus: 1852
districts:
  - to: "us/states/ga/districts/08"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ga/districts/senate/8"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ga/districts/house/176"
    rel: in-district
    area_weight: 0.9987
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Lanier County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 10221 |
| Under 18 | 2303 |
| 18–64 | 6365 |
| 65+ | 1553 |
| Median household income | 47186 |
| Poverty rate | 26.15 |
| Homeownership rate | 73.21 |
| Unemployment rate | 3.99 |
| Median home value | 162300 |
| Gini index | 0.4853 |
| Vacancy rate | 16.51 |
| White | 6684 |
| Black | 2476 |
| Asian | 129 |
| Native | 9 |
| Hispanic/Latino | 758 |
| Bachelor's or higher | 1852 |

## Districts

- [GA-08](/us/states/ga/districts/08.md) — 100% (congressional)
- [GA Senate District 8](/us/states/ga/districts/senate/8.md) — 100% (state senate)
- [GA House District 176](/us/states/ga/districts/house/176.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
