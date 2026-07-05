---
type: Jurisdiction
title: "Cochran County, TX"
classification: county
fips: "48079"
state: "TX"
demographics:
  population: 2550
  population_under_18: 714
  population_18_64: 1468
  population_65_plus: 368
  median_household_income: 45313
  poverty_rate: 27.76
  homeownership_rate: 64.64
  unemployment_rate: 4.81
  median_home_value: 53200
  gini_index: 0.4766
  vacancy_rate: 27.29
  race_white: 1089
  race_black: 125
  race_asian: 1
  race_native: 10
  hispanic: 1536
  bachelors_plus: 157
districts:
  - to: "us/states/tx/districts/19"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/senate/31"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/88"
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

# Cochran County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2550 |
| Under 18 | 714 |
| 18–64 | 1468 |
| 65+ | 368 |
| Median household income | 45313 |
| Poverty rate | 27.76 |
| Homeownership rate | 64.64 |
| Unemployment rate | 4.81 |
| Median home value | 53200 |
| Gini index | 0.4766 |
| Vacancy rate | 27.29 |
| White | 1089 |
| Black | 125 |
| Asian | 1 |
| Native | 10 |
| Hispanic/Latino | 1536 |
| Bachelor's or higher | 157 |

## Districts

- [TX-19](/us/states/tx/districts/19.md) — 100% (congressional)
- [TX Senate District 31](/us/states/tx/districts/senate/31.md) — 100% (state senate)
- [TX House District 88](/us/states/tx/districts/house/88.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
