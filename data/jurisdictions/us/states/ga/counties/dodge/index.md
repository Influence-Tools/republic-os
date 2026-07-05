---
type: Jurisdiction
title: "Dodge County, GA"
classification: county
fips: "13091"
state: "GA"
demographics:
  population: 19805
  population_under_18: 3707
  population_18_64: 12178
  population_65_plus: 3920
  median_household_income: 51587
  poverty_rate: 21.55
  homeownership_rate: 70.56
  unemployment_rate: 6.08
  median_home_value: 118100
  gini_index: 0.4364
  vacancy_rate: 19.87
  race_white: 12758
  race_black: 6133
  race_asian: 9
  race_native: 72
  hispanic: 716
  bachelors_plus: 3544
districts:
  - to: "us/states/ga/districts/08"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ga/districts/senate/20"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ga/districts/house/133"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Dodge County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 19805 |
| Under 18 | 3707 |
| 18–64 | 12178 |
| 65+ | 3920 |
| Median household income | 51587 |
| Poverty rate | 21.55 |
| Homeownership rate | 70.56 |
| Unemployment rate | 6.08 |
| Median home value | 118100 |
| Gini index | 0.4364 |
| Vacancy rate | 19.87 |
| White | 12758 |
| Black | 6133 |
| Asian | 9 |
| Native | 72 |
| Hispanic/Latino | 716 |
| Bachelor's or higher | 3544 |

## Districts

- [GA-08](/us/states/ga/districts/08.md) — 100% (congressional)
- [GA Senate District 20](/us/states/ga/districts/senate/20.md) — 100% (state senate)
- [GA House District 133](/us/states/ga/districts/house/133.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
