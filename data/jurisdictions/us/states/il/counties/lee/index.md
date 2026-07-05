---
type: Jurisdiction
title: "Lee County, IL"
classification: county
fips: "17103"
state: "IL"
demographics:
  population: 33869
  population_under_18: 6655
  population_18_64: 19987
  population_65_plus: 7227
  median_household_income: 70292
  poverty_rate: 11.82
  homeownership_rate: 73.64
  unemployment_rate: 5.21
  median_home_value: 154600
  gini_index: 0.4348
  vacancy_rate: 11.06
  race_white: 29059
  race_black: 1798
  race_asian: 243
  race_native: 37
  hispanic: 2564
  bachelors_plus: 6562
districts:
  - to: "us/states/il/districts/16"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/il/districts/senate/37"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/il/districts/house/74"
    rel: in-district
    area_weight: 0.8033
  - to: "us/states/il/districts/house/73"
    rel: in-district
    area_weight: 0.1967
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Lee County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 33869 |
| Under 18 | 6655 |
| 18–64 | 19987 |
| 65+ | 7227 |
| Median household income | 70292 |
| Poverty rate | 11.82 |
| Homeownership rate | 73.64 |
| Unemployment rate | 5.21 |
| Median home value | 154600 |
| Gini index | 0.4348 |
| Vacancy rate | 11.06 |
| White | 29059 |
| Black | 1798 |
| Asian | 243 |
| Native | 37 |
| Hispanic/Latino | 2564 |
| Bachelor's or higher | 6562 |

## Districts

- [IL-16](/us/states/il/districts/16.md) — 100% (congressional)
- [IL Senate District 37](/us/states/il/districts/senate/37.md) — 100% (state senate)
- [IL House District 74](/us/states/il/districts/house/74.md) — 80% (state house)
- [IL House District 73](/us/states/il/districts/house/73.md) — 20% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
