---
type: Jurisdiction
title: "Howard County, TX"
classification: county
fips: "48227"
state: "TX"
demographics:
  population: 32290
  population_under_18: 7297
  population_18_64: 20671
  population_65_plus: 4322
  median_household_income: 69649
  poverty_rate: 13.82
  homeownership_rate: 69.51
  unemployment_rate: 5.37
  median_home_value: 155600
  gini_index: 0.4489
  vacancy_rate: 13.22
  race_white: 20696
  race_black: 1660
  race_asian: 429
  race_native: 125
  hispanic: 15408
  bachelors_plus: 4578
districts:
  - to: "us/states/tx/districts/19"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tx/districts/senate/31"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/72"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Howard County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 32290 |
| Under 18 | 7297 |
| 18–64 | 20671 |
| 65+ | 4322 |
| Median household income | 69649 |
| Poverty rate | 13.82 |
| Homeownership rate | 69.51 |
| Unemployment rate | 5.37 |
| Median home value | 155600 |
| Gini index | 0.4489 |
| Vacancy rate | 13.22 |
| White | 20696 |
| Black | 1660 |
| Asian | 429 |
| Native | 125 |
| Hispanic/Latino | 15408 |
| Bachelor's or higher | 4578 |

## Districts

- [TX-19](/us/states/tx/districts/19.md) — 100% (congressional)
- [TX Senate District 31](/us/states/tx/districts/senate/31.md) — 100% (state senate)
- [TX House District 72](/us/states/tx/districts/house/72.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
