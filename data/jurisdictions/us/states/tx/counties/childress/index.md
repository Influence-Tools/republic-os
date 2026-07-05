---
type: Jurisdiction
title: "Childress County, TX"
classification: county
fips: "48075"
state: "TX"
demographics:
  population: 6743
  population_under_18: 1364
  population_18_64: 4225
  population_65_plus: 1154
  median_household_income: 58654
  poverty_rate: 15.35
  homeownership_rate: 71.0
  unemployment_rate: 0.55
  median_home_value: 125400
  gini_index: 0.5091
  vacancy_rate: 33.69
  race_white: 4309
  race_black: 454
  race_asian: 13
  race_native: 100
  hispanic: 2153
  bachelors_plus: 725
districts:
  - to: "us/states/tx/districts/13"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/senate/28"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/88"
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

# Childress County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 6743 |
| Under 18 | 1364 |
| 18–64 | 4225 |
| 65+ | 1154 |
| Median household income | 58654 |
| Poverty rate | 15.35 |
| Homeownership rate | 71.0 |
| Unemployment rate | 0.55 |
| Median home value | 125400 |
| Gini index | 0.5091 |
| Vacancy rate | 33.69 |
| White | 4309 |
| Black | 454 |
| Asian | 13 |
| Native | 100 |
| Hispanic/Latino | 2153 |
| Bachelor's or higher | 725 |

## Districts

- [TX-13](/us/states/tx/districts/13.md) — 100% (congressional)
- [TX Senate District 28](/us/states/tx/districts/senate/28.md) — 100% (state senate)
- [TX House District 88](/us/states/tx/districts/house/88.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
