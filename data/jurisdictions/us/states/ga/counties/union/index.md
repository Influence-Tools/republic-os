---
type: Jurisdiction
title: "Union County, GA"
classification: county
fips: "13291"
state: "GA"
demographics:
  population: 26304
  population_under_18: 3923
  population_18_64: 13394
  population_65_plus: 8987
  median_household_income: 66176
  poverty_rate: 10.89
  homeownership_rate: 84.4
  unemployment_rate: 2.64
  median_home_value: 307400
  gini_index: 0.4818
  vacancy_rate: 24.23
  race_white: 24544
  race_black: 243
  race_asian: 93
  race_native: 85
  hispanic: 1000
  bachelors_plus: 7741
districts:
  - to: "us/states/ga/districts/09"
    rel: in-district
    area_weight: 0.9957
  - to: "us/states/ga/districts/senate/51"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ga/districts/house/8"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Union County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 26304 |
| Under 18 | 3923 |
| 18–64 | 13394 |
| 65+ | 8987 |
| Median household income | 66176 |
| Poverty rate | 10.89 |
| Homeownership rate | 84.4 |
| Unemployment rate | 2.64 |
| Median home value | 307400 |
| Gini index | 0.4818 |
| Vacancy rate | 24.23 |
| White | 24544 |
| Black | 243 |
| Asian | 93 |
| Native | 85 |
| Hispanic/Latino | 1000 |
| Bachelor's or higher | 7741 |

## Districts

- [GA-09](/us/states/ga/districts/09.md) — 100% (congressional)
- [GA Senate District 51](/us/states/ga/districts/senate/51.md) — 100% (state senate)
- [GA House District 8](/us/states/ga/districts/house/8.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
