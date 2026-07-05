---
type: Jurisdiction
title: "Reeves County, TX"
classification: county
fips: "48389"
state: "TX"
demographics:
  population: 12664
  population_under_18: 3276
  population_18_64: 7793
  population_65_plus: 1595
  median_household_income: 64297
  poverty_rate: 16.76
  homeownership_rate: 73.7
  unemployment_rate: 2.36
  median_home_value: 118000
  gini_index: 0.4317
  vacancy_rate: 18.25
  race_white: 4910
  race_black: 226
  race_asian: 23
  race_native: 166
  hispanic: 10798
  bachelors_plus: 748
districts:
  - to: "us/states/tx/districts/23"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/senate/29"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tx/districts/house/74"
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

# Reeves County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 12664 |
| Under 18 | 3276 |
| 18–64 | 7793 |
| 65+ | 1595 |
| Median household income | 64297 |
| Poverty rate | 16.76 |
| Homeownership rate | 73.7 |
| Unemployment rate | 2.36 |
| Median home value | 118000 |
| Gini index | 0.4317 |
| Vacancy rate | 18.25 |
| White | 4910 |
| Black | 226 |
| Asian | 23 |
| Native | 166 |
| Hispanic/Latino | 10798 |
| Bachelor's or higher | 748 |

## Districts

- [TX-23](/us/states/tx/districts/23.md) — 100% (congressional)
- [TX Senate District 29](/us/states/tx/districts/senate/29.md) — 100% (state senate)
- [TX House District 74](/us/states/tx/districts/house/74.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
