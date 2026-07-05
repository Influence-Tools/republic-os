---
type: Jurisdiction
title: "Kimble County, TX"
classification: county
fips: "48267"
state: "TX"
demographics:
  population: 4389
  population_under_18: 746
  population_18_64: 2272
  population_65_plus: 1371
  median_household_income: 69455
  poverty_rate: 11.68
  homeownership_rate: 78.93
  unemployment_rate: 1.27
  median_home_value: 201300
  gini_index: 0.4366
  vacancy_rate: 25.4
  race_white: 3247
  race_black: 62
  race_asian: 0
  race_native: 50
  hispanic: 1162
  bachelors_plus: 1205
districts:
  - to: "us/states/tx/districts/11"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/tx/districts/senate/24"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/53"
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

# Kimble County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 4389 |
| Under 18 | 746 |
| 18–64 | 2272 |
| 65+ | 1371 |
| Median household income | 69455 |
| Poverty rate | 11.68 |
| Homeownership rate | 78.93 |
| Unemployment rate | 1.27 |
| Median home value | 201300 |
| Gini index | 0.4366 |
| Vacancy rate | 25.4 |
| White | 3247 |
| Black | 62 |
| Asian | 0 |
| Native | 50 |
| Hispanic/Latino | 1162 |
| Bachelor's or higher | 1205 |

## Districts

- [TX-11](/us/states/tx/districts/11.md) — 100% (congressional)
- [TX Senate District 24](/us/states/tx/districts/senate/24.md) — 100% (state senate)
- [TX House District 53](/us/states/tx/districts/house/53.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
