---
type: Jurisdiction
title: "Tipton County, TN"
classification: county
fips: "47167"
state: "TN"
demographics:
  population: 61553
  population_under_18: 14490
  population_18_64: 37446
  population_65_plus: 9617
  median_household_income: 74127
  poverty_rate: 13.6
  homeownership_rate: 76.32
  unemployment_rate: 5.53
  median_home_value: 240600
  gini_index: 0.4274
  vacancy_rate: 7.2
  race_white: 45987
  race_black: 11214
  race_asian: 281
  race_native: 150
  hispanic: 1916
  bachelors_plus: 11757
districts:
  - to: "us/states/tn/districts/09"
    rel: in-district
    area_weight: 0.56
  - to: "us/states/tn/districts/08"
    rel: in-district
    area_weight: 0.4382
  - to: "us/states/tn/districts/senate/32"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/tn/districts/house/81"
    rel: in-district
    area_weight: 0.9991
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Tipton County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 61553 |
| Under 18 | 14490 |
| 18–64 | 37446 |
| 65+ | 9617 |
| Median household income | 74127 |
| Poverty rate | 13.6 |
| Homeownership rate | 76.32 |
| Unemployment rate | 5.53 |
| Median home value | 240600 |
| Gini index | 0.4274 |
| Vacancy rate | 7.2 |
| White | 45987 |
| Black | 11214 |
| Asian | 281 |
| Native | 150 |
| Hispanic/Latino | 1916 |
| Bachelor's or higher | 11757 |

## Districts

- [TN-09](/us/states/tn/districts/09.md) — 56% (congressional)
- [TN-08](/us/states/tn/districts/08.md) — 44% (congressional)
- [TN Senate District 32](/us/states/tn/districts/senate/32.md) — 100% (state senate)
- [TN House District 81](/us/states/tn/districts/house/81.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
