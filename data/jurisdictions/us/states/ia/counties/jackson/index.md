---
type: Jurisdiction
title: "Jackson County, IA"
classification: county
fips: "19097"
state: "IA"
demographics:
  population: 19390
  population_under_18: 4303
  population_18_64: 10783
  population_65_plus: 4304
  median_household_income: 74186
  poverty_rate: 9.65
  homeownership_rate: 80.72
  unemployment_rate: 5.1
  median_home_value: 175000
  gini_index: 0.4463
  vacancy_rate: 11.2
  race_white: 18420
  race_black: 189
  race_asian: 22
  race_native: 13
  hispanic: 306
  bachelors_plus: 3391
districts:
  - to: "us/states/ia/districts/01"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/ia/districts/senate/33"
    rel: in-district
    area_weight: 0.8329
  - to: "us/states/ia/districts/senate/35"
    rel: in-district
    area_weight: 0.1669
  - to: "us/states/ia/districts/house/66"
    rel: in-district
    area_weight: 0.8329
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Jackson County, IA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 19390 |
| Under 18 | 4303 |
| 18–64 | 10783 |
| 65+ | 4304 |
| Median household income | 74186 |
| Poverty rate | 9.65 |
| Homeownership rate | 80.72 |
| Unemployment rate | 5.1 |
| Median home value | 175000 |
| Gini index | 0.4463 |
| Vacancy rate | 11.2 |
| White | 18420 |
| Black | 189 |
| Asian | 22 |
| Native | 13 |
| Hispanic/Latino | 306 |
| Bachelor's or higher | 3391 |

## Districts

- [IA-01](/us/states/ia/districts/01.md) — 100% (congressional)
- [IA Senate District 33](/us/states/ia/districts/senate/33.md) — 83% (state senate)
- [IA Senate District 35](/us/states/ia/districts/senate/35.md) — 17% (state senate)
- [IA House District 66](/us/states/ia/districts/house/66.md) — 83% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
