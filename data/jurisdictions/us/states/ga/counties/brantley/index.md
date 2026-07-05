---
type: Jurisdiction
title: "Brantley County, GA"
classification: county
fips: "13025"
state: "GA"
demographics:
  population: 18315
  population_under_18: 3834
  population_18_64: 11301
  population_65_plus: 3180
  median_household_income: 58239
  poverty_rate: 17.08
  homeownership_rate: 79.89
  unemployment_rate: 2.8
  median_home_value: 99600
  gini_index: 0.4349
  vacancy_rate: 20.47
  race_white: 16637
  race_black: 586
  race_asian: 97
  race_native: 0
  hispanic: 572
  bachelors_plus: 2652
districts:
  - to: "us/states/ga/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ga/districts/senate/3"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ga/districts/house/174"
    rel: in-district
    area_weight: 0.9994
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Brantley County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 18315 |
| Under 18 | 3834 |
| 18–64 | 11301 |
| 65+ | 3180 |
| Median household income | 58239 |
| Poverty rate | 17.08 |
| Homeownership rate | 79.89 |
| Unemployment rate | 2.8 |
| Median home value | 99600 |
| Gini index | 0.4349 |
| Vacancy rate | 20.47 |
| White | 16637 |
| Black | 586 |
| Asian | 97 |
| Native | 0 |
| Hispanic/Latino | 572 |
| Bachelor's or higher | 2652 |

## Districts

- [GA-01](/us/states/ga/districts/01.md) — 100% (congressional)
- [GA Senate District 3](/us/states/ga/districts/senate/3.md) — 100% (state senate)
- [GA House District 174](/us/states/ga/districts/house/174.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
