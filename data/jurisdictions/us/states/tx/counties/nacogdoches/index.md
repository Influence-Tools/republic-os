---
type: Jurisdiction
title: "Nacogdoches County, TX"
classification: county
fips: "48347"
state: "TX"
demographics:
  population: 65162
  population_under_18: 15182
  population_18_64: 39738
  population_65_plus: 10242
  median_household_income: 53555
  poverty_rate: 21.8
  homeownership_rate: 59.26
  unemployment_rate: 7.02
  median_home_value: 169200
  gini_index: 0.5086
  vacancy_rate: 13.22
  race_white: 40377
  race_black: 10903
  race_asian: 554
  race_native: 299
  hispanic: 14101
  bachelors_plus: 14898
districts:
  - to: "us/states/tx/districts/17"
    rel: in-district
    area_weight: 0.9973
  - to: "us/states/tx/districts/senate/3"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/11"
    rel: in-district
    area_weight: 0.9993
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Nacogdoches County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 65162 |
| Under 18 | 15182 |
| 18–64 | 39738 |
| 65+ | 10242 |
| Median household income | 53555 |
| Poverty rate | 21.8 |
| Homeownership rate | 59.26 |
| Unemployment rate | 7.02 |
| Median home value | 169200 |
| Gini index | 0.5086 |
| Vacancy rate | 13.22 |
| White | 40377 |
| Black | 10903 |
| Asian | 554 |
| Native | 299 |
| Hispanic/Latino | 14101 |
| Bachelor's or higher | 14898 |

## Districts

- [TX-17](/us/states/tx/districts/17.md) — 100% (congressional)
- [TX Senate District 3](/us/states/tx/districts/senate/3.md) — 100% (state senate)
- [TX House District 11](/us/states/tx/districts/house/11.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
