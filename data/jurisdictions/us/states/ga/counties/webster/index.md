---
type: Jurisdiction
title: "Webster County, GA"
classification: county
fips: "13307"
state: "GA"
demographics:
  population: 2381
  population_under_18: 339
  population_18_64: 1579
  population_65_plus: 463
  median_household_income: 46792
  poverty_rate: 22.32
  homeownership_rate: 76.99
  unemployment_rate: 4.16
  median_home_value: 82600
  gini_index: 0.4165
  vacancy_rate: 26.25
  race_white: 986
  race_black: 1336
  race_asian: 0
  race_native: 0
  hispanic: 105
  bachelors_plus: 190
districts:
  - to: "us/states/ga/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ga/districts/house/151"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Webster County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2381 |
| Under 18 | 339 |
| 18–64 | 1579 |
| 65+ | 463 |
| Median household income | 46792 |
| Poverty rate | 22.32 |
| Homeownership rate | 76.99 |
| Unemployment rate | 4.16 |
| Median home value | 82600 |
| Gini index | 0.4165 |
| Vacancy rate | 26.25 |
| White | 986 |
| Black | 1336 |
| Asian | 0 |
| Native | 0 |
| Hispanic/Latino | 105 |
| Bachelor's or higher | 190 |

## Districts

- [GA-02](/us/states/ga/districts/02.md) — 100% (congressional)
- [GA House District 151](/us/states/ga/districts/house/151.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
