---
type: Jurisdiction
title: "Osceola County, FL"
classification: county
fips: "12097"
state: "FL"
demographics:
  population: 427415
  population_under_18: 102052
  population_18_64: 268101
  population_65_plus: 57262
  median_household_income: 72637
  poverty_rate: 12.81
  homeownership_rate: 65.33
  unemployment_rate: 5.36
  median_home_value: 353300
  gini_index: 0.4314
  vacancy_rate: 16.69
  race_white: 161840
  race_black: 47181
  race_asian: 12324
  race_native: 2057
  hispanic: 239150
  bachelors_plus: 111320
districts:
  - to: "us/states/fl/districts/09"
    rel: in-district
    area_weight: 0.9984
  - to: "us/states/fl/districts/senate/25"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/fl/districts/house/35"
    rel: in-district
    area_weight: 0.8084
  - to: "us/states/fl/districts/house/46"
    rel: in-district
    area_weight: 0.0995
  - to: "us/states/fl/districts/house/47"
    rel: in-district
    area_weight: 0.0604
  - to: "us/states/fl/districts/house/45"
    rel: in-district
    area_weight: 0.0315
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, fl]
timestamp: "2026-07-03"
---

# Osceola County, FL

County jurisdiction — 26 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 427415 |
| Under 18 | 102052 |
| 18–64 | 268101 |
| 65+ | 57262 |
| Median household income | 72637 |
| Poverty rate | 12.81 |
| Homeownership rate | 65.33 |
| Unemployment rate | 5.36 |
| Median home value | 353300 |
| Gini index | 0.4314 |
| Vacancy rate | 16.69 |
| White | 161840 |
| Black | 47181 |
| Asian | 12324 |
| Native | 2057 |
| Hispanic/Latino | 239150 |
| Bachelor's or higher | 111320 |

## Districts

- [FL-09](/us/states/fl/districts/09.md) — 100% (congressional)
- [FL Senate District 25](/us/states/fl/districts/senate/25.md) — 100% (state senate)
- [FL House District 35](/us/states/fl/districts/house/35.md) — 81% (state house)
- [FL House District 46](/us/states/fl/districts/house/46.md) — 10% (state house)
- [FL House District 47](/us/states/fl/districts/house/47.md) — 6% (state house)
- [FL House District 45](/us/states/fl/districts/house/45.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
