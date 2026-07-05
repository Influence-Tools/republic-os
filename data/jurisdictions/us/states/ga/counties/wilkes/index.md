---
type: Jurisdiction
title: "Wilkes County, GA"
classification: county
fips: "13317"
state: "GA"
demographics:
  population: 9549
  population_under_18: 1925
  population_18_64: 5315
  population_65_plus: 2309
  median_household_income: 52043
  poverty_rate: 17.81
  homeownership_rate: 66.08
  unemployment_rate: 1.55
  median_home_value: 122700
  gini_index: 0.5167
  vacancy_rate: 21.34
  race_white: 4938
  race_black: 3773
  race_asian: 117
  race_native: 14
  hispanic: 463
  bachelors_plus: 1541
districts:
  - to: "us/states/ga/districts/12"
    rel: in-district
    area_weight: 0.7216
  - to: "us/states/ga/districts/10"
    rel: in-district
    area_weight: 0.2784
  - to: "us/states/ga/districts/senate/24"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ga/districts/house/123"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Wilkes County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9549 |
| Under 18 | 1925 |
| 18–64 | 5315 |
| 65+ | 2309 |
| Median household income | 52043 |
| Poverty rate | 17.81 |
| Homeownership rate | 66.08 |
| Unemployment rate | 1.55 |
| Median home value | 122700 |
| Gini index | 0.5167 |
| Vacancy rate | 21.34 |
| White | 4938 |
| Black | 3773 |
| Asian | 117 |
| Native | 14 |
| Hispanic/Latino | 463 |
| Bachelor's or higher | 1541 |

## Districts

- [GA-12](/us/states/ga/districts/12.md) — 72% (congressional)
- [GA-10](/us/states/ga/districts/10.md) — 28% (congressional)
- [GA Senate District 24](/us/states/ga/districts/senate/24.md) — 100% (state senate)
- [GA House District 123](/us/states/ga/districts/house/123.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
