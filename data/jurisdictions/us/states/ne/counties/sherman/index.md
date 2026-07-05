---
type: Jurisdiction
title: "Sherman County, NE"
classification: county
fips: "31163"
state: "NE"
demographics:
  population: 2967
  population_under_18: 630
  population_18_64: 1510
  population_65_plus: 827
  median_household_income: 63578
  poverty_rate: 8.65
  homeownership_rate: 75.4
  unemployment_rate: 3.04
  median_home_value: 152000
  gini_index: 0.418
  vacancy_rate: 26.22
  race_white: 2783
  race_black: 9
  race_asian: 16
  race_native: 4
  hispanic: 84
  bachelors_plus: 584
districts:
  - to: "us/states/ne/districts/03"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ne]
timestamp: "2026-07-03"
---

# Sherman County, NE

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2967 |
| Under 18 | 630 |
| 18–64 | 1510 |
| 65+ | 827 |
| Median household income | 63578 |
| Poverty rate | 8.65 |
| Homeownership rate | 75.4 |
| Unemployment rate | 3.04 |
| Median home value | 152000 |
| Gini index | 0.418 |
| Vacancy rate | 26.22 |
| White | 2783 |
| Black | 9 |
| Asian | 16 |
| Native | 4 |
| Hispanic/Latino | 84 |
| Bachelor's or higher | 584 |

## Districts

- [NE-03](/us/states/ne/districts/03.md) — 100% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
