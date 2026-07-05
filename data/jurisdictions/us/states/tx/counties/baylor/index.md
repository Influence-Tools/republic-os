---
type: Jurisdiction
title: "Baylor County, TX"
classification: county
fips: "48023"
state: "TX"
demographics:
  population: 3485
  population_under_18: 756
  population_18_64: 1779
  population_65_plus: 950
  median_household_income: 45370
  poverty_rate: 21.79
  homeownership_rate: 66.21
  unemployment_rate: 4.49
  median_home_value: 103100
  gini_index: 0.466
  vacancy_rate: 30.14
  race_white: 2874
  race_black: 43
  race_asian: 0
  race_native: 15
  hispanic: 458
  bachelors_plus: 795
districts:
  - to: "us/states/tx/districts/13"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/senate/28"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/69"
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

# Baylor County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3485 |
| Under 18 | 756 |
| 18–64 | 1779 |
| 65+ | 950 |
| Median household income | 45370 |
| Poverty rate | 21.79 |
| Homeownership rate | 66.21 |
| Unemployment rate | 4.49 |
| Median home value | 103100 |
| Gini index | 0.466 |
| Vacancy rate | 30.14 |
| White | 2874 |
| Black | 43 |
| Asian | 0 |
| Native | 15 |
| Hispanic/Latino | 458 |
| Bachelor's or higher | 795 |

## Districts

- [TX-13](/us/states/tx/districts/13.md) — 100% (congressional)
- [TX Senate District 28](/us/states/tx/districts/senate/28.md) — 100% (state senate)
- [TX House District 69](/us/states/tx/districts/house/69.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
