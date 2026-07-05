---
type: Jurisdiction
title: "Floyd County, IN"
classification: county
fips: "18043"
state: "IN"
demographics:
  population: 80918
  population_under_18: 18131
  population_18_64: 48504
  population_65_plus: 14283
  median_household_income: 79704
  poverty_rate: 10.35
  homeownership_rate: 73.19
  unemployment_rate: 4.13
  median_home_value: 251000
  gini_index: 0.4399
  vacancy_rate: 8.37
  race_white: 69488
  race_black: 3867
  race_asian: 1002
  race_native: 162
  hispanic: 3453
  bachelors_plus: 25333
districts:
  - to: "us/states/in/districts/09"
    rel: in-district
    area_weight: 0.9985
  - to: "us/states/in/districts/senate/47"
    rel: in-district
    area_weight: 0.9416
  - to: "us/states/in/districts/senate/45"
    rel: in-district
    area_weight: 0.0581
  - to: "us/states/in/districts/house/72"
    rel: in-district
    area_weight: 0.6559
  - to: "us/states/in/districts/house/70"
    rel: in-district
    area_weight: 0.3397
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Floyd County, IN

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 80918 |
| Under 18 | 18131 |
| 18–64 | 48504 |
| 65+ | 14283 |
| Median household income | 79704 |
| Poverty rate | 10.35 |
| Homeownership rate | 73.19 |
| Unemployment rate | 4.13 |
| Median home value | 251000 |
| Gini index | 0.4399 |
| Vacancy rate | 8.37 |
| White | 69488 |
| Black | 3867 |
| Asian | 1002 |
| Native | 162 |
| Hispanic/Latino | 3453 |
| Bachelor's or higher | 25333 |

## Districts

- [IN-09](/us/states/in/districts/09.md) — 100% (congressional)
- [IN Senate District 47](/us/states/in/districts/senate/47.md) — 94% (state senate)
- [IN Senate District 45](/us/states/in/districts/senate/45.md) — 6% (state senate)
- [IN House District 72](/us/states/in/districts/house/72.md) — 66% (state house)
- [IN House District 70](/us/states/in/districts/house/70.md) — 34% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
