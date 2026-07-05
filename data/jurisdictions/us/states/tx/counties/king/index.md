---
type: Jurisdiction
title: "King County, TX"
classification: county
fips: "48269"
state: "TX"
demographics:
  population: 211
  population_under_18: 31
  population_18_64: 115
  population_65_plus: 65
  median_household_income: 46645
  poverty_rate: 23.7
  homeownership_rate: 59.46
  unemployment_rate: 0.0
  median_home_value: 52100
  gini_index: 0.4772
  vacancy_rate: 41.27
  race_white: 146
  race_black: 0
  race_asian: 0
  race_native: 0
  hispanic: 35
  bachelors_plus: 79
districts:
  - to: "us/states/tx/districts/13"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/tx/districts/senate/28"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/69"
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

# King County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 211 |
| Under 18 | 31 |
| 18–64 | 115 |
| 65+ | 65 |
| Median household income | 46645 |
| Poverty rate | 23.7 |
| Homeownership rate | 59.46 |
| Unemployment rate | 0.0 |
| Median home value | 52100 |
| Gini index | 0.4772 |
| Vacancy rate | 41.27 |
| White | 146 |
| Black | 0 |
| Asian | 0 |
| Native | 0 |
| Hispanic/Latino | 35 |
| Bachelor's or higher | 79 |

## Districts

- [TX-13](/us/states/tx/districts/13.md) — 100% (congressional)
- [TX Senate District 28](/us/states/tx/districts/senate/28.md) — 100% (state senate)
- [TX House District 69](/us/states/tx/districts/house/69.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
