---
type: Jurisdiction
title: "Kershaw County, SC"
classification: county
fips: "45055"
state: "SC"
demographics:
  population: 68314
  population_under_18: 15860
  population_18_64: 39530
  population_65_plus: 12924
  median_household_income: 68231
  poverty_rate: 13.16
  homeownership_rate: 82.04
  unemployment_rate: 4.75
  median_home_value: 217100
  gini_index: 0.4537
  vacancy_rate: 10.74
  race_white: 45586
  race_black: 16215
  race_asian: 474
  race_native: 334
  hispanic: 4057
  bachelors_plus: 15665
districts:
  - to: "us/states/sc/districts/05"
    rel: in-district
    area_weight: 0.999
  - to: "us/states/sc/districts/senate/27"
    rel: in-district
    area_weight: 0.5589
  - to: "us/states/sc/districts/senate/35"
    rel: in-district
    area_weight: 0.441
  - to: "us/states/sc/districts/house/65"
    rel: in-district
    area_weight: 0.3205
  - to: "us/states/sc/districts/house/45"
    rel: in-district
    area_weight: 0.223
  - to: "us/states/sc/districts/house/50"
    rel: in-district
    area_weight: 0.2211
  - to: "us/states/sc/districts/house/70"
    rel: in-district
    area_weight: 0.1473
  - to: "us/states/sc/districts/house/52"
    rel: in-district
    area_weight: 0.0881
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sc]
timestamp: "2026-07-03"
---

# Kershaw County, SC

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 68314 |
| Under 18 | 15860 |
| 18–64 | 39530 |
| 65+ | 12924 |
| Median household income | 68231 |
| Poverty rate | 13.16 |
| Homeownership rate | 82.04 |
| Unemployment rate | 4.75 |
| Median home value | 217100 |
| Gini index | 0.4537 |
| Vacancy rate | 10.74 |
| White | 45586 |
| Black | 16215 |
| Asian | 474 |
| Native | 334 |
| Hispanic/Latino | 4057 |
| Bachelor's or higher | 15665 |

## Districts

- [SC-05](/us/states/sc/districts/05.md) — 100% (congressional)
- [SC Senate District 27](/us/states/sc/districts/senate/27.md) — 56% (state senate)
- [SC Senate District 35](/us/states/sc/districts/senate/35.md) — 44% (state senate)
- [SC House District 65](/us/states/sc/districts/house/65.md) — 32% (state house)
- [SC House District 45](/us/states/sc/districts/house/45.md) — 22% (state house)
- [SC House District 50](/us/states/sc/districts/house/50.md) — 22% (state house)
- [SC House District 70](/us/states/sc/districts/house/70.md) — 15% (state house)
- [SC House District 52](/us/states/sc/districts/house/52.md) — 9% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
