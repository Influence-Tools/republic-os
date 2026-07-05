---
type: Jurisdiction
title: "Butte County, CA"
classification: county
fips: "06007"
state: "CA"
demographics:
  population: 207929
  population_under_18: 42452
  population_18_64: 127250
  population_65_plus: 38227
  median_household_income: 67928
  poverty_rate: 19.25
  homeownership_rate: 57.28
  unemployment_rate: 7.46
  median_home_value: 424700
  gini_index: 0.4833
  vacancy_rate: 10.24
  race_white: 144544
  race_black: 3823
  race_asian: 11629
  race_native: 2789
  hispanic: 41660
  bachelors_plus: 58578
districts:
  - to: "us/states/ca/districts/01"
    rel: in-district
    area_weight: 0.9976
  - to: "us/states/ca/districts/senate/1"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ca/districts/house/3"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ca]
timestamp: "2026-07-03"
---

# Butte County, CA

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 207929 |
| Under 18 | 42452 |
| 18–64 | 127250 |
| 65+ | 38227 |
| Median household income | 67928 |
| Poverty rate | 19.25 |
| Homeownership rate | 57.28 |
| Unemployment rate | 7.46 |
| Median home value | 424700 |
| Gini index | 0.4833 |
| Vacancy rate | 10.24 |
| White | 144544 |
| Black | 3823 |
| Asian | 11629 |
| Native | 2789 |
| Hispanic/Latino | 41660 |
| Bachelor's or higher | 58578 |

## Districts

- [CA-01](/us/states/ca/districts/01.md) — 100% (congressional)
- [CA Senate District 1](/us/states/ca/districts/senate/1.md) — 100% (state senate)
- [CA House District 3](/us/states/ca/districts/house/3.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
