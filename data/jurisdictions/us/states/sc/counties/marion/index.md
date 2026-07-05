---
type: Jurisdiction
title: "Marion County, SC"
classification: county
fips: "45067"
state: "SC"
demographics:
  population: 28664
  population_under_18: 6333
  population_18_64: 16128
  population_65_plus: 6203
  median_household_income: 36301
  poverty_rate: 29.99
  homeownership_rate: 62.63
  unemployment_rate: 7.24
  median_home_value: 93200
  gini_index: 0.4938
  vacancy_rate: 16.05
  race_white: 11234
  race_black: 15736
  race_asian: 3
  race_native: 185
  hispanic: 789
  bachelors_plus: 4169
districts:
  - to: "us/states/sc/districts/07"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/sc/districts/senate/30"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/sc/districts/house/57"
    rel: in-district
    area_weight: 0.6308
  - to: "us/states/sc/districts/house/59"
    rel: in-district
    area_weight: 0.3686
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sc]
timestamp: "2026-07-03"
---

# Marion County, SC

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 28664 |
| Under 18 | 6333 |
| 18–64 | 16128 |
| 65+ | 6203 |
| Median household income | 36301 |
| Poverty rate | 29.99 |
| Homeownership rate | 62.63 |
| Unemployment rate | 7.24 |
| Median home value | 93200 |
| Gini index | 0.4938 |
| Vacancy rate | 16.05 |
| White | 11234 |
| Black | 15736 |
| Asian | 3 |
| Native | 185 |
| Hispanic/Latino | 789 |
| Bachelor's or higher | 4169 |

## Districts

- [SC-07](/us/states/sc/districts/07.md) — 100% (congressional)
- [SC Senate District 30](/us/states/sc/districts/senate/30.md) — 100% (state senate)
- [SC House District 57](/us/states/sc/districts/house/57.md) — 63% (state house)
- [SC House District 59](/us/states/sc/districts/house/59.md) — 37% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
