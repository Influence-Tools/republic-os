---
type: Jurisdiction
title: "Marion County, TX"
classification: county
fips: "48315"
state: "TX"
demographics:
  population: 9737
  population_under_18: 1649
  population_18_64: 5470
  population_65_plus: 2618
  median_household_income: 49672
  poverty_rate: 18.32
  homeownership_rate: 78.49
  unemployment_rate: 8.68
  median_home_value: 101500
  gini_index: 0.474
  vacancy_rate: 25.18
  race_white: 6854
  race_black: 2135
  race_asian: 16
  race_native: 40
  hispanic: 468
  bachelors_plus: 1343
districts:
  - to: "us/states/tx/districts/01"
    rel: in-district
    area_weight: 0.9984
  - to: "us/states/tx/districts/senate/1"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/7"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Marion County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9737 |
| Under 18 | 1649 |
| 18–64 | 5470 |
| 65+ | 2618 |
| Median household income | 49672 |
| Poverty rate | 18.32 |
| Homeownership rate | 78.49 |
| Unemployment rate | 8.68 |
| Median home value | 101500 |
| Gini index | 0.474 |
| Vacancy rate | 25.18 |
| White | 6854 |
| Black | 2135 |
| Asian | 16 |
| Native | 40 |
| Hispanic/Latino | 468 |
| Bachelor's or higher | 1343 |

## Districts

- [TX-01](/us/states/tx/districts/01.md) — 100% (congressional)
- [TX Senate District 1](/us/states/tx/districts/senate/1.md) — 100% (state senate)
- [TX House District 7](/us/states/tx/districts/house/7.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
