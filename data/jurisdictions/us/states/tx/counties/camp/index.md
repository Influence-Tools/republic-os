---
type: Jurisdiction
title: "Camp County, TX"
classification: county
fips: "48063"
state: "TX"
demographics:
  population: 12798
  population_under_18: 3359
  population_18_64: 7038
  population_65_plus: 2401
  median_household_income: 58843
  poverty_rate: 19.92
  homeownership_rate: 77.5
  unemployment_rate: 5.68
  median_home_value: 173100
  gini_index: 0.4675
  vacancy_rate: 17.29
  race_white: 7564
  race_black: 2002
  race_asian: 173
  race_native: 0
  hispanic: 3504
  bachelors_plus: 2358
districts:
  - to: "us/states/tx/districts/01"
    rel: in-district
    area_weight: 0.9971
  - to: "us/states/tx/districts/senate/1"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/5"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Camp County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 12798 |
| Under 18 | 3359 |
| 18–64 | 7038 |
| 65+ | 2401 |
| Median household income | 58843 |
| Poverty rate | 19.92 |
| Homeownership rate | 77.5 |
| Unemployment rate | 5.68 |
| Median home value | 173100 |
| Gini index | 0.4675 |
| Vacancy rate | 17.29 |
| White | 7564 |
| Black | 2002 |
| Asian | 173 |
| Native | 0 |
| Hispanic/Latino | 3504 |
| Bachelor's or higher | 2358 |

## Districts

- [TX-01](/us/states/tx/districts/01.md) — 100% (congressional)
- [TX Senate District 1](/us/states/tx/districts/senate/1.md) — 100% (state senate)
- [TX House District 5](/us/states/tx/districts/house/5.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
