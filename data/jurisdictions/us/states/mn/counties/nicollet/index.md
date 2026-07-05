---
type: Jurisdiction
title: "Nicollet County, MN"
classification: county
fips: "27103"
state: "MN"
demographics:
  population: 34411
  population_under_18: 7382
  population_18_64: 20986
  population_65_plus: 6043
  median_household_income: 79756
  poverty_rate: 8.01
  homeownership_rate: 72.21
  unemployment_rate: 2.17
  median_home_value: 270300
  gini_index: 0.4625
  vacancy_rate: 4.37
  race_white: 29832
  race_black: 1586
  race_asian: 566
  race_native: 145
  hispanic: 1871
  bachelors_plus: 10725
districts:
  - to: "us/states/mn/districts/01"
    rel: in-district
    area_weight: 0.9976
  - to: "us/states/mn/districts/senate/18"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/mn/districts/house/18a"
    rel: in-district
    area_weight: 0.9993
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Nicollet County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 34411 |
| Under 18 | 7382 |
| 18–64 | 20986 |
| 65+ | 6043 |
| Median household income | 79756 |
| Poverty rate | 8.01 |
| Homeownership rate | 72.21 |
| Unemployment rate | 2.17 |
| Median home value | 270300 |
| Gini index | 0.4625 |
| Vacancy rate | 4.37 |
| White | 29832 |
| Black | 1586 |
| Asian | 566 |
| Native | 145 |
| Hispanic/Latino | 1871 |
| Bachelor's or higher | 10725 |

## Districts

- [MN-01](/us/states/mn/districts/01.md) — 100% (congressional)
- [MN Senate District 18](/us/states/mn/districts/senate/18.md) — 100% (state senate)
- [MN House District 18A](/us/states/mn/districts/house/18a.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
