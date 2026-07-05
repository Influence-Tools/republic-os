---
type: Jurisdiction
title: "Gage County, NE"
classification: county
fips: "31067"
state: "NE"
demographics:
  population: 21629
  population_under_18: 4888
  population_18_64: 11965
  population_65_plus: 4776
  median_household_income: 67247
  poverty_rate: 12.6
  homeownership_rate: 73.53
  unemployment_rate: 1.54
  median_home_value: 174000
  gini_index: 0.4241
  vacancy_rate: 10.31
  race_white: 20242
  race_black: 140
  race_asian: 144
  race_native: 99
  hispanic: 742
  bachelors_plus: 4427
districts:
  - to: "us/states/ne/districts/03"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ne]
timestamp: "2026-07-03"
---

# Gage County, NE

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 21629 |
| Under 18 | 4888 |
| 18–64 | 11965 |
| 65+ | 4776 |
| Median household income | 67247 |
| Poverty rate | 12.6 |
| Homeownership rate | 73.53 |
| Unemployment rate | 1.54 |
| Median home value | 174000 |
| Gini index | 0.4241 |
| Vacancy rate | 10.31 |
| White | 20242 |
| Black | 140 |
| Asian | 144 |
| Native | 99 |
| Hispanic/Latino | 742 |
| Bachelor's or higher | 4427 |

## Districts

- [NE-03](/us/states/ne/districts/03.md) — 100% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
