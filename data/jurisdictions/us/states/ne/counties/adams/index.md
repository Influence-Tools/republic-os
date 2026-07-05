---
type: Jurisdiction
title: "Adams County, NE"
classification: county
fips: "31001"
state: "NE"
demographics:
  population: 31052
  population_under_18: 7502
  population_18_64: 17707
  population_65_plus: 5843
  median_household_income: 68365
  poverty_rate: 12.67
  homeownership_rate: 69.75
  unemployment_rate: 2.44
  median_home_value: 193100
  gini_index: 0.4606
  vacancy_rate: 6.16
  race_white: 26118
  race_black: 480
  race_asian: 300
  race_native: 67
  hispanic: 3869
  bachelors_plus: 8416
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

# Adams County, NE

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 31052 |
| Under 18 | 7502 |
| 18–64 | 17707 |
| 65+ | 5843 |
| Median household income | 68365 |
| Poverty rate | 12.67 |
| Homeownership rate | 69.75 |
| Unemployment rate | 2.44 |
| Median home value | 193100 |
| Gini index | 0.4606 |
| Vacancy rate | 6.16 |
| White | 26118 |
| Black | 480 |
| Asian | 300 |
| Native | 67 |
| Hispanic/Latino | 3869 |
| Bachelor's or higher | 8416 |

## Districts

- [NE-03](/us/states/ne/districts/03.md) — 100% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
