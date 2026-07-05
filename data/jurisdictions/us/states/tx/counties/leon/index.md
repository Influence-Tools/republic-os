---
type: Jurisdiction
title: "Leon County, TX"
classification: county
fips: "48289"
state: "TX"
demographics:
  population: 16263
  population_under_18: 3699
  population_18_64: 8565
  population_65_plus: 3999
  median_household_income: 61449
  poverty_rate: 16.4
  homeownership_rate: 76.58
  unemployment_rate: 4.17
  median_home_value: 186400
  gini_index: 0.4535
  vacancy_rate: 25.65
  race_white: 12350
  race_black: 1168
  race_asian: 24
  race_native: 175
  hispanic: 2712
  bachelors_plus: 2880
districts:
  - to: "us/states/tx/districts/17"
    rel: in-district
    area_weight: 0.9985
  - to: "us/states/tx/districts/senate/5"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/13"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Leon County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 16263 |
| Under 18 | 3699 |
| 18–64 | 8565 |
| 65+ | 3999 |
| Median household income | 61449 |
| Poverty rate | 16.4 |
| Homeownership rate | 76.58 |
| Unemployment rate | 4.17 |
| Median home value | 186400 |
| Gini index | 0.4535 |
| Vacancy rate | 25.65 |
| White | 12350 |
| Black | 1168 |
| Asian | 24 |
| Native | 175 |
| Hispanic/Latino | 2712 |
| Bachelor's or higher | 2880 |

## Districts

- [TX-17](/us/states/tx/districts/17.md) — 100% (congressional)
- [TX Senate District 5](/us/states/tx/districts/senate/5.md) — 100% (state senate)
- [TX House District 13](/us/states/tx/districts/house/13.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
