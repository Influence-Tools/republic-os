---
type: Jurisdiction
title: "Portage County, WI"
classification: county
fips: "55097"
state: "WI"
demographics:
  population: 70832
  population_under_18: 13294
  population_18_64: 44548
  population_65_plus: 12990
  median_household_income: 76070
  poverty_rate: 10.09
  homeownership_rate: 69.73
  unemployment_rate: 3.2
  median_home_value: 243100
  gini_index: 0.4051
  vacancy_rate: 6.51
  race_white: 63752
  race_black: 547
  race_asian: 2039
  race_native: 112
  hispanic: 2956
  bachelors_plus: 20477
districts:
  - to: "us/states/wi/districts/03"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/wi/districts/senate/24"
    rel: in-district
    area_weight: 0.4937
  - to: "us/states/wi/districts/senate/29"
    rel: in-district
    area_weight: 0.3649
  - to: "us/states/wi/districts/senate/19"
    rel: in-district
    area_weight: 0.1414
  - to: "us/states/wi/districts/house/71"
    rel: in-district
    area_weight: 0.4937
  - to: "us/states/wi/districts/house/87"
    rel: in-district
    area_weight: 0.226
  - to: "us/states/wi/districts/house/57"
    rel: in-district
    area_weight: 0.1414
  - to: "us/states/wi/districts/house/86"
    rel: in-district
    area_weight: 0.1389
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wi]
timestamp: "2026-07-03"
---

# Portage County, WI

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 70832 |
| Under 18 | 13294 |
| 18–64 | 44548 |
| 65+ | 12990 |
| Median household income | 76070 |
| Poverty rate | 10.09 |
| Homeownership rate | 69.73 |
| Unemployment rate | 3.2 |
| Median home value | 243100 |
| Gini index | 0.4051 |
| Vacancy rate | 6.51 |
| White | 63752 |
| Black | 547 |
| Asian | 2039 |
| Native | 112 |
| Hispanic/Latino | 2956 |
| Bachelor's or higher | 20477 |

## Districts

- [WI-03](/us/states/wi/districts/03.md) — 100% (congressional)
- [WI Senate District 24](/us/states/wi/districts/senate/24.md) — 49% (state senate)
- [WI Senate District 29](/us/states/wi/districts/senate/29.md) — 36% (state senate)
- [WI Senate District 19](/us/states/wi/districts/senate/19.md) — 14% (state senate)
- [WI House District 71](/us/states/wi/districts/house/71.md) — 49% (state house)
- [WI House District 87](/us/states/wi/districts/house/87.md) — 23% (state house)
- [WI House District 57](/us/states/wi/districts/house/57.md) — 14% (state house)
- [WI House District 86](/us/states/wi/districts/house/86.md) — 14% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
