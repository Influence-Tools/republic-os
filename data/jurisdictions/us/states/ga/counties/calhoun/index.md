---
type: Jurisdiction
title: "Calhoun County, GA"
classification: county
fips: "13037"
state: "GA"
demographics:
  population: 5498
  population_under_18: 840
  population_18_64: 3706
  population_65_plus: 952
  median_household_income: 46940
  poverty_rate: 22.83
  homeownership_rate: 59.45
  unemployment_rate: 5.99
  median_home_value: 81000
  gini_index: 0.5496
  vacancy_rate: 21.53
  race_white: 1878
  race_black: 3209
  race_asian: 24
  race_native: 12
  hispanic: 303
  bachelors_plus: 794
districts:
  - to: "us/states/ga/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ga/districts/house/154"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Calhoun County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5498 |
| Under 18 | 840 |
| 18–64 | 3706 |
| 65+ | 952 |
| Median household income | 46940 |
| Poverty rate | 22.83 |
| Homeownership rate | 59.45 |
| Unemployment rate | 5.99 |
| Median home value | 81000 |
| Gini index | 0.5496 |
| Vacancy rate | 21.53 |
| White | 1878 |
| Black | 3209 |
| Asian | 24 |
| Native | 12 |
| Hispanic/Latino | 303 |
| Bachelor's or higher | 794 |

## Districts

- [GA-02](/us/states/ga/districts/02.md) — 100% (congressional)
- [GA House District 154](/us/states/ga/districts/house/154.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
