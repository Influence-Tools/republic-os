---
type: Jurisdiction
title: "Rusk County, TX"
classification: county
fips: "48401"
state: "TX"
demographics:
  population: 52842
  population_under_18: 11930
  population_18_64: 31687
  population_65_plus: 9225
  median_household_income: 68658
  poverty_rate: 14.41
  homeownership_rate: 78.84
  unemployment_rate: 4.46
  median_home_value: 171300
  gini_index: 0.48
  vacancy_rate: 15.41
  race_white: 34666
  race_black: 6976
  race_asian: 195
  race_native: 68
  hispanic: 10088
  bachelors_plus: 8538
districts:
  - to: "us/states/tx/districts/01"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/tx/districts/senate/1"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/11"
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

# Rusk County, TX

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 52842 |
| Under 18 | 11930 |
| 18–64 | 31687 |
| 65+ | 9225 |
| Median household income | 68658 |
| Poverty rate | 14.41 |
| Homeownership rate | 78.84 |
| Unemployment rate | 4.46 |
| Median home value | 171300 |
| Gini index | 0.48 |
| Vacancy rate | 15.41 |
| White | 34666 |
| Black | 6976 |
| Asian | 195 |
| Native | 68 |
| Hispanic/Latino | 10088 |
| Bachelor's or higher | 8538 |

## Districts

- [TX-01](/us/states/tx/districts/01.md) — 100% (congressional)
- [TX Senate District 1](/us/states/tx/districts/senate/1.md) — 100% (state senate)
- [TX House District 11](/us/states/tx/districts/house/11.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
