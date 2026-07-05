---
type: Jurisdiction
title: "Washtenaw County, MI"
classification: county
fips: "26161"
state: "MI"
demographics:
  population: 369822
  population_under_18: 67474
  population_18_64: 244106
  population_65_plus: 58242
  median_household_income: 89180
  poverty_rate: 14.17
  homeownership_rate: 61.62
  unemployment_rate: 4.59
  median_home_value: 374100
  gini_index: 0.4871
  vacancy_rate: 5.78
  race_white: 253992
  race_black: 42421
  race_asian: 34148
  race_native: 1007
  hispanic: 21403
  bachelors_plus: 214008
districts:
  - to: "us/states/mi/districts/06"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mi/districts/senate/14"
    rel: in-district
    area_weight: 0.538
  - to: "us/states/mi/districts/senate/15"
    rel: in-district
    area_weight: 0.4619
  - to: "us/states/mi/districts/house/47"
    rel: in-district
    area_weight: 0.2596
  - to: "us/states/mi/districts/house/48"
    rel: in-district
    area_weight: 0.2181
  - to: "us/states/mi/districts/house/33"
    rel: in-district
    area_weight: 0.2085
  - to: "us/states/mi/districts/house/23"
    rel: in-district
    area_weight: 0.1104
  - to: "us/states/mi/districts/house/31"
    rel: in-district
    area_weight: 0.0897
  - to: "us/states/mi/districts/house/32"
    rel: in-district
    area_weight: 0.0613
  - to: "us/states/mi/districts/house/46"
    rel: in-district
    area_weight: 0.0524
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Washtenaw County, MI

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 369822 |
| Under 18 | 67474 |
| 18–64 | 244106 |
| 65+ | 58242 |
| Median household income | 89180 |
| Poverty rate | 14.17 |
| Homeownership rate | 61.62 |
| Unemployment rate | 4.59 |
| Median home value | 374100 |
| Gini index | 0.4871 |
| Vacancy rate | 5.78 |
| White | 253992 |
| Black | 42421 |
| Asian | 34148 |
| Native | 1007 |
| Hispanic/Latino | 21403 |
| Bachelor's or higher | 214008 |

## Districts

- [MI-06](/us/states/mi/districts/06.md) — 100% (congressional)
- [MI Senate District 14](/us/states/mi/districts/senate/14.md) — 54% (state senate)
- [MI Senate District 15](/us/states/mi/districts/senate/15.md) — 46% (state senate)
- [MI House District 47](/us/states/mi/districts/house/47.md) — 26% (state house)
- [MI House District 48](/us/states/mi/districts/house/48.md) — 22% (state house)
- [MI House District 33](/us/states/mi/districts/house/33.md) — 21% (state house)
- [MI House District 23](/us/states/mi/districts/house/23.md) — 11% (state house)
- [MI House District 31](/us/states/mi/districts/house/31.md) — 9% (state house)
- [MI House District 32](/us/states/mi/districts/house/32.md) — 6% (state house)
- [MI House District 46](/us/states/mi/districts/house/46.md) — 5% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
