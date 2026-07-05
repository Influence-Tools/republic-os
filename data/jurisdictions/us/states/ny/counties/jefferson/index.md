---
type: Jurisdiction
title: "Jefferson County, NY"
classification: county
fips: "36045"
state: "NY"
demographics:
  population: 115040
  population_under_18: 27653
  population_18_64: 70006
  population_65_plus: 17381
  median_household_income: 66301
  poverty_rate: 13.68
  homeownership_rate: 54.65
  unemployment_rate: 5.88
  median_home_value: 188200
  gini_index: 0.4394
  vacancy_rate: 23.04
  race_white: 94857
  race_black: 5521
  race_asian: 2189
  race_native: 432
  hispanic: 8657
  bachelors_plus: 27819
districts:
  - to: "us/states/ny/districts/24"
    rel: in-district
    area_weight: 0.5954
  - to: "us/states/ny/districts/21"
    rel: in-district
    area_weight: 0.1506
  - to: "us/states/ny/districts/senate/49"
    rel: in-district
    area_weight: 0.7232
  - to: "us/states/ny/districts/house/116"
    rel: in-district
    area_weight: 0.4559
  - to: "us/states/ny/districts/house/117"
    rel: in-district
    area_weight: 0.1538
  - to: "us/states/ny/districts/house/120"
    rel: in-district
    area_weight: 0.1135
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ny]
timestamp: "2026-07-03"
---

# Jefferson County, NY

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 115040 |
| Under 18 | 27653 |
| 18–64 | 70006 |
| 65+ | 17381 |
| Median household income | 66301 |
| Poverty rate | 13.68 |
| Homeownership rate | 54.65 |
| Unemployment rate | 5.88 |
| Median home value | 188200 |
| Gini index | 0.4394 |
| Vacancy rate | 23.04 |
| White | 94857 |
| Black | 5521 |
| Asian | 2189 |
| Native | 432 |
| Hispanic/Latino | 8657 |
| Bachelor's or higher | 27819 |

## Districts

- [NY-24](/us/states/ny/districts/24.md) — 60% (congressional)
- [NY-21](/us/states/ny/districts/21.md) — 15% (congressional)
- [NY Senate District 49](/us/states/ny/districts/senate/49.md) — 72% (state senate)
- [NY House District 116](/us/states/ny/districts/house/116.md) — 46% (state house)
- [NY House District 117](/us/states/ny/districts/house/117.md) — 15% (state house)
- [NY House District 120](/us/states/ny/districts/house/120.md) — 11% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
