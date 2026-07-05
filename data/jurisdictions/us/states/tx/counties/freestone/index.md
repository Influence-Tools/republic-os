---
type: Jurisdiction
title: "Freestone County, TX"
classification: county
fips: "48161"
state: "TX"
demographics:
  population: 20049
  population_under_18: 4531
  population_18_64: 11481
  population_65_plus: 4037
  median_household_income: 59960
  poverty_rate: 12.3
  homeownership_rate: 75.43
  unemployment_rate: 3.04
  median_home_value: 168000
  gini_index: 0.4467
  vacancy_rate: 22.28
  race_white: 13164
  race_black: 2908
  race_asian: 44
  race_native: 92
  hispanic: 3455
  bachelors_plus: 2957
districts:
  - to: "us/states/tx/districts/06"
    rel: in-district
    area_weight: 0.5883
  - to: "us/states/tx/districts/17"
    rel: in-district
    area_weight: 0.4117
  - to: "us/states/tx/districts/senate/5"
    rel: in-district
    area_weight: 0.9997
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

# Freestone County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 20049 |
| Under 18 | 4531 |
| 18–64 | 11481 |
| 65+ | 4037 |
| Median household income | 59960 |
| Poverty rate | 12.3 |
| Homeownership rate | 75.43 |
| Unemployment rate | 3.04 |
| Median home value | 168000 |
| Gini index | 0.4467 |
| Vacancy rate | 22.28 |
| White | 13164 |
| Black | 2908 |
| Asian | 44 |
| Native | 92 |
| Hispanic/Latino | 3455 |
| Bachelor's or higher | 2957 |

## Districts

- [TX-06](/us/states/tx/districts/06.md) — 59% (congressional)
- [TX-17](/us/states/tx/districts/17.md) — 41% (congressional)
- [TX Senate District 5](/us/states/tx/districts/senate/5.md) — 100% (state senate)
- [TX House District 13](/us/states/tx/districts/house/13.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
