---
type: Jurisdiction
title: "Laurel County, KY"
classification: county
fips: "21125"
state: "KY"
demographics:
  population: 62983
  population_under_18: 14265
  population_18_64: 37939
  population_65_plus: 10779
  median_household_income: 57771
  poverty_rate: 20.46
  homeownership_rate: 71.62
  unemployment_rate: 3.5
  median_home_value: 159500
  gini_index: 0.4419
  vacancy_rate: 10.52
  race_white: 60016
  race_black: 352
  race_asian: 195
  race_native: 71
  hispanic: 1061
  bachelors_plus: 11058
districts:
  - to: "us/states/ky/districts/05"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ky/districts/senate/21"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/ky/districts/house/85"
    rel: in-district
    area_weight: 0.2496
  - to: "us/states/ky/districts/house/89"
    rel: in-district
    area_weight: 0.2018
  - to: "us/states/ky/districts/house/90"
    rel: in-district
    area_weight: 0.1793
  - to: "us/states/ky/districts/house/86"
    rel: in-district
    area_weight: 0.1502
  - to: "us/states/ky/districts/house/71"
    rel: in-district
    area_weight: 0.1343
  - to: "us/states/ky/districts/house/82"
    rel: in-district
    area_weight: 0.0848
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Laurel County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 62983 |
| Under 18 | 14265 |
| 18–64 | 37939 |
| 65+ | 10779 |
| Median household income | 57771 |
| Poverty rate | 20.46 |
| Homeownership rate | 71.62 |
| Unemployment rate | 3.5 |
| Median home value | 159500 |
| Gini index | 0.4419 |
| Vacancy rate | 10.52 |
| White | 60016 |
| Black | 352 |
| Asian | 195 |
| Native | 71 |
| Hispanic/Latino | 1061 |
| Bachelor's or higher | 11058 |

## Districts

- [KY-05](/us/states/ky/districts/05.md) — 100% (congressional)
- [KY Senate District 21](/us/states/ky/districts/senate/21.md) — 100% (state senate)
- [KY House District 85](/us/states/ky/districts/house/85.md) — 25% (state house)
- [KY House District 89](/us/states/ky/districts/house/89.md) — 20% (state house)
- [KY House District 90](/us/states/ky/districts/house/90.md) — 18% (state house)
- [KY House District 86](/us/states/ky/districts/house/86.md) — 15% (state house)
- [KY House District 71](/us/states/ky/districts/house/71.md) — 13% (state house)
- [KY House District 82](/us/states/ky/districts/house/82.md) — 8% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
