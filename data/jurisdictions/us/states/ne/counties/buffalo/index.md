---
type: Jurisdiction
title: "Buffalo County, NE"
classification: county
fips: "31019"
state: "NE"
demographics:
  population: 50579
  population_under_18: 11492
  population_18_64: 30693
  population_65_plus: 8394
  median_household_income: 75911
  poverty_rate: 9.88
  homeownership_rate: 66.4
  unemployment_rate: 2.56
  median_home_value: 246400
  gini_index: 0.4347
  vacancy_rate: 6.12
  race_white: 43775
  race_black: 467
  race_asian: 827
  race_native: 259
  hispanic: 5385
  bachelors_plus: 14557
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

# Buffalo County, NE

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 50579 |
| Under 18 | 11492 |
| 18–64 | 30693 |
| 65+ | 8394 |
| Median household income | 75911 |
| Poverty rate | 9.88 |
| Homeownership rate | 66.4 |
| Unemployment rate | 2.56 |
| Median home value | 246400 |
| Gini index | 0.4347 |
| Vacancy rate | 6.12 |
| White | 43775 |
| Black | 467 |
| Asian | 827 |
| Native | 259 |
| Hispanic/Latino | 5385 |
| Bachelor's or higher | 14557 |

## Districts

- [NE-03](/us/states/ne/districts/03.md) — 100% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
