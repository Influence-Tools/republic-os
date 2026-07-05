---
type: Jurisdiction
title: "Lampasas County, TX"
classification: county
fips: "48281"
state: "TX"
demographics:
  population: 22715
  population_under_18: 4829
  population_18_64: 13123
  population_65_plus: 4763
  median_household_income: 81736
  poverty_rate: 9.12
  homeownership_rate: 80.14
  unemployment_rate: 4.48
  median_home_value: 250400
  gini_index: 0.4055
  vacancy_rate: 15.0
  race_white: 17448
  race_black: 911
  race_asian: 268
  race_native: 159
  hispanic: 4657
  bachelors_plus: 5058
districts:
  - to: "us/states/tx/districts/11"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/tx/districts/senate/24"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/68"
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

# Lampasas County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 22715 |
| Under 18 | 4829 |
| 18–64 | 13123 |
| 65+ | 4763 |
| Median household income | 81736 |
| Poverty rate | 9.12 |
| Homeownership rate | 80.14 |
| Unemployment rate | 4.48 |
| Median home value | 250400 |
| Gini index | 0.4055 |
| Vacancy rate | 15.0 |
| White | 17448 |
| Black | 911 |
| Asian | 268 |
| Native | 159 |
| Hispanic/Latino | 4657 |
| Bachelor's or higher | 5058 |

## Districts

- [TX-11](/us/states/tx/districts/11.md) — 100% (congressional)
- [TX Senate District 24](/us/states/tx/districts/senate/24.md) — 100% (state senate)
- [TX House District 68](/us/states/tx/districts/house/68.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
