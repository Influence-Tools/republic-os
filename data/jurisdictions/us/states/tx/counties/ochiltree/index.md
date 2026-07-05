---
type: Jurisdiction
title: "Ochiltree County, TX"
classification: county
fips: "48357"
state: "TX"
demographics:
  population: 9786
  population_under_18: 2957
  population_18_64: 5685
  population_65_plus: 1144
  median_household_income: 70183
  poverty_rate: 11.85
  homeownership_rate: 72.72
  unemployment_rate: 0.28
  median_home_value: 134400
  gini_index: 0.4544
  vacancy_rate: 15.3
  race_white: 6617
  race_black: 4
  race_asian: 28
  race_native: 143
  hispanic: 5562
  bachelors_plus: 1592
districts:
  - to: "us/states/tx/districts/13"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/senate/31"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/87"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Ochiltree County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9786 |
| Under 18 | 2957 |
| 18–64 | 5685 |
| 65+ | 1144 |
| Median household income | 70183 |
| Poverty rate | 11.85 |
| Homeownership rate | 72.72 |
| Unemployment rate | 0.28 |
| Median home value | 134400 |
| Gini index | 0.4544 |
| Vacancy rate | 15.3 |
| White | 6617 |
| Black | 4 |
| Asian | 28 |
| Native | 143 |
| Hispanic/Latino | 5562 |
| Bachelor's or higher | 1592 |

## Districts

- [TX-13](/us/states/tx/districts/13.md) — 100% (congressional)
- [TX Senate District 31](/us/states/tx/districts/senate/31.md) — 100% (state senate)
- [TX House District 87](/us/states/tx/districts/house/87.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
