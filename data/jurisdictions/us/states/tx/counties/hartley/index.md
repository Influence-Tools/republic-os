---
type: Jurisdiction
title: "Hartley County, TX"
classification: county
fips: "48205"
state: "TX"
demographics:
  population: 5215
  population_under_18: 1160
  population_18_64: 3223
  population_65_plus: 832
  median_household_income: 75841
  poverty_rate: 9.38
  homeownership_rate: 74.4
  unemployment_rate: 1.65
  median_home_value: 262500
  gini_index: 0.4223
  vacancy_rate: 9.98
  race_white: 3631
  race_black: 315
  race_asian: 9
  race_native: 10
  hispanic: 1626
  bachelors_plus: 1077
districts:
  - to: "us/states/tx/districts/13"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/senate/31"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/86"
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

# Hartley County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5215 |
| Under 18 | 1160 |
| 18–64 | 3223 |
| 65+ | 832 |
| Median household income | 75841 |
| Poverty rate | 9.38 |
| Homeownership rate | 74.4 |
| Unemployment rate | 1.65 |
| Median home value | 262500 |
| Gini index | 0.4223 |
| Vacancy rate | 9.98 |
| White | 3631 |
| Black | 315 |
| Asian | 9 |
| Native | 10 |
| Hispanic/Latino | 1626 |
| Bachelor's or higher | 1077 |

## Districts

- [TX-13](/us/states/tx/districts/13.md) — 100% (congressional)
- [TX Senate District 31](/us/states/tx/districts/senate/31.md) — 100% (state senate)
- [TX House District 86](/us/states/tx/districts/house/86.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
