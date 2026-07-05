---
type: Jurisdiction
title: "Martin County, TX"
classification: county
fips: "48317"
state: "TX"
demographics:
  population: 5218
  population_under_18: 1558
  population_18_64: 3090
  population_65_plus: 570
  median_household_income: 93734
  poverty_rate: 8.32
  homeownership_rate: 78.05
  unemployment_rate: 5.37
  median_home_value: 174800
  gini_index: 0.4835
  vacancy_rate: 7.59
  race_white: 3505
  race_black: 146
  race_asian: 5
  race_native: 0
  hispanic: 2488
  bachelors_plus: 798
districts:
  - to: "us/states/tx/districts/19"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/senate/31"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/82"
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

# Martin County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5218 |
| Under 18 | 1558 |
| 18–64 | 3090 |
| 65+ | 570 |
| Median household income | 93734 |
| Poverty rate | 8.32 |
| Homeownership rate | 78.05 |
| Unemployment rate | 5.37 |
| Median home value | 174800 |
| Gini index | 0.4835 |
| Vacancy rate | 7.59 |
| White | 3505 |
| Black | 146 |
| Asian | 5 |
| Native | 0 |
| Hispanic/Latino | 2488 |
| Bachelor's or higher | 798 |

## Districts

- [TX-19](/us/states/tx/districts/19.md) — 100% (congressional)
- [TX Senate District 31](/us/states/tx/districts/senate/31.md) — 100% (state senate)
- [TX House District 82](/us/states/tx/districts/house/82.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
