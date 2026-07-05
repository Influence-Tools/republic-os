---
type: Jurisdiction
title: "Essex County, MA"
classification: county
fips: "25009"
state: "MA"
demographics:
  population: 813054
  population_under_18: 169485
  population_18_64: 493463
  population_65_plus: 150106
  median_household_income: 101883
  poverty_rate: 9.37
  homeownership_rate: 63.5
  unemployment_rate: 5.11
  median_home_value: 619100
  gini_index: 0.4819
  vacancy_rate: 5.04
  race_white: 551107
  race_black: 32753
  race_asian: 29493
  race_native: 2429
  hispanic: 195593
  bachelors_plus: 348582
districts:
  - to: "us/states/ma/districts/06"
    rel: in-district
    area_weight: 0.5662
  - to: "us/states/ma/districts/03"
    rel: in-district
    area_weight: 0.0799
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ma]
timestamp: "2026-07-03"
---

# Essex County, MA

County jurisdiction — 8 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 813054 |
| Under 18 | 169485 |
| 18–64 | 493463 |
| 65+ | 150106 |
| Median household income | 101883 |
| Poverty rate | 9.37 |
| Homeownership rate | 63.5 |
| Unemployment rate | 5.11 |
| Median home value | 619100 |
| Gini index | 0.4819 |
| Vacancy rate | 5.04 |
| White | 551107 |
| Black | 32753 |
| Asian | 29493 |
| Native | 2429 |
| Hispanic/Latino | 195593 |
| Bachelor's or higher | 348582 |

## Districts

- [MA-06](/us/states/ma/districts/06.md) — 57% (congressional)
- [MA-03](/us/states/ma/districts/03.md) — 8% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
