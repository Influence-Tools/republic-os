---
type: Jurisdiction
title: "Matagorda County, TX"
classification: county
fips: "48321"
state: "TX"
demographics:
  population: 36329
  population_under_18: 9284
  population_18_64: 20438
  population_65_plus: 6607
  median_household_income: 58628
  poverty_rate: 20.73
  homeownership_rate: 68.11
  unemployment_rate: 8.68
  median_home_value: 172900
  gini_index: 0.4653
  vacancy_rate: 18.99
  race_white: 19089
  race_black: 3750
  race_asian: 650
  race_native: 128
  hispanic: 15889
  bachelors_plus: 7321
districts:
  - to: "us/states/tx/districts/22"
    rel: in-district
    area_weight: 0.857
  - to: "us/states/tx/districts/senate/17"
    rel: in-district
    area_weight: 0.8576
  - to: "us/states/tx/districts/house/30"
    rel: in-district
    area_weight: 0.8575
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Matagorda County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 36329 |
| Under 18 | 9284 |
| 18–64 | 20438 |
| 65+ | 6607 |
| Median household income | 58628 |
| Poverty rate | 20.73 |
| Homeownership rate | 68.11 |
| Unemployment rate | 8.68 |
| Median home value | 172900 |
| Gini index | 0.4653 |
| Vacancy rate | 18.99 |
| White | 19089 |
| Black | 3750 |
| Asian | 650 |
| Native | 128 |
| Hispanic/Latino | 15889 |
| Bachelor's or higher | 7321 |

## Districts

- [TX-22](/us/states/tx/districts/22.md) — 86% (congressional)
- [TX Senate District 17](/us/states/tx/districts/senate/17.md) — 86% (state senate)
- [TX House District 30](/us/states/tx/districts/house/30.md) — 86% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
