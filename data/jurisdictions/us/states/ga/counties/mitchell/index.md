---
type: Jurisdiction
title: "Mitchell County, GA"
classification: county
fips: "13205"
state: "GA"
demographics:
  population: 21058
  population_under_18: 4823
  population_18_64: 12312
  population_65_plus: 3923
  median_household_income: 57613
  poverty_rate: 23.44
  homeownership_rate: 65.17
  unemployment_rate: 5.95
  median_home_value: 106000
  gini_index: 0.452
  vacancy_rate: 13.46
  race_white: 9730
  race_black: 9531
  race_asian: 3
  race_native: 37
  hispanic: 1098
  bachelors_plus: 2954
districts:
  - to: "us/states/ga/districts/02"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ga/districts/house/171"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Mitchell County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 21058 |
| Under 18 | 4823 |
| 18–64 | 12312 |
| 65+ | 3923 |
| Median household income | 57613 |
| Poverty rate | 23.44 |
| Homeownership rate | 65.17 |
| Unemployment rate | 5.95 |
| Median home value | 106000 |
| Gini index | 0.452 |
| Vacancy rate | 13.46 |
| White | 9730 |
| Black | 9531 |
| Asian | 3 |
| Native | 37 |
| Hispanic/Latino | 1098 |
| Bachelor's or higher | 2954 |

## Districts

- [GA-02](/us/states/ga/districts/02.md) — 100% (congressional)
- [GA House District 171](/us/states/ga/districts/house/171.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
