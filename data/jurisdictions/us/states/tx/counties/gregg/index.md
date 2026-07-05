---
type: Jurisdiction
title: "Gregg County, TX"
classification: county
fips: "48183"
state: "TX"
demographics:
  population: 125480
  population_under_18: 32277
  population_18_64: 73028
  population_65_plus: 20175
  median_household_income: 66550
  poverty_rate: 16.1
  homeownership_rate: 60.33
  unemployment_rate: 3.6
  median_home_value: 203400
  gini_index: 0.4555
  vacancy_rate: 10.4
  race_white: 72261
  race_black: 22555
  race_asian: 1656
  race_native: 624
  hispanic: 25347
  bachelors_plus: 24731
districts:
  - to: "us/states/tx/districts/01"
    rel: in-district
    area_weight: 0.9988
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

# Gregg County, TX

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 125480 |
| Under 18 | 32277 |
| 18–64 | 73028 |
| 65+ | 20175 |
| Median household income | 66550 |
| Poverty rate | 16.1 |
| Homeownership rate | 60.33 |
| Unemployment rate | 3.6 |
| Median home value | 203400 |
| Gini index | 0.4555 |
| Vacancy rate | 10.4 |
| White | 72261 |
| Black | 22555 |
| Asian | 1656 |
| Native | 624 |
| Hispanic/Latino | 25347 |
| Bachelor's or higher | 24731 |

## Districts

- [TX-01](/us/states/tx/districts/01.md) — 100% (congressional)
- [TX Senate District 1](/us/states/tx/districts/senate/1.md) — 100% (state senate)
- [TX House District 7](/us/states/tx/districts/house/7.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
