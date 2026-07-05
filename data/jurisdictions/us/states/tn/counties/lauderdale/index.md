---
type: Jurisdiction
title: "Lauderdale County, TN"
classification: county
fips: "47097"
state: "TN"
demographics:
  population: 24784
  population_under_18: 5371
  population_18_64: 15282
  population_65_plus: 4131
  median_household_income: 49879
  poverty_rate: 21.04
  homeownership_rate: 64.35
  unemployment_rate: 5.57
  median_home_value: 143200
  gini_index: 0.4708
  vacancy_rate: 12.87
  race_white: 14621
  race_black: 8305
  race_asian: 155
  race_native: 48
  hispanic: 685
  bachelors_plus: 2688
districts:
  - to: "us/states/tn/districts/08"
    rel: in-district
    area_weight: 0.996
  - to: "us/states/tn/districts/senate/32"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/tn/districts/house/82"
    rel: in-district
    area_weight: 0.999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Lauderdale County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 24784 |
| Under 18 | 5371 |
| 18–64 | 15282 |
| 65+ | 4131 |
| Median household income | 49879 |
| Poverty rate | 21.04 |
| Homeownership rate | 64.35 |
| Unemployment rate | 5.57 |
| Median home value | 143200 |
| Gini index | 0.4708 |
| Vacancy rate | 12.87 |
| White | 14621 |
| Black | 8305 |
| Asian | 155 |
| Native | 48 |
| Hispanic/Latino | 685 |
| Bachelor's or higher | 2688 |

## Districts

- [TN-08](/us/states/tn/districts/08.md) — 100% (congressional)
- [TN Senate District 32](/us/states/tn/districts/senate/32.md) — 100% (state senate)
- [TN House District 82](/us/states/tn/districts/house/82.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
