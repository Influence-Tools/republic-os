---
type: Jurisdiction
title: "Quitman County, GA"
classification: county
fips: "13239"
state: "GA"
demographics:
  population: 2264
  population_under_18: 317
  population_18_64: 1105
  population_65_plus: 842
  median_household_income: 40179
  poverty_rate: 15.68
  homeownership_rate: 84.25
  unemployment_rate: 28.63
  median_home_value: 104600
  gini_index: 0.4732
  vacancy_rate: 39.62
  race_white: 970
  race_black: 1189
  race_asian: 0
  race_native: 0
  hispanic: 19
  bachelors_plus: 277
districts:
  - to: "us/states/ga/districts/02"
    rel: in-district
    area_weight: 0.9914
  - to: "us/states/al/districts/02"
    rel: in-district
    area_weight: 0.0086
  - to: "us/states/ga/districts/house/154"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Quitman County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2264 |
| Under 18 | 317 |
| 18–64 | 1105 |
| 65+ | 842 |
| Median household income | 40179 |
| Poverty rate | 15.68 |
| Homeownership rate | 84.25 |
| Unemployment rate | 28.63 |
| Median home value | 104600 |
| Gini index | 0.4732 |
| Vacancy rate | 39.62 |
| White | 970 |
| Black | 1189 |
| Asian | 0 |
| Native | 0 |
| Hispanic/Latino | 19 |
| Bachelor's or higher | 277 |

## Districts

- [GA-02](/us/states/ga/districts/02.md) — 99% (congressional)
- [AL-02](/us/states/al/districts/02.md) — 1% (congressional)
- [GA House District 154](/us/states/ga/districts/house/154.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
