---
type: Jurisdiction
title: "Blaine County, ID"
classification: county
fips: "16013"
state: "ID"
demographics:
  population: 24951
  population_under_18: 4781
  population_18_64: 14505
  population_65_plus: 5665
  median_household_income: 92566
  poverty_rate: 6.64
  homeownership_rate: 73.54
  unemployment_rate: 2.06
  median_home_value: 735300
  gini_index: 0.4844
  vacancy_rate: 34.87
  race_white: 19398
  race_black: 97
  race_asian: 147
  race_native: 332
  hispanic: 5451
  bachelors_plus: 11126
districts:
  - to: "us/states/id/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/id/districts/senate/26"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, id]
timestamp: "2026-07-03"
---

# Blaine County, ID

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 24951 |
| Under 18 | 4781 |
| 18–64 | 14505 |
| 65+ | 5665 |
| Median household income | 92566 |
| Poverty rate | 6.64 |
| Homeownership rate | 73.54 |
| Unemployment rate | 2.06 |
| Median home value | 735300 |
| Gini index | 0.4844 |
| Vacancy rate | 34.87 |
| White | 19398 |
| Black | 97 |
| Asian | 147 |
| Native | 332 |
| Hispanic/Latino | 5451 |
| Bachelor's or higher | 11126 |

## Districts

- [ID-02](/us/states/id/districts/02.md) — 100% (congressional)
- [ID Senate District 26](/us/states/id/districts/senate/26.md) — 100% (state senate)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
