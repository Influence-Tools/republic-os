---
type: Jurisdiction
title: "Brewster County, TX"
classification: county
fips: "48043"
state: "TX"
demographics:
  population: 9503
  population_under_18: 1588
  population_18_64: 5400
  population_65_plus: 2515
  median_household_income: 56212
  poverty_rate: 8.93
  homeownership_rate: 62.49
  unemployment_rate: 3.04
  median_home_value: 227000
  gini_index: 0.4175
  vacancy_rate: 16.33
  race_white: 6547
  race_black: 56
  race_asian: 177
  race_native: 0
  hispanic: 3998
  bachelors_plus: 4517
districts:
  - to: "us/states/tx/districts/23"
    rel: in-district
    area_weight: 0.9988
  - to: "us/states/tx/districts/senate/19"
    rel: in-district
    area_weight: 0.5605
  - to: "us/states/tx/districts/senate/29"
    rel: in-district
    area_weight: 0.4394
  - to: "us/states/tx/districts/house/74"
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

# Brewster County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9503 |
| Under 18 | 1588 |
| 18–64 | 5400 |
| 65+ | 2515 |
| Median household income | 56212 |
| Poverty rate | 8.93 |
| Homeownership rate | 62.49 |
| Unemployment rate | 3.04 |
| Median home value | 227000 |
| Gini index | 0.4175 |
| Vacancy rate | 16.33 |
| White | 6547 |
| Black | 56 |
| Asian | 177 |
| Native | 0 |
| Hispanic/Latino | 3998 |
| Bachelor's or higher | 4517 |

## Districts

- [TX-23](/us/states/tx/districts/23.md) — 100% (congressional)
- [TX Senate District 19](/us/states/tx/districts/senate/19.md) — 56% (state senate)
- [TX Senate District 29](/us/states/tx/districts/senate/29.md) — 44% (state senate)
- [TX House District 74](/us/states/tx/districts/house/74.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
