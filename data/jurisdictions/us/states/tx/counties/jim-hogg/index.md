---
type: Jurisdiction
title: "Jim Hogg County, TX"
classification: county
fips: "48247"
state: "TX"
demographics:
  population: 4727
  population_under_18: 1527
  population_18_64: 2747
  population_65_plus: 453
  median_household_income: 42211
  poverty_rate: 31.43
  homeownership_rate: 56.37
  unemployment_rate: 6.31
  median_home_value: 129400
  gini_index: 0.4814
  vacancy_rate: 31.68
  race_white: 1585
  race_black: 16
  race_asian: 103
  race_native: 0
  hispanic: 4322
  bachelors_plus: 506
districts:
  - to: "us/states/tx/districts/28"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/senate/21"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/31"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Jim Hogg County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 4727 |
| Under 18 | 1527 |
| 18–64 | 2747 |
| 65+ | 453 |
| Median household income | 42211 |
| Poverty rate | 31.43 |
| Homeownership rate | 56.37 |
| Unemployment rate | 6.31 |
| Median home value | 129400 |
| Gini index | 0.4814 |
| Vacancy rate | 31.68 |
| White | 1585 |
| Black | 16 |
| Asian | 103 |
| Native | 0 |
| Hispanic/Latino | 4322 |
| Bachelor's or higher | 506 |

## Districts

- [TX-28](/us/states/tx/districts/28.md) — 100% (congressional)
- [TX Senate District 21](/us/states/tx/districts/senate/21.md) — 100% (state senate)
- [TX House District 31](/us/states/tx/districts/house/31.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
