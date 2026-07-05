---
type: Jurisdiction
title: "Angelina County, TX"
classification: county
fips: "48005"
state: "TX"
demographics:
  population: 87275
  population_under_18: 22070
  population_18_64: 50483
  population_65_plus: 14722
  median_household_income: 60960
  poverty_rate: 15.76
  homeownership_rate: 63.99
  unemployment_rate: 6.39
  median_home_value: 163500
  gini_index: 0.4451
  vacancy_rate: 12.84
  race_white: 55368
  race_black: 10591
  race_asian: 825
  race_native: 899
  hispanic: 20528
  bachelors_plus: 14156
districts:
  - to: "us/states/tx/districts/17"
    rel: in-district
    area_weight: 0.9981
  - to: "us/states/tx/districts/senate/3"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/9"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Angelina County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 87275 |
| Under 18 | 22070 |
| 18–64 | 50483 |
| 65+ | 14722 |
| Median household income | 60960 |
| Poverty rate | 15.76 |
| Homeownership rate | 63.99 |
| Unemployment rate | 6.39 |
| Median home value | 163500 |
| Gini index | 0.4451 |
| Vacancy rate | 12.84 |
| White | 55368 |
| Black | 10591 |
| Asian | 825 |
| Native | 899 |
| Hispanic/Latino | 20528 |
| Bachelor's or higher | 14156 |

## Districts

- [TX-17](/us/states/tx/districts/17.md) — 100% (congressional)
- [TX Senate District 3](/us/states/tx/districts/senate/3.md) — 100% (state senate)
- [TX House District 9](/us/states/tx/districts/house/9.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
