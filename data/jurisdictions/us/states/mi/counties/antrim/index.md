---
type: Jurisdiction
title: "Antrim County, MI"
classification: county
fips: "26009"
state: "MI"
demographics:
  population: 24127
  population_under_18: 4081
  population_18_64: 13116
  population_65_plus: 6930
  median_household_income: 72054
  poverty_rate: 9.87
  homeownership_rate: 86.37
  unemployment_rate: 3.9
  median_home_value: 255500
  gini_index: 0.4343
  vacancy_rate: 37.37
  race_white: 22399
  race_black: 149
  race_asian: 74
  race_native: 125
  hispanic: 525
  bachelors_plus: 8784
districts:
  - to: "us/states/mi/districts/01"
    rel: in-district
    area_weight: 0.8728
  - to: "us/states/mi/districts/senate/37"
    rel: in-district
    area_weight: 0.8722
  - to: "us/states/mi/districts/house/104"
    rel: in-district
    area_weight: 0.6374
  - to: "us/states/mi/districts/house/105"
    rel: in-district
    area_weight: 0.2348
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Antrim County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 24127 |
| Under 18 | 4081 |
| 18–64 | 13116 |
| 65+ | 6930 |
| Median household income | 72054 |
| Poverty rate | 9.87 |
| Homeownership rate | 86.37 |
| Unemployment rate | 3.9 |
| Median home value | 255500 |
| Gini index | 0.4343 |
| Vacancy rate | 37.37 |
| White | 22399 |
| Black | 149 |
| Asian | 74 |
| Native | 125 |
| Hispanic/Latino | 525 |
| Bachelor's or higher | 8784 |

## Districts

- [MI-01](/us/states/mi/districts/01.md) — 87% (congressional)
- [MI Senate District 37](/us/states/mi/districts/senate/37.md) — 87% (state senate)
- [MI House District 104](/us/states/mi/districts/house/104.md) — 64% (state house)
- [MI House District 105](/us/states/mi/districts/house/105.md) — 23% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
