---
type: Jurisdiction
title: "Grady County, OK"
classification: county
fips: "40051"
state: "OK"
demographics:
  population: 56606
  population_under_18: 13144
  population_18_64: 33857
  population_65_plus: 9605
  median_household_income: 75419
  poverty_rate: 12.18
  homeownership_rate: 75.0
  unemployment_rate: 5.47
  median_home_value: 205800
  gini_index: 0.4196
  vacancy_rate: 12.07
  race_white: 45420
  race_black: 1065
  race_asian: 277
  race_native: 2096
  hispanic: 4037
  bachelors_plus: 11448
districts:
  - to: "us/states/ok/districts/04"
    rel: in-district
    area_weight: 0.9984
  - to: "us/states/ok/districts/senate/23"
    rel: in-district
    area_weight: 0.5413
  - to: "us/states/ok/districts/senate/43"
    rel: in-district
    area_weight: 0.4587
  - to: "us/states/ok/districts/house/51"
    rel: in-district
    area_weight: 0.6641
  - to: "us/states/ok/districts/house/56"
    rel: in-district
    area_weight: 0.3358
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Grady County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 56606 |
| Under 18 | 13144 |
| 18–64 | 33857 |
| 65+ | 9605 |
| Median household income | 75419 |
| Poverty rate | 12.18 |
| Homeownership rate | 75.0 |
| Unemployment rate | 5.47 |
| Median home value | 205800 |
| Gini index | 0.4196 |
| Vacancy rate | 12.07 |
| White | 45420 |
| Black | 1065 |
| Asian | 277 |
| Native | 2096 |
| Hispanic/Latino | 4037 |
| Bachelor's or higher | 11448 |

## Districts

- [OK-04](/us/states/ok/districts/04.md) — 100% (congressional)
- [OK Senate District 23](/us/states/ok/districts/senate/23.md) — 54% (state senate)
- [OK Senate District 43](/us/states/ok/districts/senate/43.md) — 46% (state senate)
- [OK House District 51](/us/states/ok/districts/house/51.md) — 66% (state house)
- [OK House District 56](/us/states/ok/districts/house/56.md) — 34% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
