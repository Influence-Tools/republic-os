---
type: Jurisdiction
title: "Polk County, TX"
classification: county
fips: "48373"
state: "TX"
demographics:
  population: 52800
  population_under_18: 10727
  population_18_64: 31972
  population_65_plus: 10101
  median_household_income: 62259
  poverty_rate: 17.46
  homeownership_rate: 78.09
  unemployment_rate: 8.08
  median_home_value: 184800
  gini_index: 0.4359
  vacancy_rate: 26.26
  race_white: 39355
  race_black: 4087
  race_asian: 314
  race_native: 741
  hispanic: 8100
  bachelors_plus: 8256
districts:
  - to: "us/states/tx/districts/08"
    rel: in-district
    area_weight: 0.9989
  - to: "us/states/tx/districts/senate/3"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/9"
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

# Polk County, TX

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 52800 |
| Under 18 | 10727 |
| 18–64 | 31972 |
| 65+ | 10101 |
| Median household income | 62259 |
| Poverty rate | 17.46 |
| Homeownership rate | 78.09 |
| Unemployment rate | 8.08 |
| Median home value | 184800 |
| Gini index | 0.4359 |
| Vacancy rate | 26.26 |
| White | 39355 |
| Black | 4087 |
| Asian | 314 |
| Native | 741 |
| Hispanic/Latino | 8100 |
| Bachelor's or higher | 8256 |

## Districts

- [TX-08](/us/states/tx/districts/08.md) — 100% (congressional)
- [TX Senate District 3](/us/states/tx/districts/senate/3.md) — 100% (state senate)
- [TX House District 9](/us/states/tx/districts/house/9.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
