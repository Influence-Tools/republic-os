---
type: Jurisdiction
title: "Butler County, MO"
classification: county
fips: "29023"
state: "MO"
demographics:
  population: 42020
  population_under_18: 9780
  population_18_64: 24056
  population_65_plus: 8184
  median_household_income: 49089
  poverty_rate: 20.5
  homeownership_rate: 64.64
  unemployment_rate: 4.83
  median_home_value: 145100
  gini_index: 0.4612
  vacancy_rate: 14.03
  race_white: 36461
  race_black: 1978
  race_asian: 185
  race_native: 78
  hispanic: 1035
  bachelors_plus: 6131
districts:
  - to: "us/states/mo/districts/08"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/senate/25"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/house/152"
    rel: in-district
    area_weight: 0.6657
  - to: "us/states/mo/districts/house/150"
    rel: in-district
    area_weight: 0.3339
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Butler County, MO

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 42020 |
| Under 18 | 9780 |
| 18–64 | 24056 |
| 65+ | 8184 |
| Median household income | 49089 |
| Poverty rate | 20.5 |
| Homeownership rate | 64.64 |
| Unemployment rate | 4.83 |
| Median home value | 145100 |
| Gini index | 0.4612 |
| Vacancy rate | 14.03 |
| White | 36461 |
| Black | 1978 |
| Asian | 185 |
| Native | 78 |
| Hispanic/Latino | 1035 |
| Bachelor's or higher | 6131 |

## Districts

- [MO-08](/us/states/mo/districts/08.md) — 100% (congressional)
- [MO Senate District 25](/us/states/mo/districts/senate/25.md) — 100% (state senate)
- [MO House District 152](/us/states/mo/districts/house/152.md) — 67% (state house)
- [MO House District 150](/us/states/mo/districts/house/150.md) — 33% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
