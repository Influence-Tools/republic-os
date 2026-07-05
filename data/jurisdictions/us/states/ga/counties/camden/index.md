---
type: Jurisdiction
title: "Camden County, GA"
classification: county
fips: "13039"
state: "GA"
demographics:
  population: 56970
  population_under_18: 13714
  population_18_64: 34517
  population_65_plus: 8739
  median_household_income: 74378
  poverty_rate: 12.87
  homeownership_rate: 67.79
  unemployment_rate: 5.38
  median_home_value: 261400
  gini_index: 0.3927
  vacancy_rate: 8.36
  race_white: 39791
  race_black: 9542
  race_asian: 1036
  race_native: 102
  hispanic: 4325
  bachelors_plus: 12490
districts:
  - to: "us/states/ga/districts/01"
    rel: in-district
    area_weight: 0.8744
  - to: "us/states/ga/districts/senate/3"
    rel: in-district
    area_weight: 0.8766
  - to: "us/states/ga/districts/house/180"
    rel: in-district
    area_weight: 0.8765
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Camden County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 56970 |
| Under 18 | 13714 |
| 18–64 | 34517 |
| 65+ | 8739 |
| Median household income | 74378 |
| Poverty rate | 12.87 |
| Homeownership rate | 67.79 |
| Unemployment rate | 5.38 |
| Median home value | 261400 |
| Gini index | 0.3927 |
| Vacancy rate | 8.36 |
| White | 39791 |
| Black | 9542 |
| Asian | 1036 |
| Native | 102 |
| Hispanic/Latino | 4325 |
| Bachelor's or higher | 12490 |

## Districts

- [GA-01](/us/states/ga/districts/01.md) — 87% (congressional)
- [GA Senate District 3](/us/states/ga/districts/senate/3.md) — 88% (state senate)
- [GA House District 180](/us/states/ga/districts/house/180.md) — 88% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
