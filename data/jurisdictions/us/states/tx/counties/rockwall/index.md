---
type: Jurisdiction
title: "Rockwall County, TX"
classification: county
fips: "48397"
state: "TX"
demographics:
  population: 123617
  population_under_18: 32755
  population_18_64: 75249
  population_65_plus: 15613
  median_household_income: 127981
  poverty_rate: 4.04
  homeownership_rate: 82.53
  unemployment_rate: 4.29
  median_home_value: 415500
  gini_index: 0.4213
  vacancy_rate: 5.38
  race_white: 83523
  race_black: 11479
  race_asian: 4322
  race_native: 559
  hispanic: 25723
  bachelors_plus: 48616
districts:
  - to: "us/states/tx/districts/04"
    rel: in-district
    area_weight: 0.9991
  - to: "us/states/tx/districts/senate/2"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tx/districts/house/33"
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

# Rockwall County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 123617 |
| Under 18 | 32755 |
| 18–64 | 75249 |
| 65+ | 15613 |
| Median household income | 127981 |
| Poverty rate | 4.04 |
| Homeownership rate | 82.53 |
| Unemployment rate | 4.29 |
| Median home value | 415500 |
| Gini index | 0.4213 |
| Vacancy rate | 5.38 |
| White | 83523 |
| Black | 11479 |
| Asian | 4322 |
| Native | 559 |
| Hispanic/Latino | 25723 |
| Bachelor's or higher | 48616 |

## Districts

- [TX-04](/us/states/tx/districts/04.md) — 100% (congressional)
- [TX Senate District 2](/us/states/tx/districts/senate/2.md) — 100% (state senate)
- [TX House District 33](/us/states/tx/districts/house/33.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
