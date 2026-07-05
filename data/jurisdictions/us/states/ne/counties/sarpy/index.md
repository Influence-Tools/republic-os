---
type: Jurisdiction
title: "Sarpy County, NE"
classification: county
fips: "31153"
state: "NE"
demographics:
  population: 197389
  population_under_18: 51948
  population_18_64: 120102
  population_65_plus: 25339
  median_household_income: 103321
  poverty_rate: 5.57
  homeownership_rate: 70.35
  unemployment_rate: 2.61
  median_home_value: 314100
  gini_index: 0.399
  vacancy_rate: 3.49
  race_white: 156792
  race_black: 8171
  race_asian: 5476
  race_native: 899
  hispanic: 22804
  bachelors_plus: 74989
districts:
  - to: "us/states/ne/districts/02"
    rel: in-district
    area_weight: 0.6031
  - to: "us/states/ne/districts/01"
    rel: in-district
    area_weight: 0.3964
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ne]
timestamp: "2026-07-03"
---

# Sarpy County, NE

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 197389 |
| Under 18 | 51948 |
| 18–64 | 120102 |
| 65+ | 25339 |
| Median household income | 103321 |
| Poverty rate | 5.57 |
| Homeownership rate | 70.35 |
| Unemployment rate | 2.61 |
| Median home value | 314100 |
| Gini index | 0.399 |
| Vacancy rate | 3.49 |
| White | 156792 |
| Black | 8171 |
| Asian | 5476 |
| Native | 899 |
| Hispanic/Latino | 22804 |
| Bachelor's or higher | 74989 |

## Districts

- [NE-02](/us/states/ne/districts/02.md) — 60% (congressional)
- [NE-01](/us/states/ne/districts/01.md) — 40% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
