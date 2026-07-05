---
type: Jurisdiction
title: "Scott County, IN"
classification: county
fips: "18143"
state: "IN"
demographics:
  population: 24526
  population_under_18: 5702
  population_18_64: 14637
  population_65_plus: 4187
  median_household_income: 56352
  poverty_rate: 16.56
  homeownership_rate: 70.92
  unemployment_rate: 3.3
  median_home_value: 158400
  gini_index: 0.4319
  vacancy_rate: 9.15
  race_white: 23142
  race_black: 118
  race_asian: 0
  race_native: 2
  hispanic: 644
  bachelors_plus: 2957
districts:
  - to: "us/states/in/districts/09"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/in/districts/senate/43"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/in/districts/house/69"
    rel: in-district
    area_weight: 0.5304
  - to: "us/states/in/districts/house/66"
    rel: in-district
    area_weight: 0.4693
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Scott County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 24526 |
| Under 18 | 5702 |
| 18–64 | 14637 |
| 65+ | 4187 |
| Median household income | 56352 |
| Poverty rate | 16.56 |
| Homeownership rate | 70.92 |
| Unemployment rate | 3.3 |
| Median home value | 158400 |
| Gini index | 0.4319 |
| Vacancy rate | 9.15 |
| White | 23142 |
| Black | 118 |
| Asian | 0 |
| Native | 2 |
| Hispanic/Latino | 644 |
| Bachelor's or higher | 2957 |

## Districts

- [IN-09](/us/states/in/districts/09.md) — 100% (congressional)
- [IN Senate District 43](/us/states/in/districts/senate/43.md) — 100% (state senate)
- [IN House District 69](/us/states/in/districts/house/69.md) — 53% (state house)
- [IN House District 66](/us/states/in/districts/house/66.md) — 47% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
