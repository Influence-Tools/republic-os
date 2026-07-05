---
type: Jurisdiction
title: "Meagher County, MT"
classification: county
fips: "30059"
state: "MT"
demographics:
  population: 2007
  population_under_18: 246
  population_18_64: 1064
  population_65_plus: 697
  median_household_income: 71932
  poverty_rate: 12.35
  homeownership_rate: 75.4
  unemployment_rate: 0.27
  median_home_value: 259800
  gini_index: 0.4366
  vacancy_rate: 36.07
  race_white: 1921
  race_black: 15
  race_asian: 0
  race_native: 29
  hispanic: 65
  bachelors_plus: 563
districts:
  - to: "us/states/mt/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mt/districts/senate/39"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mt/districts/house/78"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mt]
timestamp: "2026-07-03"
---

# Meagher County, MT

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2007 |
| Under 18 | 246 |
| 18–64 | 1064 |
| 65+ | 697 |
| Median household income | 71932 |
| Poverty rate | 12.35 |
| Homeownership rate | 75.4 |
| Unemployment rate | 0.27 |
| Median home value | 259800 |
| Gini index | 0.4366 |
| Vacancy rate | 36.07 |
| White | 1921 |
| Black | 15 |
| Asian | 0 |
| Native | 29 |
| Hispanic/Latino | 65 |
| Bachelor's or higher | 563 |

## Districts

- [MT-02](/us/states/mt/districts/02.md) — 100% (congressional)
- [MT Senate District 39](/us/states/mt/districts/senate/39.md) — 100% (state senate)
- [MT House District 78](/us/states/mt/districts/house/78.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
