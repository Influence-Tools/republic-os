---
type: Jurisdiction
title: "Northampton County, NC"
classification: county
fips: "37131"
state: "NC"
demographics:
  population: 16931
  population_under_18: 2998
  population_18_64: 8920
  population_65_plus: 5013
  median_household_income: 50086
  poverty_rate: 21.11
  homeownership_rate: 74.58
  unemployment_rate: 8.11
  median_home_value: 114500
  gini_index: 0.487
  vacancy_rate: 26.16
  race_white: 6771
  race_black: 9293
  race_asian: 5
  race_native: 50
  hispanic: 407
  bachelors_plus: 3180
districts:
  - to: "us/states/nc/districts/01"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/nc/districts/senate/1"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/nc/districts/house/27"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Northampton County, NC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 16931 |
| Under 18 | 2998 |
| 18–64 | 8920 |
| 65+ | 5013 |
| Median household income | 50086 |
| Poverty rate | 21.11 |
| Homeownership rate | 74.58 |
| Unemployment rate | 8.11 |
| Median home value | 114500 |
| Gini index | 0.487 |
| Vacancy rate | 26.16 |
| White | 6771 |
| Black | 9293 |
| Asian | 5 |
| Native | 50 |
| Hispanic/Latino | 407 |
| Bachelor's or higher | 3180 |

## Districts

- [NC-01](/us/states/nc/districts/01.md) — 100% (congressional)
- [NC Senate District 1](/us/states/nc/districts/senate/1.md) — 100% (state senate)
- [NC House District 27](/us/states/nc/districts/house/27.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
