---
type: Jurisdiction
title: "Tattnall County, GA"
classification: county
fips: "13267"
state: "GA"
demographics:
  population: 24208
  population_under_18: 4872
  population_18_64: 15600
  population_65_plus: 3736
  median_household_income: 50747
  poverty_rate: 23.35
  homeownership_rate: 71.02
  unemployment_rate: 6.68
  median_home_value: 140000
  gini_index: 0.4729
  vacancy_rate: 18.87
  race_white: 14226
  race_black: 6636
  race_asian: 200
  race_native: 77
  hispanic: 2595
  bachelors_plus: 3592
districts:
  - to: "us/states/ga/districts/12"
    rel: in-district
    area_weight: 0.9956
  - to: "us/states/ga/districts/senate/19"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ga/districts/house/157"
    rel: in-district
    area_weight: 0.9167
  - to: "us/states/ga/districts/house/156"
    rel: in-district
    area_weight: 0.0831
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Tattnall County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 24208 |
| Under 18 | 4872 |
| 18–64 | 15600 |
| 65+ | 3736 |
| Median household income | 50747 |
| Poverty rate | 23.35 |
| Homeownership rate | 71.02 |
| Unemployment rate | 6.68 |
| Median home value | 140000 |
| Gini index | 0.4729 |
| Vacancy rate | 18.87 |
| White | 14226 |
| Black | 6636 |
| Asian | 200 |
| Native | 77 |
| Hispanic/Latino | 2595 |
| Bachelor's or higher | 3592 |

## Districts

- [GA-12](/us/states/ga/districts/12.md) — 100% (congressional)
- [GA Senate District 19](/us/states/ga/districts/senate/19.md) — 100% (state senate)
- [GA House District 157](/us/states/ga/districts/house/157.md) — 92% (state house)
- [GA House District 156](/us/states/ga/districts/house/156.md) — 8% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
