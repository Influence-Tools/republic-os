---
type: Jurisdiction
title: "Houghton County, MI"
classification: county
fips: "26061"
state: "MI"
demographics:
  population: 37693
  population_under_18: 7459
  population_18_64: 23459
  population_65_plus: 6775
  median_household_income: 58899
  poverty_rate: 16.5
  homeownership_rate: 71.8
  unemployment_rate: 5.71
  median_home_value: 159900
  gini_index: 0.4644
  vacancy_rate: 24.19
  race_white: 34481
  race_black: 444
  race_asian: 1084
  race_native: 187
  hispanic: 697
  bachelors_plus: 11806
districts:
  - to: "us/states/mi/districts/01"
    rel: in-district
    area_weight: 0.693
  - to: "us/states/mi/districts/senate/38"
    rel: in-district
    area_weight: 0.6923
  - to: "us/states/mi/districts/house/110"
    rel: in-district
    area_weight: 0.6922
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Houghton County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 37693 |
| Under 18 | 7459 |
| 18–64 | 23459 |
| 65+ | 6775 |
| Median household income | 58899 |
| Poverty rate | 16.5 |
| Homeownership rate | 71.8 |
| Unemployment rate | 5.71 |
| Median home value | 159900 |
| Gini index | 0.4644 |
| Vacancy rate | 24.19 |
| White | 34481 |
| Black | 444 |
| Asian | 1084 |
| Native | 187 |
| Hispanic/Latino | 697 |
| Bachelor's or higher | 11806 |

## Districts

- [MI-01](/us/states/mi/districts/01.md) — 69% (congressional)
- [MI Senate District 38](/us/states/mi/districts/senate/38.md) — 69% (state senate)
- [MI House District 110](/us/states/mi/districts/house/110.md) — 69% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
