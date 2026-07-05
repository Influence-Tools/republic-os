---
type: Jurisdiction
title: "York County, SC"
classification: county
fips: "45091"
state: "SC"
demographics:
  population: 293673
  population_under_18: 69346
  population_18_64: 179194
  population_65_plus: 45133
  median_household_income: 89095
  poverty_rate: 8.37
  homeownership_rate: 74.53
  unemployment_rate: 4.15
  median_home_value: 361300
  gini_index: 0.4331
  vacancy_rate: 5.69
  race_white: 200002
  race_black: 54027
  race_asian: 8875
  race_native: 1587
  hispanic: 21772
  bachelors_plus: 108530
districts:
  - to: "us/states/sc/districts/05"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/sc/districts/senate/15"
    rel: in-district
    area_weight: 0.4294
  - to: "us/states/sc/districts/senate/14"
    rel: in-district
    area_weight: 0.324
  - to: "us/states/sc/districts/senate/17"
    rel: in-district
    area_weight: 0.1656
  - to: "us/states/sc/districts/senate/16"
    rel: in-district
    area_weight: 0.0805
  - to: "us/states/sc/districts/house/29"
    rel: in-district
    area_weight: 0.3325
  - to: "us/states/sc/districts/house/47"
    rel: in-district
    area_weight: 0.2621
  - to: "us/states/sc/districts/house/43"
    rel: in-district
    area_weight: 0.1017
  - to: "us/states/sc/districts/house/49"
    rel: in-district
    area_weight: 0.1012
  - to: "us/states/sc/districts/house/48"
    rel: in-district
    area_weight: 0.0726
  - to: "us/states/sc/districts/house/26"
    rel: in-district
    area_weight: 0.0506
  - to: "us/states/sc/districts/house/46"
    rel: in-district
    area_weight: 0.049
  - to: "us/states/sc/districts/house/66"
    rel: in-district
    area_weight: 0.0298
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sc]
timestamp: "2026-07-03"
---

# York County, SC

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 293673 |
| Under 18 | 69346 |
| 18–64 | 179194 |
| 65+ | 45133 |
| Median household income | 89095 |
| Poverty rate | 8.37 |
| Homeownership rate | 74.53 |
| Unemployment rate | 4.15 |
| Median home value | 361300 |
| Gini index | 0.4331 |
| Vacancy rate | 5.69 |
| White | 200002 |
| Black | 54027 |
| Asian | 8875 |
| Native | 1587 |
| Hispanic/Latino | 21772 |
| Bachelor's or higher | 108530 |

## Districts

- [SC-05](/us/states/sc/districts/05.md) — 100% (congressional)
- [SC Senate District 15](/us/states/sc/districts/senate/15.md) — 43% (state senate)
- [SC Senate District 14](/us/states/sc/districts/senate/14.md) — 32% (state senate)
- [SC Senate District 17](/us/states/sc/districts/senate/17.md) — 17% (state senate)
- [SC Senate District 16](/us/states/sc/districts/senate/16.md) — 8% (state senate)
- [SC House District 29](/us/states/sc/districts/house/29.md) — 33% (state house)
- [SC House District 47](/us/states/sc/districts/house/47.md) — 26% (state house)
- [SC House District 43](/us/states/sc/districts/house/43.md) — 10% (state house)
- [SC House District 49](/us/states/sc/districts/house/49.md) — 10% (state house)
- [SC House District 48](/us/states/sc/districts/house/48.md) — 7% (state house)
- [SC House District 26](/us/states/sc/districts/house/26.md) — 5% (state house)
- [SC House District 46](/us/states/sc/districts/house/46.md) — 5% (state house)
- [SC House District 66](/us/states/sc/districts/house/66.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
