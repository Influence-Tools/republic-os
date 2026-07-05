---
type: Jurisdiction
title: "Eastland County, TX"
classification: county
fips: "48133"
state: "TX"
demographics:
  population: 18011
  population_under_18: 3805
  population_18_64: 10256
  population_65_plus: 3950
  median_household_income: 53549
  poverty_rate: 16.21
  homeownership_rate: 71.59
  unemployment_rate: 4.69
  median_home_value: 134800
  gini_index: 0.4605
  vacancy_rate: 22.89
  race_white: 14545
  race_black: 388
  race_asian: 85
  race_native: 90
  hispanic: 3109
  bachelors_plus: 3635
districts:
  - to: "us/states/tx/districts/25"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/senate/22"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/68"
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

# Eastland County, TX

County jurisdiction — 3 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 18011 |
| Under 18 | 3805 |
| 18–64 | 10256 |
| 65+ | 3950 |
| Median household income | 53549 |
| Poverty rate | 16.21 |
| Homeownership rate | 71.59 |
| Unemployment rate | 4.69 |
| Median home value | 134800 |
| Gini index | 0.4605 |
| Vacancy rate | 22.89 |
| White | 14545 |
| Black | 388 |
| Asian | 85 |
| Native | 90 |
| Hispanic/Latino | 3109 |
| Bachelor's or higher | 3635 |

## Districts

- [TX-25](/us/states/tx/districts/25.md) — 100% (congressional)
- [TX Senate District 22](/us/states/tx/districts/senate/22.md) — 100% (state senate)
- [TX House District 68](/us/states/tx/districts/house/68.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
