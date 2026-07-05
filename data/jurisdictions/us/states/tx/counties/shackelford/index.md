---
type: Jurisdiction
title: "Shackelford County, TX"
classification: county
fips: "48417"
state: "TX"
demographics:
  population: 3175
  population_under_18: 656
  population_18_64: 1881
  population_65_plus: 638
  median_household_income: 73047
  poverty_rate: 9.53
  homeownership_rate: 78.65
  unemployment_rate: 7.47
  median_home_value: 174800
  gini_index: 0.417
  vacancy_rate: 17.9
  race_white: 2657
  race_black: 27
  race_asian: 1
  race_native: 14
  hispanic: 411
  bachelors_plus: 975
districts:
  - to: "us/states/tx/districts/19"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tx/districts/senate/10"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tx/districts/house/68"
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

# Shackelford County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3175 |
| Under 18 | 656 |
| 18–64 | 1881 |
| 65+ | 638 |
| Median household income | 73047 |
| Poverty rate | 9.53 |
| Homeownership rate | 78.65 |
| Unemployment rate | 7.47 |
| Median home value | 174800 |
| Gini index | 0.417 |
| Vacancy rate | 17.9 |
| White | 2657 |
| Black | 27 |
| Asian | 1 |
| Native | 14 |
| Hispanic/Latino | 411 |
| Bachelor's or higher | 975 |

## Districts

- [TX-19](/us/states/tx/districts/19.md) — 100% (congressional)
- [TX Senate District 10](/us/states/tx/districts/senate/10.md) — 100% (state senate)
- [TX House District 68](/us/states/tx/districts/house/68.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
