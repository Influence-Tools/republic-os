---
type: Jurisdiction
title: "Brown County, TX"
classification: county
fips: "48049"
state: "TX"
demographics:
  population: 38347
  population_under_18: 7819
  population_18_64: 22466
  population_65_plus: 8062
  median_household_income: 57470
  poverty_rate: 15.32
  homeownership_rate: 68.28
  unemployment_rate: 5.27
  median_home_value: 158900
  gini_index: 0.4528
  vacancy_rate: 22.21
  race_white: 28670
  race_black: 1408
  race_asian: 228
  race_native: 69
  hispanic: 8617
  bachelors_plus: 7003
districts:
  - to: "us/states/tx/districts/11"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/senate/10"
    rel: in-district
    area_weight: 0.9999
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

# Brown County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 38347 |
| Under 18 | 7819 |
| 18–64 | 22466 |
| 65+ | 8062 |
| Median household income | 57470 |
| Poverty rate | 15.32 |
| Homeownership rate | 68.28 |
| Unemployment rate | 5.27 |
| Median home value | 158900 |
| Gini index | 0.4528 |
| Vacancy rate | 22.21 |
| White | 28670 |
| Black | 1408 |
| Asian | 228 |
| Native | 69 |
| Hispanic/Latino | 8617 |
| Bachelor's or higher | 7003 |

## Districts

- [TX-11](/us/states/tx/districts/11.md) — 100% (congressional)
- [TX Senate District 10](/us/states/tx/districts/senate/10.md) — 100% (state senate)
- [TX House District 68](/us/states/tx/districts/house/68.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
