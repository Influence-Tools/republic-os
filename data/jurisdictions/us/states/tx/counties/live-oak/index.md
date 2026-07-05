---
type: Jurisdiction
title: "Live Oak County, TX"
classification: county
fips: "48297"
state: "TX"
demographics:
  population: 11620
  population_under_18: 2254
  population_18_64: 6990
  population_65_plus: 2376
  median_household_income: 57150
  poverty_rate: 17.06
  homeownership_rate: 71.34
  unemployment_rate: 5.88
  median_home_value: 159200
  gini_index: 0.4735
  vacancy_rate: 27.32
  race_white: 8104
  race_black: 262
  race_asian: 84
  race_native: 0
  hispanic: 4911
  bachelors_plus: 1902
districts:
  - to: "us/states/tx/districts/15"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/tx/districts/senate/21"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/31"
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

# Live Oak County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 11620 |
| Under 18 | 2254 |
| 18–64 | 6990 |
| 65+ | 2376 |
| Median household income | 57150 |
| Poverty rate | 17.06 |
| Homeownership rate | 71.34 |
| Unemployment rate | 5.88 |
| Median home value | 159200 |
| Gini index | 0.4735 |
| Vacancy rate | 27.32 |
| White | 8104 |
| Black | 262 |
| Asian | 84 |
| Native | 0 |
| Hispanic/Latino | 4911 |
| Bachelor's or higher | 1902 |

## Districts

- [TX-15](/us/states/tx/districts/15.md) — 100% (congressional)
- [TX Senate District 21](/us/states/tx/districts/senate/21.md) — 100% (state senate)
- [TX House District 31](/us/states/tx/districts/house/31.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
