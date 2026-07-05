---
type: Jurisdiction
title: "Kaufman County, TX"
classification: county
fips: "48257"
state: "TX"
demographics:
  population: 172604
  population_under_18: 49649
  population_18_64: 104551
  population_65_plus: 18404
  median_household_income: 89485
  poverty_rate: 9.68
  homeownership_rate: 78.09
  unemployment_rate: 5.31
  median_home_value: 320900
  gini_index: 0.3925
  vacancy_rate: 5.8
  race_white: 93550
  race_black: 32086
  race_asian: 3293
  race_native: 1450
  hispanic: 47209
  bachelors_plus: 37148
districts:
  - to: "us/states/tx/districts/05"
    rel: in-district
    area_weight: 0.9979
  - to: "us/states/tx/districts/senate/2"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/4"
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

# Kaufman County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 172604 |
| Under 18 | 49649 |
| 18–64 | 104551 |
| 65+ | 18404 |
| Median household income | 89485 |
| Poverty rate | 9.68 |
| Homeownership rate | 78.09 |
| Unemployment rate | 5.31 |
| Median home value | 320900 |
| Gini index | 0.3925 |
| Vacancy rate | 5.8 |
| White | 93550 |
| Black | 32086 |
| Asian | 3293 |
| Native | 1450 |
| Hispanic/Latino | 47209 |
| Bachelor's or higher | 37148 |

## Districts

- [TX-05](/us/states/tx/districts/05.md) — 100% (congressional)
- [TX Senate District 2](/us/states/tx/districts/senate/2.md) — 100% (state senate)
- [TX House District 4](/us/states/tx/districts/house/4.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
