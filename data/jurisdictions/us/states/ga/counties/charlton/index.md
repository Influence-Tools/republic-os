---
type: Jurisdiction
title: "Charlton County, GA"
classification: county
fips: "13049"
state: "GA"
demographics:
  population: 12818
  population_under_18: 2545
  population_18_64: 8442
  population_65_plus: 1831
  median_household_income: 61276
  poverty_rate: 18.08
  homeownership_rate: 80.14
  unemployment_rate: 13.96
  median_home_value: 142800
  gini_index: 0.4649
  vacancy_rate: 11.36
  race_white: 7088
  race_black: 3183
  race_asian: 135
  race_native: 45
  hispanic: 1980
  bachelors_plus: 1294
districts:
  - to: "us/states/ga/districts/01"
    rel: in-district
    area_weight: 0.9979
  - to: "us/states/ga/districts/senate/3"
    rel: in-district
    area_weight: 0.9986
  - to: "us/states/ga/districts/house/174"
    rel: in-district
    area_weight: 0.9985
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Charlton County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 12818 |
| Under 18 | 2545 |
| 18–64 | 8442 |
| 65+ | 1831 |
| Median household income | 61276 |
| Poverty rate | 18.08 |
| Homeownership rate | 80.14 |
| Unemployment rate | 13.96 |
| Median home value | 142800 |
| Gini index | 0.4649 |
| Vacancy rate | 11.36 |
| White | 7088 |
| Black | 3183 |
| Asian | 135 |
| Native | 45 |
| Hispanic/Latino | 1980 |
| Bachelor's or higher | 1294 |

## Districts

- [GA-01](/us/states/ga/districts/01.md) — 100% (congressional)
- [GA Senate District 3](/us/states/ga/districts/senate/3.md) — 100% (state senate)
- [GA House District 174](/us/states/ga/districts/house/174.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
