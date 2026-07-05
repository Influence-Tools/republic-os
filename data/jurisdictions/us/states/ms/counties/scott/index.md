---
type: Jurisdiction
title: "Scott County, MS"
classification: county
fips: "28123"
state: "MS"
demographics:
  population: 27718
  population_under_18: 7803
  population_18_64: 15520
  population_65_plus: 4395
  median_household_income: 48786
  poverty_rate: 22.16
  homeownership_rate: 71.33
  unemployment_rate: 5.49
  median_home_value: 106700
  gini_index: 0.4641
  vacancy_rate: 15.65
  race_white: 13095
  race_black: 9375
  race_asian: 39
  race_native: 0
  hispanic: 4293
  bachelors_plus: 3265
districts:
  - to: "us/states/ms/districts/03"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ms/districts/senate/31"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ms/districts/house/78"
    rel: in-district
    area_weight: 0.3624
  - to: "us/states/ms/districts/house/75"
    rel: in-district
    area_weight: 0.2772
  - to: "us/states/ms/districts/house/79"
    rel: in-district
    area_weight: 0.207
  - to: "us/states/ms/districts/house/27"
    rel: in-district
    area_weight: 0.1534
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Scott County, MS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 27718 |
| Under 18 | 7803 |
| 18–64 | 15520 |
| 65+ | 4395 |
| Median household income | 48786 |
| Poverty rate | 22.16 |
| Homeownership rate | 71.33 |
| Unemployment rate | 5.49 |
| Median home value | 106700 |
| Gini index | 0.4641 |
| Vacancy rate | 15.65 |
| White | 13095 |
| Black | 9375 |
| Asian | 39 |
| Native | 0 |
| Hispanic/Latino | 4293 |
| Bachelor's or higher | 3265 |

## Districts

- [MS-03](/us/states/ms/districts/03.md) — 100% (congressional)
- [MS Senate District 31](/us/states/ms/districts/senate/31.md) — 100% (state senate)
- [MS House District 78](/us/states/ms/districts/house/78.md) — 36% (state house)
- [MS House District 75](/us/states/ms/districts/house/75.md) — 28% (state house)
- [MS House District 79](/us/states/ms/districts/house/79.md) — 21% (state house)
- [MS House District 27](/us/states/ms/districts/house/27.md) — 15% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
