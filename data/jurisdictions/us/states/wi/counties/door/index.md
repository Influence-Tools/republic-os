---
type: Jurisdiction
title: "Door County, WI"
classification: county
fips: "55029"
state: "WI"
demographics:
  population: 30445
  population_under_18: 4802
  population_18_64: 15772
  population_65_plus: 9871
  median_household_income: 74795
  poverty_rate: 7.66
  homeownership_rate: 78.23
  unemployment_rate: 2.42
  median_home_value: 342600
  gini_index: 0.47
  vacancy_rate: 38.67
  race_white: 28122
  race_black: 70
  race_asian: 138
  race_native: 277
  hispanic: 1266
  bachelors_plus: 12144
districts:
  - to: "us/states/wi/districts/08"
    rel: in-district
    area_weight: 0.215
  - to: "us/states/wi/districts/senate/1"
    rel: in-district
    area_weight: 0.2058
  - to: "us/states/wi/districts/house/1"
    rel: in-district
    area_weight: 0.2058
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wi]
timestamp: "2026-07-03"
---

# Door County, WI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 30445 |
| Under 18 | 4802 |
| 18–64 | 15772 |
| 65+ | 9871 |
| Median household income | 74795 |
| Poverty rate | 7.66 |
| Homeownership rate | 78.23 |
| Unemployment rate | 2.42 |
| Median home value | 342600 |
| Gini index | 0.47 |
| Vacancy rate | 38.67 |
| White | 28122 |
| Black | 70 |
| Asian | 138 |
| Native | 277 |
| Hispanic/Latino | 1266 |
| Bachelor's or higher | 12144 |

## Districts

- [WI-08](/us/states/wi/districts/08.md) — 22% (congressional)
- [WI Senate District 1](/us/states/wi/districts/senate/1.md) — 21% (state senate)
- [WI House District 1](/us/states/wi/districts/house/1.md) — 21% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
