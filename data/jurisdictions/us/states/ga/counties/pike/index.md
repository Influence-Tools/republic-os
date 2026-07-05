---
type: Jurisdiction
title: "Pike County, GA"
classification: county
fips: "13231"
state: "GA"
demographics:
  population: 19903
  population_under_18: 4617
  population_18_64: 12137
  population_65_plus: 3149
  median_household_income: 86719
  poverty_rate: 9.25
  homeownership_rate: 84.65
  unemployment_rate: 3.39
  median_home_value: 305600
  gini_index: 0.4213
  vacancy_rate: 8.89
  race_white: 17437
  race_black: 1671
  race_asian: 124
  race_native: 9
  hispanic: 455
  bachelors_plus: 4040
districts:
  - to: "us/states/ga/districts/03"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ga/districts/senate/16"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/ga/districts/house/135"
    rel: in-district
    area_weight: 0.9994
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Pike County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 19903 |
| Under 18 | 4617 |
| 18–64 | 12137 |
| 65+ | 3149 |
| Median household income | 86719 |
| Poverty rate | 9.25 |
| Homeownership rate | 84.65 |
| Unemployment rate | 3.39 |
| Median home value | 305600 |
| Gini index | 0.4213 |
| Vacancy rate | 8.89 |
| White | 17437 |
| Black | 1671 |
| Asian | 124 |
| Native | 9 |
| Hispanic/Latino | 455 |
| Bachelor's or higher | 4040 |

## Districts

- [GA-03](/us/states/ga/districts/03.md) — 100% (congressional)
- [GA Senate District 16](/us/states/ga/districts/senate/16.md) — 100% (state senate)
- [GA House District 135](/us/states/ga/districts/house/135.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
