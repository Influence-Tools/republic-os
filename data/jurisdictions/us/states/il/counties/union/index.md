---
type: Jurisdiction
title: "Union County, IL"
classification: county
fips: "17181"
state: "IL"
demographics:
  population: 16997
  population_under_18: 3617
  population_18_64: 9481
  population_65_plus: 3899
  median_household_income: 55728
  poverty_rate: 20.22
  homeownership_rate: 77.45
  unemployment_rate: 3.94
  median_home_value: 131700
  gini_index: 0.4586
  vacancy_rate: 12.52
  race_white: 15210
  race_black: 161
  race_asian: 108
  race_native: 23
  hispanic: 932
  bachelors_plus: 3394
districts:
  - to: "us/states/il/districts/12"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/il/districts/house/118"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Union County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 16997 |
| Under 18 | 3617 |
| 18–64 | 9481 |
| 65+ | 3899 |
| Median household income | 55728 |
| Poverty rate | 20.22 |
| Homeownership rate | 77.45 |
| Unemployment rate | 3.94 |
| Median home value | 131700 |
| Gini index | 0.4586 |
| Vacancy rate | 12.52 |
| White | 15210 |
| Black | 161 |
| Asian | 108 |
| Native | 23 |
| Hispanic/Latino | 932 |
| Bachelor's or higher | 3394 |

## Districts

- [IL-12](/us/states/il/districts/12.md) — 100% (congressional)
- [IL House District 118](/us/states/il/districts/house/118.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
