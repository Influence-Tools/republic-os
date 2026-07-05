---
type: Jurisdiction
title: "Bucks County, PA"
classification: county
fips: "42017"
state: "PA"
demographics:
  population: 647461
  population_under_18: 128990
  population_18_64: 385485
  population_65_plus: 132986
  median_household_income: 114764
  poverty_rate: 6.1
  homeownership_rate: 77.8
  unemployment_rate: 4.4
  median_home_value: 445700
  gini_index: 0.4472
  vacancy_rate: 3.14
  race_white: 525093
  race_black: 24691
  race_asian: 32489
  race_native: 1020
  hispanic: 42668
  bachelors_plus: 295620
districts:
  - to: "us/states/pa/districts/01"
    rel: in-district
    area_weight: 0.999
  - to: "us/states/pa/districts/senate/16"
    rel: in-district
    area_weight: 0.4297
  - to: "us/states/pa/districts/senate/10"
    rel: in-district
    area_weight: 0.3663
  - to: "us/states/pa/districts/senate/6"
    rel: in-district
    area_weight: 0.2035
  - to: "us/states/pa/districts/house/145"
    rel: in-district
    area_weight: 0.2785
  - to: "us/states/pa/districts/house/143"
    rel: in-district
    area_weight: 0.2164
  - to: "us/states/pa/districts/house/29"
    rel: in-district
    area_weight: 0.1322
  - to: "us/states/pa/districts/house/31"
    rel: in-district
    area_weight: 0.0861
  - to: "us/states/pa/districts/house/178"
    rel: in-district
    area_weight: 0.0804
  - to: "us/states/pa/districts/house/140"
    rel: in-district
    area_weight: 0.055
  - to: "us/states/pa/districts/house/142"
    rel: in-district
    area_weight: 0.044
  - to: "us/states/pa/districts/house/144"
    rel: in-district
    area_weight: 0.0424
  - to: "us/states/pa/districts/house/18"
    rel: in-district
    area_weight: 0.0341
  - to: "us/states/pa/districts/house/141"
    rel: in-district
    area_weight: 0.0306
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, pa]
timestamp: "2026-07-03"
---

# Bucks County, PA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 647461 |
| Under 18 | 128990 |
| 18–64 | 385485 |
| 65+ | 132986 |
| Median household income | 114764 |
| Poverty rate | 6.1 |
| Homeownership rate | 77.8 |
| Unemployment rate | 4.4 |
| Median home value | 445700 |
| Gini index | 0.4472 |
| Vacancy rate | 3.14 |
| White | 525093 |
| Black | 24691 |
| Asian | 32489 |
| Native | 1020 |
| Hispanic/Latino | 42668 |
| Bachelor's or higher | 295620 |

## Districts

- [PA-01](/us/states/pa/districts/01.md) — 100% (congressional)
- [PA Senate District 16](/us/states/pa/districts/senate/16.md) — 43% (state senate)
- [PA Senate District 10](/us/states/pa/districts/senate/10.md) — 37% (state senate)
- [PA Senate District 6](/us/states/pa/districts/senate/6.md) — 20% (state senate)
- [PA House District 145](/us/states/pa/districts/house/145.md) — 28% (state house)
- [PA House District 143](/us/states/pa/districts/house/143.md) — 22% (state house)
- [PA House District 29](/us/states/pa/districts/house/29.md) — 13% (state house)
- [PA House District 31](/us/states/pa/districts/house/31.md) — 9% (state house)
- [PA House District 178](/us/states/pa/districts/house/178.md) — 8% (state house)
- [PA House District 140](/us/states/pa/districts/house/140.md) — 6% (state house)
- [PA House District 142](/us/states/pa/districts/house/142.md) — 4% (state house)
- [PA House District 144](/us/states/pa/districts/house/144.md) — 4% (state house)
- [PA House District 18](/us/states/pa/districts/house/18.md) — 3% (state house)
- [PA House District 141](/us/states/pa/districts/house/141.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
