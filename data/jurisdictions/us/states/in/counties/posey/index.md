---
type: Jurisdiction
title: "Posey County, IN"
classification: county
fips: "18129"
state: "IN"
demographics:
  population: 25116
  population_under_18: 5418
  population_18_64: 14453
  population_65_plus: 5245
  median_household_income: 78129
  poverty_rate: 10.15
  homeownership_rate: 82.29
  unemployment_rate: 1.83
  median_home_value: 222900
  gini_index: 0.4025
  vacancy_rate: 5.15
  race_white: 23472
  race_black: 165
  race_asian: 85
  race_native: 20
  hispanic: 386
  bachelors_plus: 6188
districts:
  - to: "us/states/in/districts/08"
    rel: in-district
    area_weight: 0.9958
  - to: "us/states/in/districts/senate/49"
    rel: in-district
    area_weight: 0.9987
  - to: "us/states/in/districts/house/76"
    rel: in-district
    area_weight: 0.9987
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Posey County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 25116 |
| Under 18 | 5418 |
| 18–64 | 14453 |
| 65+ | 5245 |
| Median household income | 78129 |
| Poverty rate | 10.15 |
| Homeownership rate | 82.29 |
| Unemployment rate | 1.83 |
| Median home value | 222900 |
| Gini index | 0.4025 |
| Vacancy rate | 5.15 |
| White | 23472 |
| Black | 165 |
| Asian | 85 |
| Native | 20 |
| Hispanic/Latino | 386 |
| Bachelor's or higher | 6188 |

## Districts

- [IN-08](/us/states/in/districts/08.md) — 100% (congressional)
- [IN Senate District 49](/us/states/in/districts/senate/49.md) — 100% (state senate)
- [IN House District 76](/us/states/in/districts/house/76.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
