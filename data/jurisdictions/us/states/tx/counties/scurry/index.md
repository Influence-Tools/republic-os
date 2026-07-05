---
type: Jurisdiction
title: "Scurry County, TX"
classification: county
fips: "48415"
state: "TX"
demographics:
  population: 16488
  population_under_18: 4154
  population_18_64: 9770
  population_65_plus: 2564
  median_household_income: 60039
  poverty_rate: 11.6
  homeownership_rate: 76.82
  unemployment_rate: 2.44
  median_home_value: 113800
  gini_index: 0.4102
  vacancy_rate: 14.61
  race_white: 10628
  race_black: 537
  race_asian: 137
  race_native: 121
  hispanic: 7145
  bachelors_plus: 1704
districts:
  - to: "us/states/tx/districts/19"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/senate/31"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tx/districts/house/83"
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

# Scurry County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 16488 |
| Under 18 | 4154 |
| 18–64 | 9770 |
| 65+ | 2564 |
| Median household income | 60039 |
| Poverty rate | 11.6 |
| Homeownership rate | 76.82 |
| Unemployment rate | 2.44 |
| Median home value | 113800 |
| Gini index | 0.4102 |
| Vacancy rate | 14.61 |
| White | 10628 |
| Black | 537 |
| Asian | 137 |
| Native | 121 |
| Hispanic/Latino | 7145 |
| Bachelor's or higher | 1704 |

## Districts

- [TX-19](/us/states/tx/districts/19.md) — 100% (congressional)
- [TX Senate District 31](/us/states/tx/districts/senate/31.md) — 100% (state senate)
- [TX House District 83](/us/states/tx/districts/house/83.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
