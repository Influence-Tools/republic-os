---
type: Jurisdiction
title: "Lycoming County, PA"
classification: county
fips: "42081"
state: "PA"
demographics:
  population: 113489
  population_under_18: 23296
  population_18_64: 66818
  population_65_plus: 23375
  median_household_income: 63917
  poverty_rate: 12.83
  homeownership_rate: 69.09
  unemployment_rate: 5.14
  median_home_value: 202200
  gini_index: 0.4444
  vacancy_rate: 11.1
  race_white: 100481
  race_black: 4828
  race_asian: 1077
  race_native: 235
  hispanic: 2691
  bachelors_plus: 26946
districts:
  - to: "us/states/pa/districts/15"
    rel: in-district
    area_weight: 0.722
  - to: "us/states/pa/districts/09"
    rel: in-district
    area_weight: 0.278
  - to: "us/states/pa/districts/senate/23"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/pa/districts/house/84"
    rel: in-district
    area_weight: 0.8774
  - to: "us/states/pa/districts/house/83"
    rel: in-district
    area_weight: 0.1224
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, pa]
timestamp: "2026-07-03"
---

# Lycoming County, PA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 113489 |
| Under 18 | 23296 |
| 18–64 | 66818 |
| 65+ | 23375 |
| Median household income | 63917 |
| Poverty rate | 12.83 |
| Homeownership rate | 69.09 |
| Unemployment rate | 5.14 |
| Median home value | 202200 |
| Gini index | 0.4444 |
| Vacancy rate | 11.1 |
| White | 100481 |
| Black | 4828 |
| Asian | 1077 |
| Native | 235 |
| Hispanic/Latino | 2691 |
| Bachelor's or higher | 26946 |

## Districts

- [PA-15](/us/states/pa/districts/15.md) — 72% (congressional)
- [PA-09](/us/states/pa/districts/09.md) — 28% (congressional)
- [PA Senate District 23](/us/states/pa/districts/senate/23.md) — 100% (state senate)
- [PA House District 84](/us/states/pa/districts/house/84.md) — 88% (state house)
- [PA House District 83](/us/states/pa/districts/house/83.md) — 12% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
