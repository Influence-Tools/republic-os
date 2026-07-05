---
type: Jurisdiction
title: "Polk County, GA"
classification: county
fips: "13233"
state: "GA"
demographics:
  population: 43785
  population_under_18: 10991
  population_18_64: 26058
  population_65_plus: 6736
  median_household_income: 58515
  poverty_rate: 16.35
  homeownership_rate: 66.03
  unemployment_rate: 5.9
  median_home_value: 187600
  gini_index: 0.4361
  vacancy_rate: 8.45
  race_white: 31770
  race_black: 5214
  race_asian: 301
  race_native: 312
  hispanic: 6087
  bachelors_plus: 6145
districts:
  - to: "us/states/ga/districts/14"
    rel: in-district
    area_weight: 0.9989
  - to: "us/states/ga/districts/senate/31"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ga/districts/house/16"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Polk County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 43785 |
| Under 18 | 10991 |
| 18–64 | 26058 |
| 65+ | 6736 |
| Median household income | 58515 |
| Poverty rate | 16.35 |
| Homeownership rate | 66.03 |
| Unemployment rate | 5.9 |
| Median home value | 187600 |
| Gini index | 0.4361 |
| Vacancy rate | 8.45 |
| White | 31770 |
| Black | 5214 |
| Asian | 301 |
| Native | 312 |
| Hispanic/Latino | 6087 |
| Bachelor's or higher | 6145 |

## Districts

- [GA-14](/us/states/ga/districts/14.md) — 100% (congressional)
- [GA Senate District 31](/us/states/ga/districts/senate/31.md) — 100% (state senate)
- [GA House District 16](/us/states/ga/districts/house/16.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
