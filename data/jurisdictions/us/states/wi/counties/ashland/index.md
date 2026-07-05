---
type: Jurisdiction
title: "Ashland County, WI"
classification: county
fips: "55003"
state: "WI"
demographics:
  population: 16080
  population_under_18: 3331
  population_18_64: 9297
  population_65_plus: 3452
  median_household_income: 62462
  poverty_rate: 13.38
  homeownership_rate: 73.43
  unemployment_rate: 3.77
  median_home_value: 170300
  gini_index: 0.4269
  vacancy_rate: 27.67
  race_white: 13326
  race_black: 83
  race_asian: 119
  race_native: 1532
  hispanic: 476
  bachelors_plus: 3697
districts:
  - to: "us/states/wi/districts/07"
    rel: in-district
    area_weight: 0.4586
  - to: "us/states/wi/districts/senate/25"
    rel: in-district
    area_weight: 0.4567
  - to: "us/states/wi/districts/house/74"
    rel: in-district
    area_weight: 0.331
  - to: "us/states/wi/districts/house/73"
    rel: in-district
    area_weight: 0.1257
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wi]
timestamp: "2026-07-03"
---

# Ashland County, WI

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 16080 |
| Under 18 | 3331 |
| 18–64 | 9297 |
| 65+ | 3452 |
| Median household income | 62462 |
| Poverty rate | 13.38 |
| Homeownership rate | 73.43 |
| Unemployment rate | 3.77 |
| Median home value | 170300 |
| Gini index | 0.4269 |
| Vacancy rate | 27.67 |
| White | 13326 |
| Black | 83 |
| Asian | 119 |
| Native | 1532 |
| Hispanic/Latino | 476 |
| Bachelor's or higher | 3697 |

## Districts

- [WI-07](/us/states/wi/districts/07.md) — 46% (congressional)
- [WI Senate District 25](/us/states/wi/districts/senate/25.md) — 46% (state senate)
- [WI House District 74](/us/states/wi/districts/house/74.md) — 33% (state house)
- [WI House District 73](/us/states/wi/districts/house/73.md) — 13% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
