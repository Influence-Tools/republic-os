---
type: Jurisdiction
title: "Modoc County, CA"
classification: county
fips: "06049"
state: "CA"
demographics:
  population: 8600
  population_under_18: 1639
  population_18_64: 4239
  population_65_plus: 2722
  median_household_income: 59455
  poverty_rate: 17.9
  homeownership_rate: 77.44
  unemployment_rate: 7.6
  median_home_value: 224700
  gini_index: 0.4466
  vacancy_rate: 31.42
  race_white: 6766
  race_black: 49
  race_asian: 177
  race_native: 174
  hispanic: 1348
  bachelors_plus: 2036
districts:
  - to: "us/states/ca/districts/01"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ca/districts/senate/1"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ca/districts/house/1"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ca]
timestamp: "2026-07-03"
---

# Modoc County, CA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8600 |
| Under 18 | 1639 |
| 18–64 | 4239 |
| 65+ | 2722 |
| Median household income | 59455 |
| Poverty rate | 17.9 |
| Homeownership rate | 77.44 |
| Unemployment rate | 7.6 |
| Median home value | 224700 |
| Gini index | 0.4466 |
| Vacancy rate | 31.42 |
| White | 6766 |
| Black | 49 |
| Asian | 177 |
| Native | 174 |
| Hispanic/Latino | 1348 |
| Bachelor's or higher | 2036 |

## Districts

- [CA-01](/us/states/ca/districts/01.md) — 100% (congressional)
- [CA Senate District 1](/us/states/ca/districts/senate/1.md) — 100% (state senate)
- [CA House District 1](/us/states/ca/districts/house/1.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
