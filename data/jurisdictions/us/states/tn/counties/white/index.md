---
type: Jurisdiction
title: "White County, TN"
classification: county
fips: "47185"
state: "TN"
demographics:
  population: 28160
  population_under_18: 6096
  population_18_64: 16085
  population_65_plus: 5979
  median_household_income: 52188
  poverty_rate: 13.17
  homeownership_rate: 76.88
  unemployment_rate: 5.57
  median_home_value: 207200
  gini_index: 0.4318
  vacancy_rate: 8.99
  race_white: 26076
  race_black: 287
  race_asian: 124
  race_native: 130
  hispanic: 909
  bachelors_plus: 4133
districts:
  - to: "us/states/tn/districts/06"
    rel: in-district
    area_weight: 0.9987
  - to: "us/states/tn/districts/senate/15"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tn/districts/house/43"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# White County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 28160 |
| Under 18 | 6096 |
| 18–64 | 16085 |
| 65+ | 5979 |
| Median household income | 52188 |
| Poverty rate | 13.17 |
| Homeownership rate | 76.88 |
| Unemployment rate | 5.57 |
| Median home value | 207200 |
| Gini index | 0.4318 |
| Vacancy rate | 8.99 |
| White | 26076 |
| Black | 287 |
| Asian | 124 |
| Native | 130 |
| Hispanic/Latino | 909 |
| Bachelor's or higher | 4133 |

## Districts

- [TN-06](/us/states/tn/districts/06.md) — 100% (congressional)
- [TN Senate District 15](/us/states/tn/districts/senate/15.md) — 100% (state senate)
- [TN House District 43](/us/states/tn/districts/house/43.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
