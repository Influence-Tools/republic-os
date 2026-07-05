---
type: Jurisdiction
title: "Nez Perce County, ID"
classification: county
fips: "16069"
state: "ID"
demographics:
  population: 42697
  population_under_18: 9063
  population_18_64: 24636
  population_65_plus: 8998
  median_household_income: 72599
  poverty_rate: 12.25
  homeownership_rate: 70.43
  unemployment_rate: 2.59
  median_home_value: 334700
  gini_index: 0.4422
  vacancy_rate: 7.04
  race_white: 37457
  race_black: 83
  race_asian: 368
  race_native: 1889
  hispanic: 1885
  bachelors_plus: 10678
districts:
  - to: "us/states/id/districts/01"
    rel: in-district
    area_weight: 0.9986
  - to: "us/states/id/districts/senate/6"
    rel: in-district
    area_weight: 0.623
  - to: "us/states/id/districts/senate/7"
    rel: in-district
    area_weight: 0.3766
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, id]
timestamp: "2026-07-03"
---

# Nez Perce County, ID

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 42697 |
| Under 18 | 9063 |
| 18–64 | 24636 |
| 65+ | 8998 |
| Median household income | 72599 |
| Poverty rate | 12.25 |
| Homeownership rate | 70.43 |
| Unemployment rate | 2.59 |
| Median home value | 334700 |
| Gini index | 0.4422 |
| Vacancy rate | 7.04 |
| White | 37457 |
| Black | 83 |
| Asian | 368 |
| Native | 1889 |
| Hispanic/Latino | 1885 |
| Bachelor's or higher | 10678 |

## Districts

- [ID-01](/us/states/id/districts/01.md) — 100% (congressional)
- [ID Senate District 6](/us/states/id/districts/senate/6.md) — 62% (state senate)
- [ID Senate District 7](/us/states/id/districts/senate/7.md) — 38% (state senate)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
