---
type: Jurisdiction
title: "Randolph County, MO"
classification: county
fips: "29175"
state: "MO"
demographics:
  population: 24365
  population_under_18: 5392
  population_18_64: 14657
  population_65_plus: 4316
  median_household_income: 53033
  poverty_rate: 13.88
  homeownership_rate: 71.39
  unemployment_rate: 4.39
  median_home_value: 159300
  gini_index: 0.4286
  vacancy_rate: 14.87
  race_white: 21611
  race_black: 1203
  race_asian: 50
  race_native: 16
  hispanic: 612
  bachelors_plus: 4024
districts:
  - to: "us/states/mo/districts/06"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mo/districts/senate/18"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/house/6"
    rel: in-district
    area_weight: 0.6521
  - to: "us/states/mo/districts/house/48"
    rel: in-district
    area_weight: 0.3478
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Randolph County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 24365 |
| Under 18 | 5392 |
| 18–64 | 14657 |
| 65+ | 4316 |
| Median household income | 53033 |
| Poverty rate | 13.88 |
| Homeownership rate | 71.39 |
| Unemployment rate | 4.39 |
| Median home value | 159300 |
| Gini index | 0.4286 |
| Vacancy rate | 14.87 |
| White | 21611 |
| Black | 1203 |
| Asian | 50 |
| Native | 16 |
| Hispanic/Latino | 612 |
| Bachelor's or higher | 4024 |

## Districts

- [MO-06](/us/states/mo/districts/06.md) — 100% (congressional)
- [MO Senate District 18](/us/states/mo/districts/senate/18.md) — 100% (state senate)
- [MO House District 6](/us/states/mo/districts/house/6.md) — 65% (state house)
- [MO House District 48](/us/states/mo/districts/house/48.md) — 35% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
