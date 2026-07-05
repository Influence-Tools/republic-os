---
type: Jurisdiction
title: "Spalding County, GA"
classification: county
fips: "13255"
state: "GA"
demographics:
  population: 68892
  population_under_18: 16132
  population_18_64: 39599
  population_65_plus: 13161
  median_household_income: 62071
  poverty_rate: 18.94
  homeownership_rate: 62.75
  unemployment_rate: 7.3
  median_home_value: 228700
  gini_index: 0.5437
  vacancy_rate: 7.81
  race_white: 38004
  race_black: 24680
  race_asian: 663
  race_native: 77
  hispanic: 4229
  bachelors_plus: 11797
districts:
  - to: "us/states/ga/districts/03"
    rel: in-district
    area_weight: 0.9982
  - to: "us/states/ga/districts/senate/16"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ga/districts/house/82"
    rel: in-district
    area_weight: 0.6466
  - to: "us/states/ga/districts/house/135"
    rel: in-district
    area_weight: 0.3531
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Spalding County, GA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 68892 |
| Under 18 | 16132 |
| 18–64 | 39599 |
| 65+ | 13161 |
| Median household income | 62071 |
| Poverty rate | 18.94 |
| Homeownership rate | 62.75 |
| Unemployment rate | 7.3 |
| Median home value | 228700 |
| Gini index | 0.5437 |
| Vacancy rate | 7.81 |
| White | 38004 |
| Black | 24680 |
| Asian | 663 |
| Native | 77 |
| Hispanic/Latino | 4229 |
| Bachelor's or higher | 11797 |

## Districts

- [GA-03](/us/states/ga/districts/03.md) — 100% (congressional)
- [GA Senate District 16](/us/states/ga/districts/senate/16.md) — 100% (state senate)
- [GA House District 82](/us/states/ga/districts/house/82.md) — 65% (state house)
- [GA House District 135](/us/states/ga/districts/house/135.md) — 35% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
