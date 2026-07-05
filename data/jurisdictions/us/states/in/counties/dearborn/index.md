---
type: Jurisdiction
title: "Dearborn County, IN"
classification: county
fips: "18029"
state: "IN"
demographics:
  population: 51094
  population_under_18: 11176
  population_18_64: 30080
  population_65_plus: 9838
  median_household_income: 84735
  poverty_rate: 7.64
  homeownership_rate: 85.23
  unemployment_rate: 1.93
  median_home_value: 243400
  gini_index: 0.4125
  vacancy_rate: 3.87
  race_white: 48314
  race_black: 139
  race_asian: 276
  race_native: 60
  hispanic: 795
  bachelors_plus: 12352
districts:
  - to: "us/states/in/districts/09"
    rel: in-district
    area_weight: 0.9992
  - to: "us/states/in/districts/senate/43"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/in/districts/house/68"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Dearborn County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 51094 |
| Under 18 | 11176 |
| 18–64 | 30080 |
| 65+ | 9838 |
| Median household income | 84735 |
| Poverty rate | 7.64 |
| Homeownership rate | 85.23 |
| Unemployment rate | 1.93 |
| Median home value | 243400 |
| Gini index | 0.4125 |
| Vacancy rate | 3.87 |
| White | 48314 |
| Black | 139 |
| Asian | 276 |
| Native | 60 |
| Hispanic/Latino | 795 |
| Bachelor's or higher | 12352 |

## Districts

- [IN-09](/us/states/in/districts/09.md) — 100% (congressional)
- [IN Senate District 43](/us/states/in/districts/senate/43.md) — 100% (state senate)
- [IN House District 68](/us/states/in/districts/house/68.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
