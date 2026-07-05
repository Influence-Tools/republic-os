---
type: Jurisdiction
title: "Traverse County, MN"
classification: county
fips: "27155"
state: "MN"
demographics:
  population: 3243
  population_under_18: 702
  population_18_64: 1716
  population_65_plus: 825
  median_household_income: 62989
  poverty_rate: 11.33
  homeownership_rate: 81.85
  unemployment_rate: 4.55
  median_home_value: 114100
  gini_index: 0.4619
  vacancy_rate: 30.85
  race_white: 2813
  race_black: 20
  race_asian: 4
  race_native: 170
  hispanic: 199
  bachelors_plus: 442
districts:
  - to: "us/states/mn/districts/07"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/mn/districts/senate/9"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/mn/districts/house/9a"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Traverse County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3243 |
| Under 18 | 702 |
| 18–64 | 1716 |
| 65+ | 825 |
| Median household income | 62989 |
| Poverty rate | 11.33 |
| Homeownership rate | 81.85 |
| Unemployment rate | 4.55 |
| Median home value | 114100 |
| Gini index | 0.4619 |
| Vacancy rate | 30.85 |
| White | 2813 |
| Black | 20 |
| Asian | 4 |
| Native | 170 |
| Hispanic/Latino | 199 |
| Bachelor's or higher | 442 |

## Districts

- [MN-07](/us/states/mn/districts/07.md) — 100% (congressional)
- [MN Senate District 9](/us/states/mn/districts/senate/9.md) — 100% (state senate)
- [MN House District 9A](/us/states/mn/districts/house/9a.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
