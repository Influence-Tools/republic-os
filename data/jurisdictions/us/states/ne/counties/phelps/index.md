---
type: Jurisdiction
title: "Phelps County, NE"
classification: county
fips: "31137"
state: "NE"
demographics:
  population: 9009
  population_under_18: 2187
  population_18_64: 4912
  population_65_plus: 1910
  median_household_income: 68919
  poverty_rate: 12.24
  homeownership_rate: 68.31
  unemployment_rate: 1.2
  median_home_value: 194900
  gini_index: 0.5197
  vacancy_rate: 6.09
  race_white: 8117
  race_black: 77
  race_asian: 14
  race_native: 41
  hispanic: 618
  bachelors_plus: 2375
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

# Phelps County, NE

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9009 |
| Under 18 | 2187 |
| 18–64 | 4912 |
| 65+ | 1910 |
| Median household income | 68919 |
| Poverty rate | 12.24 |
| Homeownership rate | 68.31 |
| Unemployment rate | 1.2 |
| Median home value | 194900 |
| Gini index | 0.5197 |
| Vacancy rate | 6.09 |
| White | 8117 |
| Black | 77 |
| Asian | 14 |
| Native | 41 |
| Hispanic/Latino | 618 |
| Bachelor's or higher | 2375 |

## Districts

- [NE-03](/us/states/ne/districts/03.md) — 100% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
