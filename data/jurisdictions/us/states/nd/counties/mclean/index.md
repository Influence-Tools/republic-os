---
type: Jurisdiction
title: "McLean County, ND"
classification: county
fips: "38055"
state: "ND"
demographics:
  population: 9823
  population_under_18: 2069
  population_18_64: 5173
  population_65_plus: 2581
  median_household_income: 83583
  poverty_rate: 8.88
  homeownership_rate: 84.17
  unemployment_rate: 1.35
  median_home_value: 227100
  gini_index: 0.4057
  vacancy_rate: 24.63
  race_white: 8698
  race_black: 10
  race_asian: 100
  race_native: 576
  hispanic: 201
  bachelors_plus: 2251
districts:
  - to: "us/states/nd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/nd/districts/senate/6"
    rel: in-district
    area_weight: 0.4319
  - to: "us/states/nd/districts/senate/4"
    rel: in-district
    area_weight: 0.4155
  - to: "us/states/nd/districts/senate/33"
    rel: in-district
    area_weight: 0.1524
  - to: "us/states/nd/districts/house/6"
    rel: in-district
    area_weight: 0.4319
  - to: "us/states/nd/districts/house/4b"
    rel: in-district
    area_weight: 0.2109
  - to: "us/states/nd/districts/house/4a"
    rel: in-district
    area_weight: 0.2046
  - to: "us/states/nd/districts/house/33"
    rel: in-district
    area_weight: 0.1524
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nd]
timestamp: "2026-07-03"
---

# McLean County, ND

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9823 |
| Under 18 | 2069 |
| 18–64 | 5173 |
| 65+ | 2581 |
| Median household income | 83583 |
| Poverty rate | 8.88 |
| Homeownership rate | 84.17 |
| Unemployment rate | 1.35 |
| Median home value | 227100 |
| Gini index | 0.4057 |
| Vacancy rate | 24.63 |
| White | 8698 |
| Black | 10 |
| Asian | 100 |
| Native | 576 |
| Hispanic/Latino | 201 |
| Bachelor's or higher | 2251 |

## Districts

- [ND-00](/us/states/nd/districts/00.md) — 100% (congressional)
- [ND Senate District 6](/us/states/nd/districts/senate/6.md) — 43% (state senate)
- [ND Senate District 4](/us/states/nd/districts/senate/4.md) — 42% (state senate)
- [ND Senate District 33](/us/states/nd/districts/senate/33.md) — 15% (state senate)
- [ND House District 6](/us/states/nd/districts/house/6.md) — 43% (state house)
- [ND House District 4B](/us/states/nd/districts/house/4b.md) — 21% (state house)
- [ND House District 4A](/us/states/nd/districts/house/4a.md) — 20% (state house)
- [ND House District 33](/us/states/nd/districts/house/33.md) — 15% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
