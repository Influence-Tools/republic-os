---
type: Jurisdiction
title: "Ingham County, MI"
classification: county
fips: "26065"
state: "MI"
demographics:
  population: 283913
  population_under_18: 55759
  population_18_64: 185944
  population_65_plus: 42210
  median_household_income: 65526
  poverty_rate: 16.69
  homeownership_rate: 59.46
  unemployment_rate: 6.24
  median_home_value: 198800
  gini_index: 0.4726
  vacancy_rate: 7.24
  race_white: 194933
  race_black: 32386
  race_asian: 17807
  race_native: 1542
  hispanic: 24806
  bachelors_plus: 104349
districts:
  - to: "us/states/mi/districts/07"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mi/districts/senate/21"
    rel: in-district
    area_weight: 0.5474
  - to: "us/states/mi/districts/senate/28"
    rel: in-district
    area_weight: 0.2626
  - to: "us/states/mi/districts/senate/22"
    rel: in-district
    area_weight: 0.19
  - to: "us/states/mi/districts/house/73"
    rel: in-district
    area_weight: 0.7891
  - to: "us/states/mi/districts/house/75"
    rel: in-district
    area_weight: 0.0931
  - to: "us/states/mi/districts/house/74"
    rel: in-district
    area_weight: 0.0873
  - to: "us/states/mi/districts/house/77"
    rel: in-district
    area_weight: 0.0304
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Ingham County, MI

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 283913 |
| Under 18 | 55759 |
| 18–64 | 185944 |
| 65+ | 42210 |
| Median household income | 65526 |
| Poverty rate | 16.69 |
| Homeownership rate | 59.46 |
| Unemployment rate | 6.24 |
| Median home value | 198800 |
| Gini index | 0.4726 |
| Vacancy rate | 7.24 |
| White | 194933 |
| Black | 32386 |
| Asian | 17807 |
| Native | 1542 |
| Hispanic/Latino | 24806 |
| Bachelor's or higher | 104349 |

## Districts

- [MI-07](/us/states/mi/districts/07.md) — 100% (congressional)
- [MI Senate District 21](/us/states/mi/districts/senate/21.md) — 55% (state senate)
- [MI Senate District 28](/us/states/mi/districts/senate/28.md) — 26% (state senate)
- [MI Senate District 22](/us/states/mi/districts/senate/22.md) — 19% (state senate)
- [MI House District 73](/us/states/mi/districts/house/73.md) — 79% (state house)
- [MI House District 75](/us/states/mi/districts/house/75.md) — 9% (state house)
- [MI House District 74](/us/states/mi/districts/house/74.md) — 9% (state house)
- [MI House District 77](/us/states/mi/districts/house/77.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
