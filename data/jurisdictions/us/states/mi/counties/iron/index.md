---
type: Jurisdiction
title: "Iron County, MI"
classification: county
fips: "26071"
state: "MI"
demographics:
  population: 11667
  population_under_18: 2044
  population_18_64: 5961
  population_65_plus: 3662
  median_household_income: 55940
  poverty_rate: 16.99
  homeownership_rate: 84.5
  unemployment_rate: 5.35
  median_home_value: 109100
  gini_index: 0.4557
  vacancy_rate: 39.42
  race_white: 10646
  race_black: 110
  race_asian: 69
  race_native: 101
  hispanic: 268
  bachelors_plus: 2675
districts:
  - to: "us/states/mi/districts/01"
    rel: in-district
    area_weight: 0.9982
  - to: "us/states/mi/districts/senate/38"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mi/districts/house/110"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Iron County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 11667 |
| Under 18 | 2044 |
| 18–64 | 5961 |
| 65+ | 3662 |
| Median household income | 55940 |
| Poverty rate | 16.99 |
| Homeownership rate | 84.5 |
| Unemployment rate | 5.35 |
| Median home value | 109100 |
| Gini index | 0.4557 |
| Vacancy rate | 39.42 |
| White | 10646 |
| Black | 110 |
| Asian | 69 |
| Native | 101 |
| Hispanic/Latino | 268 |
| Bachelor's or higher | 2675 |

## Districts

- [MI-01](/us/states/mi/districts/01.md) — 100% (congressional)
- [MI Senate District 38](/us/states/mi/districts/senate/38.md) — 100% (state senate)
- [MI House District 110](/us/states/mi/districts/house/110.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
