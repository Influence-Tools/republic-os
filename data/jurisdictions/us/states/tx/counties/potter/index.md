---
type: Jurisdiction
title: "Potter County, TX"
classification: county
fips: "48375"
state: "TX"
demographics:
  population: 115975
  population_under_18: 30966
  population_18_64: 68398
  population_65_plus: 16611
  median_household_income: 53249
  poverty_rate: 20.83
  homeownership_rate: 57.29
  unemployment_rate: 3.83
  median_home_value: 147300
  gini_index: 0.4752
  vacancy_rate: 13.79
  race_white: 64757
  race_black: 12321
  race_asian: 5599
  race_native: 854
  hispanic: 45527
  bachelors_plus: 18111
districts:
  - to: "us/states/tx/districts/13"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/senate/31"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/87"
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

# Potter County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 115975 |
| Under 18 | 30966 |
| 18–64 | 68398 |
| 65+ | 16611 |
| Median household income | 53249 |
| Poverty rate | 20.83 |
| Homeownership rate | 57.29 |
| Unemployment rate | 3.83 |
| Median home value | 147300 |
| Gini index | 0.4752 |
| Vacancy rate | 13.79 |
| White | 64757 |
| Black | 12321 |
| Asian | 5599 |
| Native | 854 |
| Hispanic/Latino | 45527 |
| Bachelor's or higher | 18111 |

## Districts

- [TX-13](/us/states/tx/districts/13.md) — 100% (congressional)
- [TX Senate District 31](/us/states/tx/districts/senate/31.md) — 100% (state senate)
- [TX House District 87](/us/states/tx/districts/house/87.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
