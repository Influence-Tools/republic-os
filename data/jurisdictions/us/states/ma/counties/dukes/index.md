---
type: Jurisdiction
title: "Dukes County, MA"
classification: county
fips: "25007"
state: "MA"
demographics:
  population: 20933
  population_under_18: 3513
  population_18_64: 11882
  population_65_plus: 5538
  median_household_income: 125786
  poverty_rate: 4.43
  homeownership_rate: 82.08
  unemployment_rate: 6.56
  median_home_value: 1165800
  gini_index: 0.5535
  vacancy_rate: 57.45
  race_white: 16860
  race_black: 574
  race_asian: 309
  race_native: 222
  hispanic: 682
  bachelors_plus: 12627
districts:
  - to: "us/states/ma/districts/09"
    rel: in-district
    area_weight: 0.2533
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ma]
timestamp: "2026-07-03"
---

# Dukes County, MA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 20933 |
| Under 18 | 3513 |
| 18–64 | 11882 |
| 65+ | 5538 |
| Median household income | 125786 |
| Poverty rate | 4.43 |
| Homeownership rate | 82.08 |
| Unemployment rate | 6.56 |
| Median home value | 1165800 |
| Gini index | 0.5535 |
| Vacancy rate | 57.45 |
| White | 16860 |
| Black | 574 |
| Asian | 309 |
| Native | 222 |
| Hispanic/Latino | 682 |
| Bachelor's or higher | 12627 |

## Districts

- [MA-09](/us/states/ma/districts/09.md) — 25% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
