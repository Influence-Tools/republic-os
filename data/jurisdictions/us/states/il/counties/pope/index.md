---
type: Jurisdiction
title: "Pope County, IL"
classification: county
fips: "17151"
state: "IL"
demographics:
  population: 3739
  population_under_18: 539
  population_18_64: 2116
  population_65_plus: 1084
  median_household_income: 60050
  poverty_rate: 13.31
  homeownership_rate: 86.28
  unemployment_rate: 2.79
  median_home_value: 143800
  gini_index: 0.4318
  vacancy_rate: 37.75
  race_white: 3323
  race_black: 179
  race_asian: 1
  race_native: 78
  hispanic: 111
  bachelors_plus: 591
districts:
  - to: "us/states/il/districts/12"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/il/districts/house/117"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Pope County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3739 |
| Under 18 | 539 |
| 18–64 | 2116 |
| 65+ | 1084 |
| Median household income | 60050 |
| Poverty rate | 13.31 |
| Homeownership rate | 86.28 |
| Unemployment rate | 2.79 |
| Median home value | 143800 |
| Gini index | 0.4318 |
| Vacancy rate | 37.75 |
| White | 3323 |
| Black | 179 |
| Asian | 1 |
| Native | 78 |
| Hispanic/Latino | 111 |
| Bachelor's or higher | 591 |

## Districts

- [IL-12](/us/states/il/districts/12.md) — 100% (congressional)
- [IL House District 117](/us/states/il/districts/house/117.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
