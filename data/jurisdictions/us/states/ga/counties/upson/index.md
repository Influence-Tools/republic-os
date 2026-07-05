---
type: Jurisdiction
title: "Upson County, GA"
classification: county
fips: "13293"
state: "GA"
demographics:
  population: 28029
  population_under_18: 6397
  population_18_64: 16417
  population_65_plus: 5215
  median_household_income: 55429
  poverty_rate: 19.33
  homeownership_rate: 60.99
  unemployment_rate: 3.89
  median_home_value: 168700
  gini_index: 0.4951
  vacancy_rate: 14.79
  race_white: 19004
  race_black: 7228
  race_asian: 67
  race_native: 23
  hispanic: 744
  bachelors_plus: 4055
districts:
  - to: "us/states/ga/districts/03"
    rel: in-district
    area_weight: 0.9967
  - to: "us/states/ga/districts/senate/18"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ga/districts/house/134"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Upson County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 28029 |
| Under 18 | 6397 |
| 18–64 | 16417 |
| 65+ | 5215 |
| Median household income | 55429 |
| Poverty rate | 19.33 |
| Homeownership rate | 60.99 |
| Unemployment rate | 3.89 |
| Median home value | 168700 |
| Gini index | 0.4951 |
| Vacancy rate | 14.79 |
| White | 19004 |
| Black | 7228 |
| Asian | 67 |
| Native | 23 |
| Hispanic/Latino | 744 |
| Bachelor's or higher | 4055 |

## Districts

- [GA-03](/us/states/ga/districts/03.md) — 100% (congressional)
- [GA Senate District 18](/us/states/ga/districts/senate/18.md) — 100% (state senate)
- [GA House District 134](/us/states/ga/districts/house/134.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
