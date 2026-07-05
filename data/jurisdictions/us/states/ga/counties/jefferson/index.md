---
type: Jurisdiction
title: "Jefferson County, GA"
classification: county
fips: "13163"
state: "GA"
demographics:
  population: 15341
  population_under_18: 3462
  population_18_64: 9014
  population_65_plus: 2865
  median_household_income: 53014
  poverty_rate: 16.93
  homeownership_rate: 68.14
  unemployment_rate: 5.82
  median_home_value: 105400
  gini_index: 0.4514
  vacancy_rate: 19.81
  race_white: 6321
  race_black: 8098
  race_asian: 6
  race_native: 72
  hispanic: 547
  bachelors_plus: 1835
districts:
  - to: "us/states/ga/districts/12"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ga/districts/senate/23"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ga/districts/house/132"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Jefferson County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 15341 |
| Under 18 | 3462 |
| 18–64 | 9014 |
| 65+ | 2865 |
| Median household income | 53014 |
| Poverty rate | 16.93 |
| Homeownership rate | 68.14 |
| Unemployment rate | 5.82 |
| Median home value | 105400 |
| Gini index | 0.4514 |
| Vacancy rate | 19.81 |
| White | 6321 |
| Black | 8098 |
| Asian | 6 |
| Native | 72 |
| Hispanic/Latino | 547 |
| Bachelor's or higher | 1835 |

## Districts

- [GA-12](/us/states/ga/districts/12.md) — 100% (congressional)
- [GA Senate District 23](/us/states/ga/districts/senate/23.md) — 100% (state senate)
- [GA House District 132](/us/states/ga/districts/house/132.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
