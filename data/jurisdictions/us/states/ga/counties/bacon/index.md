---
type: Jurisdiction
title: "Bacon County, GA"
classification: county
fips: "13005"
state: "GA"
demographics:
  population: 11109
  population_under_18: 2793
  population_18_64: 6333
  population_65_plus: 1983
  median_household_income: 44694
  poverty_rate: 24.47
  homeownership_rate: 68.65
  unemployment_rate: 2.64
  median_home_value: 101400
  gini_index: 0.4982
  vacancy_rate: 12.98
  race_white: 8139
  race_black: 1487
  race_asian: 96
  race_native: 29
  hispanic: 944
  bachelors_plus: 1133
districts:
  - to: "us/states/ga/districts/01"
    rel: in-district
    area_weight: 0.998
  - to: "us/states/ga/districts/senate/19"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ga/districts/house/178"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Bacon County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 11109 |
| Under 18 | 2793 |
| 18–64 | 6333 |
| 65+ | 1983 |
| Median household income | 44694 |
| Poverty rate | 24.47 |
| Homeownership rate | 68.65 |
| Unemployment rate | 2.64 |
| Median home value | 101400 |
| Gini index | 0.4982 |
| Vacancy rate | 12.98 |
| White | 8139 |
| Black | 1487 |
| Asian | 96 |
| Native | 29 |
| Hispanic/Latino | 944 |
| Bachelor's or higher | 1133 |

## Districts

- [GA-01](/us/states/ga/districts/01.md) — 100% (congressional)
- [GA Senate District 19](/us/states/ga/districts/senate/19.md) — 100% (state senate)
- [GA House District 178](/us/states/ga/districts/house/178.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
