---
type: Jurisdiction
title: "Limestone County, TX"
classification: county
fips: "48293"
state: "TX"
demographics:
  population: 22283
  population_under_18: 4987
  population_18_64: 12639
  population_65_plus: 4657
  median_household_income: 60573
  poverty_rate: 17.07
  homeownership_rate: 72.13
  unemployment_rate: 3.72
  median_home_value: 164200
  gini_index: 0.4332
  vacancy_rate: 19.67
  race_white: 13176
  race_black: 3811
  race_asian: 219
  race_native: 16
  hispanic: 5243
  bachelors_plus: 3799
districts:
  - to: "us/states/tx/districts/17"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/senate/5"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/13"
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

# Limestone County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 22283 |
| Under 18 | 4987 |
| 18–64 | 12639 |
| 65+ | 4657 |
| Median household income | 60573 |
| Poverty rate | 17.07 |
| Homeownership rate | 72.13 |
| Unemployment rate | 3.72 |
| Median home value | 164200 |
| Gini index | 0.4332 |
| Vacancy rate | 19.67 |
| White | 13176 |
| Black | 3811 |
| Asian | 219 |
| Native | 16 |
| Hispanic/Latino | 5243 |
| Bachelor's or higher | 3799 |

## Districts

- [TX-17](/us/states/tx/districts/17.md) — 100% (congressional)
- [TX Senate District 5](/us/states/tx/districts/senate/5.md) — 100% (state senate)
- [TX House District 13](/us/states/tx/districts/house/13.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
