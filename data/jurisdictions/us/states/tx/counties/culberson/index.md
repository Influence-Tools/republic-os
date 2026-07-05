---
type: Jurisdiction
title: "Culberson County, TX"
classification: county
fips: "48109"
state: "TX"
demographics:
  population: 2195
  population_under_18: 592
  population_18_64: 962
  population_65_plus: 641
  median_household_income: 58777
  poverty_rate: 19.48
  homeownership_rate: 70.16
  unemployment_rate: 1.2
  median_home_value: 79300
  gini_index: 0.3961
  vacancy_rate: 20.88
  race_white: 1127
  race_black: 5
  race_asian: 27
  race_native: 64
  hispanic: 1712
  bachelors_plus: 253
districts:
  - to: "us/states/tx/districts/23"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/senate/29"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/74"
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

# Culberson County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2195 |
| Under 18 | 592 |
| 18–64 | 962 |
| 65+ | 641 |
| Median household income | 58777 |
| Poverty rate | 19.48 |
| Homeownership rate | 70.16 |
| Unemployment rate | 1.2 |
| Median home value | 79300 |
| Gini index | 0.3961 |
| Vacancy rate | 20.88 |
| White | 1127 |
| Black | 5 |
| Asian | 27 |
| Native | 64 |
| Hispanic/Latino | 1712 |
| Bachelor's or higher | 253 |

## Districts

- [TX-23](/us/states/tx/districts/23.md) — 100% (congressional)
- [TX Senate District 29](/us/states/tx/districts/senate/29.md) — 100% (state senate)
- [TX House District 74](/us/states/tx/districts/house/74.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
