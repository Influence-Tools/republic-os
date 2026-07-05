---
type: Jurisdiction
title: "Kent County, TX"
classification: county
fips: "48263"
state: "TX"
demographics:
  population: 734
  population_under_18: 89
  population_18_64: 371
  population_65_plus: 274
  median_household_income: 72889
  poverty_rate: 9.85
  homeownership_rate: 79.22
  unemployment_rate: 8.47
  median_home_value: 122200
  gini_index: 0.4658
  vacancy_rate: 41.11
  race_white: 624
  race_black: 7
  race_asian: 0
  race_native: 0
  hispanic: 118
  bachelors_plus: 212
districts:
  - to: "us/states/tx/districts/19"
    rel: in-district
    area_weight: 0.9984
  - to: "us/states/tx/districts/senate/28"
    rel: in-district
    area_weight: 1.0
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

# Kent County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 734 |
| Under 18 | 89 |
| 18–64 | 371 |
| 65+ | 274 |
| Median household income | 72889 |
| Poverty rate | 9.85 |
| Homeownership rate | 79.22 |
| Unemployment rate | 8.47 |
| Median home value | 122200 |
| Gini index | 0.4658 |
| Vacancy rate | 41.11 |
| White | 624 |
| Black | 7 |
| Asian | 0 |
| Native | 0 |
| Hispanic/Latino | 118 |
| Bachelor's or higher | 212 |

## Districts

- [TX-19](/us/states/tx/districts/19.md) — 100% (congressional)
- [TX Senate District 28](/us/states/tx/districts/senate/28.md) — 100% (state senate)
- [TX House District 83](/us/states/tx/districts/house/83.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
