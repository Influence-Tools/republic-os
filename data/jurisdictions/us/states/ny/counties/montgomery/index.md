---
type: Jurisdiction
title: "Montgomery County, NY"
classification: county
fips: "36057"
state: "NY"
demographics:
  population: 49528
  population_under_18: 11454
  population_18_64: 28448
  population_65_plus: 9626
  median_household_income: 64943
  poverty_rate: 14.58
  homeownership_rate: 70.39
  unemployment_rate: 4.73
  median_home_value: 157500
  gini_index: 0.4267
  vacancy_rate: 14.7
  race_white: 39937
  race_black: 1546
  race_asian: 424
  race_native: 112
  hispanic: 7632
  bachelors_plus: 10978
districts:
  - to: "us/states/ny/districts/21"
    rel: in-district
    area_weight: 0.7869
  - to: "us/states/ny/districts/20"
    rel: in-district
    area_weight: 0.213
  - to: "us/states/ny/districts/senate/46"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ny/districts/house/118"
    rel: in-district
    area_weight: 0.7853
  - to: "us/states/ny/districts/house/111"
    rel: in-district
    area_weight: 0.2146
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ny]
timestamp: "2026-07-03"
---

# Montgomery County, NY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 49528 |
| Under 18 | 11454 |
| 18–64 | 28448 |
| 65+ | 9626 |
| Median household income | 64943 |
| Poverty rate | 14.58 |
| Homeownership rate | 70.39 |
| Unemployment rate | 4.73 |
| Median home value | 157500 |
| Gini index | 0.4267 |
| Vacancy rate | 14.7 |
| White | 39937 |
| Black | 1546 |
| Asian | 424 |
| Native | 112 |
| Hispanic/Latino | 7632 |
| Bachelor's or higher | 10978 |

## Districts

- [NY-21](/us/states/ny/districts/21.md) — 79% (congressional)
- [NY-20](/us/states/ny/districts/20.md) — 21% (congressional)
- [NY Senate District 46](/us/states/ny/districts/senate/46.md) — 100% (state senate)
- [NY House District 118](/us/states/ny/districts/house/118.md) — 79% (state house)
- [NY House District 111](/us/states/ny/districts/house/111.md) — 21% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
