---
type: Jurisdiction
title: "Lincoln County, TN"
classification: county
fips: "47103"
state: "TN"
demographics:
  population: 35946
  population_under_18: 8002
  population_18_64: 20727
  population_65_plus: 7217
  median_household_income: 64667
  poverty_rate: 12.95
  homeownership_rate: 75.82
  unemployment_rate: 4.73
  median_home_value: 229700
  gini_index: 0.4588
  vacancy_rate: 8.85
  race_white: 30704
  race_black: 1998
  race_asian: 227
  race_native: 88
  hispanic: 1482
  bachelors_plus: 7091
districts:
  - to: "us/states/tn/districts/04"
    rel: in-district
    area_weight: 0.9986
  - to: "us/states/tn/districts/senate/16"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/tn/districts/house/70"
    rel: in-district
    area_weight: 0.5096
  - to: "us/states/tn/districts/house/62"
    rel: in-district
    area_weight: 0.4902
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Lincoln County, TN

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 35946 |
| Under 18 | 8002 |
| 18–64 | 20727 |
| 65+ | 7217 |
| Median household income | 64667 |
| Poverty rate | 12.95 |
| Homeownership rate | 75.82 |
| Unemployment rate | 4.73 |
| Median home value | 229700 |
| Gini index | 0.4588 |
| Vacancy rate | 8.85 |
| White | 30704 |
| Black | 1998 |
| Asian | 227 |
| Native | 88 |
| Hispanic/Latino | 1482 |
| Bachelor's or higher | 7091 |

## Districts

- [TN-04](/us/states/tn/districts/04.md) — 100% (congressional)
- [TN Senate District 16](/us/states/tn/districts/senate/16.md) — 100% (state senate)
- [TN House District 70](/us/states/tn/districts/house/70.md) — 51% (state house)
- [TN House District 62](/us/states/tn/districts/house/62.md) — 49% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
