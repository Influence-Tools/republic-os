---
type: Jurisdiction
title: "Bear Lake County, ID"
classification: county
fips: "16007"
state: "ID"
demographics:
  population: 6650
  population_under_18: 1820
  population_18_64: 3420
  population_65_plus: 1410
  median_household_income: 75260
  poverty_rate: 7.02
  homeownership_rate: 89.51
  unemployment_rate: 2.62
  median_home_value: 275000
  gini_index: 0.4038
  vacancy_rate: 43.33
  race_white: 6329
  race_black: 33
  race_asian: 14
  race_native: 36
  hispanic: 254
  bachelors_plus: 1195
districts:
  - to: "us/states/id/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/id/districts/senate/35"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, id]
timestamp: "2026-07-03"
---

# Bear Lake County, ID

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 6650 |
| Under 18 | 1820 |
| 18–64 | 3420 |
| 65+ | 1410 |
| Median household income | 75260 |
| Poverty rate | 7.02 |
| Homeownership rate | 89.51 |
| Unemployment rate | 2.62 |
| Median home value | 275000 |
| Gini index | 0.4038 |
| Vacancy rate | 43.33 |
| White | 6329 |
| Black | 33 |
| Asian | 14 |
| Native | 36 |
| Hispanic/Latino | 254 |
| Bachelor's or higher | 1195 |

## Districts

- [ID-02](/us/states/id/districts/02.md) — 100% (congressional)
- [ID Senate District 35](/us/states/id/districts/senate/35.md) — 100% (state senate)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
