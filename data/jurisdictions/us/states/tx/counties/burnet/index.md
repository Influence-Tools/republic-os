---
type: Jurisdiction
title: "Burnet County, TX"
classification: county
fips: "48053"
state: "TX"
demographics:
  population: 52652
  population_under_18: 10775
  population_18_64: 29451
  population_65_plus: 12426
  median_household_income: 78732
  poverty_rate: 7.96
  homeownership_rate: 76.3
  unemployment_rate: 2.63
  median_home_value: 344000
  gini_index: 0.4551
  vacancy_rate: 17.95
  race_white: 41755
  race_black: 656
  race_asian: 377
  race_native: 356
  hispanic: 12318
  bachelors_plus: 14472
districts:
  - to: "us/states/tx/districts/31"
    rel: in-district
    area_weight: 0.9967
  - to: "us/states/tx/districts/senate/24"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/19"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Burnet County, TX

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 52652 |
| Under 18 | 10775 |
| 18–64 | 29451 |
| 65+ | 12426 |
| Median household income | 78732 |
| Poverty rate | 7.96 |
| Homeownership rate | 76.3 |
| Unemployment rate | 2.63 |
| Median home value | 344000 |
| Gini index | 0.4551 |
| Vacancy rate | 17.95 |
| White | 41755 |
| Black | 656 |
| Asian | 377 |
| Native | 356 |
| Hispanic/Latino | 12318 |
| Bachelor's or higher | 14472 |

## Districts

- [TX-31](/us/states/tx/districts/31.md) — 100% (congressional)
- [TX Senate District 24](/us/states/tx/districts/senate/24.md) — 100% (state senate)
- [TX House District 19](/us/states/tx/districts/house/19.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
