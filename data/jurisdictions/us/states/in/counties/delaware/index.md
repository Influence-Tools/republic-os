---
type: Jurisdiction
title: "Delaware County, IN"
classification: county
fips: "18035"
state: "IN"
demographics:
  population: 112280
  population_under_18: 20376
  population_18_64: 72147
  population_65_plus: 19757
  median_household_income: 58127
  poverty_rate: 19.65
  homeownership_rate: 66.48
  unemployment_rate: 5.77
  median_home_value: 139400
  gini_index: 0.4458
  vacancy_rate: 10.42
  race_white: 95719
  race_black: 5975
  race_asian: 1956
  race_native: 172
  hispanic: 3657
  bachelors_plus: 26275
districts:
  - to: "us/states/in/districts/05"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/in/districts/senate/26"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/in/districts/house/35"
    rel: in-district
    area_weight: 0.5064
  - to: "us/states/in/districts/house/33"
    rel: in-district
    area_weight: 0.39
  - to: "us/states/in/districts/house/34"
    rel: in-district
    area_weight: 0.1035
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Delaware County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 112280 |
| Under 18 | 20376 |
| 18–64 | 72147 |
| 65+ | 19757 |
| Median household income | 58127 |
| Poverty rate | 19.65 |
| Homeownership rate | 66.48 |
| Unemployment rate | 5.77 |
| Median home value | 139400 |
| Gini index | 0.4458 |
| Vacancy rate | 10.42 |
| White | 95719 |
| Black | 5975 |
| Asian | 1956 |
| Native | 172 |
| Hispanic/Latino | 3657 |
| Bachelor's or higher | 26275 |

## Districts

- [IN-05](/us/states/in/districts/05.md) — 100% (congressional)
- [IN Senate District 26](/us/states/in/districts/senate/26.md) — 100% (state senate)
- [IN House District 35](/us/states/in/districts/house/35.md) — 51% (state house)
- [IN House District 33](/us/states/in/districts/house/33.md) — 39% (state house)
- [IN House District 34](/us/states/in/districts/house/34.md) — 10% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
