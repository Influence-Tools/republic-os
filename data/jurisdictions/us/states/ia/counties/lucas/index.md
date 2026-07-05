---
type: Jurisdiction
title: "Lucas County, IA"
classification: county
fips: "19117"
state: "IA"
demographics:
  population: 8716
  population_under_18: 2049
  population_18_64: 4750
  population_65_plus: 1917
  median_household_income: 61793
  poverty_rate: 14.95
  homeownership_rate: 78.78
  unemployment_rate: 5.16
  median_home_value: 120200
  gini_index: 0.4331
  vacancy_rate: 8.98
  race_white: 8215
  race_black: 25
  race_asian: 73
  race_native: 1
  hispanic: 255
  bachelors_plus: 1285
districts:
  - to: "us/states/ia/districts/03"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ia/districts/senate/12"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ia/districts/house/24"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Lucas County, IA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8716 |
| Under 18 | 2049 |
| 18–64 | 4750 |
| 65+ | 1917 |
| Median household income | 61793 |
| Poverty rate | 14.95 |
| Homeownership rate | 78.78 |
| Unemployment rate | 5.16 |
| Median home value | 120200 |
| Gini index | 0.4331 |
| Vacancy rate | 8.98 |
| White | 8215 |
| Black | 25 |
| Asian | 73 |
| Native | 1 |
| Hispanic/Latino | 255 |
| Bachelor's or higher | 1285 |

## Districts

- [IA-03](/us/states/ia/districts/03.md) — 100% (congressional)
- [IA Senate District 12](/us/states/ia/districts/senate/12.md) — 100% (state senate)
- [IA House District 24](/us/states/ia/districts/house/24.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
