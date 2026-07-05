---
type: Jurisdiction
title: "Cameron Parish, LA"
classification: county
fips: "22023"
state: "LA"
demographics:
  population: 5015
  population_under_18: 1220
  population_18_64: 2818
  population_65_plus: 977
  median_household_income: 75278
  poverty_rate: 7.44
  homeownership_rate: 95.39
  unemployment_rate: 2.06
  median_home_value: 202500
  gini_index: 0.3921
  vacancy_rate: 41.73
  race_white: 4304
  race_black: 166
  race_asian: 0
  race_native: 79
  hispanic: 26
  bachelors_plus: 789
districts:
  - to: "us/states/la/districts/03"
    rel: in-district
    area_weight: 0.847
  - to: "us/states/la/districts/senate/25"
    rel: in-district
    area_weight: 0.8467
  - to: "us/states/la/districts/house/47"
    rel: in-district
    area_weight: 0.8467
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, la]
timestamp: "2026-07-03"
---

# Cameron Parish, LA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5015 |
| Under 18 | 1220 |
| 18–64 | 2818 |
| 65+ | 977 |
| Median household income | 75278 |
| Poverty rate | 7.44 |
| Homeownership rate | 95.39 |
| Unemployment rate | 2.06 |
| Median home value | 202500 |
| Gini index | 0.3921 |
| Vacancy rate | 41.73 |
| White | 4304 |
| Black | 166 |
| Asian | 0 |
| Native | 79 |
| Hispanic/Latino | 26 |
| Bachelor's or higher | 789 |

## Districts

- [LA-03](/us/states/la/districts/03.md) — 85% (congressional)
- [LA Senate District 25](/us/states/la/districts/senate/25.md) — 85% (state senate)
- [LA House District 47](/us/states/la/districts/house/47.md) — 85% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
