---
type: Jurisdiction
title: "Grand Traverse County, MI"
classification: county
fips: "26055"
state: "MI"
demographics:
  population: 96166
  population_under_18: 18689
  population_18_64: 56368
  population_65_plus: 21109
  median_household_income: 81647
  poverty_rate: 9.63
  homeownership_rate: 77.17
  unemployment_rate: 3.81
  median_home_value: 339400
  gini_index: 0.4376
  vacancy_rate: 14.29
  race_white: 88184
  race_black: 789
  race_asian: 655
  race_native: 623
  hispanic: 3242
  bachelors_plus: 40297
districts:
  - to: "us/states/mi/districts/01"
    rel: in-district
    area_weight: 0.8153
  - to: "us/states/mi/districts/senate/37"
    rel: in-district
    area_weight: 0.8149
  - to: "us/states/mi/districts/house/104"
    rel: in-district
    area_weight: 0.5362
  - to: "us/states/mi/districts/house/103"
    rel: in-district
    area_weight: 0.2788
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Grand Traverse County, MI

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 96166 |
| Under 18 | 18689 |
| 18–64 | 56368 |
| 65+ | 21109 |
| Median household income | 81647 |
| Poverty rate | 9.63 |
| Homeownership rate | 77.17 |
| Unemployment rate | 3.81 |
| Median home value | 339400 |
| Gini index | 0.4376 |
| Vacancy rate | 14.29 |
| White | 88184 |
| Black | 789 |
| Asian | 655 |
| Native | 623 |
| Hispanic/Latino | 3242 |
| Bachelor's or higher | 40297 |

## Districts

- [MI-01](/us/states/mi/districts/01.md) — 82% (congressional)
- [MI Senate District 37](/us/states/mi/districts/senate/37.md) — 81% (state senate)
- [MI House District 104](/us/states/mi/districts/house/104.md) — 54% (state house)
- [MI House District 103](/us/states/mi/districts/house/103.md) — 28% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
