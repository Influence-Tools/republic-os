---
type: Jurisdiction
title: "Mille Lacs County, MN"
classification: county
fips: "27095"
state: "MN"
demographics:
  population: 27125
  population_under_18: 6279
  population_18_64: 15810
  population_65_plus: 5036
  median_household_income: 72729
  poverty_rate: 10.38
  homeownership_rate: 77.86
  unemployment_rate: 3.97
  median_home_value: 258300
  gini_index: 0.4163
  vacancy_rate: 18.34
  race_white: 24099
  race_black: 123
  race_asian: 257
  race_native: 1196
  hispanic: 625
  bachelors_plus: 4456
districts:
  - to: "us/states/mn/districts/08"
    rel: in-district
    area_weight: 0.9992
  - to: "us/states/mn/districts/senate/10"
    rel: in-district
    area_weight: 0.8927
  - to: "us/states/mn/districts/senate/27"
    rel: in-district
    area_weight: 0.1073
  - to: "us/states/mn/districts/house/10a"
    rel: in-district
    area_weight: 0.5318
  - to: "us/states/mn/districts/house/10b"
    rel: in-district
    area_weight: 0.3609
  - to: "us/states/mn/districts/house/27b"
    rel: in-district
    area_weight: 0.1073
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Mille Lacs County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 27125 |
| Under 18 | 6279 |
| 18–64 | 15810 |
| 65+ | 5036 |
| Median household income | 72729 |
| Poverty rate | 10.38 |
| Homeownership rate | 77.86 |
| Unemployment rate | 3.97 |
| Median home value | 258300 |
| Gini index | 0.4163 |
| Vacancy rate | 18.34 |
| White | 24099 |
| Black | 123 |
| Asian | 257 |
| Native | 1196 |
| Hispanic/Latino | 625 |
| Bachelor's or higher | 4456 |

## Districts

- [MN-08](/us/states/mn/districts/08.md) — 100% (congressional)
- [MN Senate District 10](/us/states/mn/districts/senate/10.md) — 89% (state senate)
- [MN Senate District 27](/us/states/mn/districts/senate/27.md) — 11% (state senate)
- [MN House District 10A](/us/states/mn/districts/house/10a.md) — 53% (state house)
- [MN House District 10B](/us/states/mn/districts/house/10b.md) — 36% (state house)
- [MN House District 27B](/us/states/mn/districts/house/27b.md) — 11% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
