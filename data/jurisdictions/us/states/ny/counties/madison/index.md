---
type: Jurisdiction
title: "Madison County, NY"
classification: county
fips: "36053"
state: "NY"
demographics:
  population: 67328
  population_under_18: 12264
  population_18_64: 41381
  population_65_plus: 13683
  median_household_income: 75499
  poverty_rate: 10.01
  homeownership_rate: 78.26
  unemployment_rate: 4.25
  median_home_value: 184600
  gini_index: 0.438
  vacancy_rate: 14.57
  race_white: 60830
  race_black: 1305
  race_asian: 817
  race_native: 213
  hispanic: 1776
  bachelors_plus: 20095
districts:
  - to: "us/states/ny/districts/22"
    rel: in-district
    area_weight: 0.998
  - to: "us/states/ny/districts/senate/53"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ny/districts/house/121"
    rel: in-district
    area_weight: 0.3777
  - to: "us/states/ny/districts/house/122"
    rel: in-district
    area_weight: 0.3696
  - to: "us/states/ny/districts/house/131"
    rel: in-district
    area_weight: 0.1743
  - to: "us/states/ny/districts/house/127"
    rel: in-district
    area_weight: 0.0784
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ny]
timestamp: "2026-07-03"
---

# Madison County, NY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 67328 |
| Under 18 | 12264 |
| 18–64 | 41381 |
| 65+ | 13683 |
| Median household income | 75499 |
| Poverty rate | 10.01 |
| Homeownership rate | 78.26 |
| Unemployment rate | 4.25 |
| Median home value | 184600 |
| Gini index | 0.438 |
| Vacancy rate | 14.57 |
| White | 60830 |
| Black | 1305 |
| Asian | 817 |
| Native | 213 |
| Hispanic/Latino | 1776 |
| Bachelor's or higher | 20095 |

## Districts

- [NY-22](/us/states/ny/districts/22.md) — 100% (congressional)
- [NY Senate District 53](/us/states/ny/districts/senate/53.md) — 100% (state senate)
- [NY House District 121](/us/states/ny/districts/house/121.md) — 38% (state house)
- [NY House District 122](/us/states/ny/districts/house/122.md) — 37% (state house)
- [NY House District 131](/us/states/ny/districts/house/131.md) — 17% (state house)
- [NY House District 127](/us/states/ny/districts/house/127.md) — 8% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
