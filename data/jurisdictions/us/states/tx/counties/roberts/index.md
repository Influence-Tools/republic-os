---
type: Jurisdiction
title: "Roberts County, TX"
classification: county
fips: "48393"
state: "TX"
demographics:
  population: 832
  population_under_18: 226
  population_18_64: 458
  population_65_plus: 148
  median_household_income: 67868
  poverty_rate: 5.65
  homeownership_rate: 85.14
  unemployment_rate: 0.51
  median_home_value: 161500
  gini_index: 0.3787
  vacancy_rate: 17.81
  race_white: 778
  race_black: 3
  race_asian: 0
  race_native: 2
  hispanic: 55
  bachelors_plus: 130
districts:
  - to: "us/states/tx/districts/13"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/senate/31"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/88"
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

# Roberts County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 832 |
| Under 18 | 226 |
| 18–64 | 458 |
| 65+ | 148 |
| Median household income | 67868 |
| Poverty rate | 5.65 |
| Homeownership rate | 85.14 |
| Unemployment rate | 0.51 |
| Median home value | 161500 |
| Gini index | 0.3787 |
| Vacancy rate | 17.81 |
| White | 778 |
| Black | 3 |
| Asian | 0 |
| Native | 2 |
| Hispanic/Latino | 55 |
| Bachelor's or higher | 130 |

## Districts

- [TX-13](/us/states/tx/districts/13.md) — 100% (congressional)
- [TX Senate District 31](/us/states/tx/districts/senate/31.md) — 100% (state senate)
- [TX House District 88](/us/states/tx/districts/house/88.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
