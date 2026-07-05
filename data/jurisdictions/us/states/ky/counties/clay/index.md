---
type: Jurisdiction
title: "Clay County, KY"
classification: county
fips: "21051"
state: "KY"
demographics:
  population: 19921
  population_under_18: 4096
  population_18_64: 12645
  population_65_plus: 3180
  median_household_income: 40900
  poverty_rate: 32.35
  homeownership_rate: 76.36
  unemployment_rate: 9.3
  median_home_value: 90700
  gini_index: 0.4715
  vacancy_rate: 15.88
  race_white: 18364
  race_black: 790
  race_asian: 38
  race_native: 14
  hispanic: 421
  bachelors_plus: 3484
districts:
  - to: "us/states/ky/districts/05"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ky/districts/senate/25"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ky/districts/house/90"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Clay County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 19921 |
| Under 18 | 4096 |
| 18–64 | 12645 |
| 65+ | 3180 |
| Median household income | 40900 |
| Poverty rate | 32.35 |
| Homeownership rate | 76.36 |
| Unemployment rate | 9.3 |
| Median home value | 90700 |
| Gini index | 0.4715 |
| Vacancy rate | 15.88 |
| White | 18364 |
| Black | 790 |
| Asian | 38 |
| Native | 14 |
| Hispanic/Latino | 421 |
| Bachelor's or higher | 3484 |

## Districts

- [KY-05](/us/states/ky/districts/05.md) — 100% (congressional)
- [KY Senate District 25](/us/states/ky/districts/senate/25.md) — 100% (state senate)
- [KY House District 90](/us/states/ky/districts/house/90.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
