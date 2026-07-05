---
type: Jurisdiction
title: "Tuscarawas County, OH"
classification: county
fips: "39157"
state: "OH"
demographics:
  population: 92385
  population_under_18: 21454
  population_18_64: 52286
  population_65_plus: 18645
  median_household_income: 65044
  poverty_rate: 13.42
  homeownership_rate: 68.86
  unemployment_rate: 4.5
  median_home_value: 185400
  gini_index: 0.4241
  vacancy_rate: 5.92
  race_white: 86386
  race_black: 615
  race_asian: 327
  race_native: 232
  hispanic: 4306
  bachelors_plus: 16966
districts:
  - to: "us/states/oh/districts/12"
    rel: in-district
    area_weight: 0.5725
  - to: "us/states/oh/districts/06"
    rel: in-district
    area_weight: 0.4275
  - to: "us/states/oh/districts/senate/31"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/oh/districts/house/51"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, oh]
timestamp: "2026-07-03"
---

# Tuscarawas County, OH

County jurisdiction — 3 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 92385 |
| Under 18 | 21454 |
| 18–64 | 52286 |
| 65+ | 18645 |
| Median household income | 65044 |
| Poverty rate | 13.42 |
| Homeownership rate | 68.86 |
| Unemployment rate | 4.5 |
| Median home value | 185400 |
| Gini index | 0.4241 |
| Vacancy rate | 5.92 |
| White | 86386 |
| Black | 615 |
| Asian | 327 |
| Native | 232 |
| Hispanic/Latino | 4306 |
| Bachelor's or higher | 16966 |

## Districts

- [OH-12](/us/states/oh/districts/12.md) — 57% (congressional)
- [OH-06](/us/states/oh/districts/06.md) — 43% (congressional)
- [OH Senate District 31](/us/states/oh/districts/senate/31.md) — 100% (state senate)
- [OH House District 51](/us/states/oh/districts/house/51.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
