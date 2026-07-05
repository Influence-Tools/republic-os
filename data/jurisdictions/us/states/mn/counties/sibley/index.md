---
type: Jurisdiction
title: "Sibley County, MN"
classification: county
fips: "27143"
state: "MN"
demographics:
  population: 15005
  population_under_18: 3390
  population_18_64: 8693
  population_65_plus: 2922
  median_household_income: 77634
  poverty_rate: 9.01
  homeownership_rate: 80.77
  unemployment_rate: 3.78
  median_home_value: 231900
  gini_index: 0.4112
  vacancy_rate: 9.11
  race_white: 13189
  race_black: 179
  race_asian: 61
  race_native: 33
  hispanic: 1390
  bachelors_plus: 2478
districts:
  - to: "us/states/mn/districts/07"
    rel: in-district
    area_weight: 0.9975
  - to: "us/states/mn/districts/senate/17"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mn/districts/house/17b"
    rel: in-district
    area_weight: 0.8096
  - to: "us/states/mn/districts/house/17a"
    rel: in-district
    area_weight: 0.1902
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Sibley County, MN

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 15005 |
| Under 18 | 3390 |
| 18–64 | 8693 |
| 65+ | 2922 |
| Median household income | 77634 |
| Poverty rate | 9.01 |
| Homeownership rate | 80.77 |
| Unemployment rate | 3.78 |
| Median home value | 231900 |
| Gini index | 0.4112 |
| Vacancy rate | 9.11 |
| White | 13189 |
| Black | 179 |
| Asian | 61 |
| Native | 33 |
| Hispanic/Latino | 1390 |
| Bachelor's or higher | 2478 |

## Districts

- [MN-07](/us/states/mn/districts/07.md) — 100% (congressional)
- [MN Senate District 17](/us/states/mn/districts/senate/17.md) — 100% (state senate)
- [MN House District 17B](/us/states/mn/districts/house/17b.md) — 81% (state house)
- [MN House District 17A](/us/states/mn/districts/house/17a.md) — 19% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
