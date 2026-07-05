---
type: Jurisdiction
title: "Medina County, TX"
classification: county
fips: "48325"
state: "TX"
demographics:
  population: 53547
  population_under_18: 11970
  population_18_64: 32084
  population_65_plus: 9493
  median_household_income: 78074
  poverty_rate: 9.63
  homeownership_rate: 83.82
  unemployment_rate: 3.05
  median_home_value: 239600
  gini_index: 0.4118
  vacancy_rate: 10.49
  race_white: 31173
  race_black: 1567
  race_asian: 487
  race_native: 305
  hispanic: 27578
  bachelors_plus: 11509
districts:
  - to: "us/states/tx/districts/23"
    rel: in-district
    area_weight: 0.9991
  - to: "us/states/tx/districts/senate/24"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/53"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Medina County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 53547 |
| Under 18 | 11970 |
| 18–64 | 32084 |
| 65+ | 9493 |
| Median household income | 78074 |
| Poverty rate | 9.63 |
| Homeownership rate | 83.82 |
| Unemployment rate | 3.05 |
| Median home value | 239600 |
| Gini index | 0.4118 |
| Vacancy rate | 10.49 |
| White | 31173 |
| Black | 1567 |
| Asian | 487 |
| Native | 305 |
| Hispanic/Latino | 27578 |
| Bachelor's or higher | 11509 |

## Districts

- [TX-23](/us/states/tx/districts/23.md) — 100% (congressional)
- [TX Senate District 24](/us/states/tx/districts/senate/24.md) — 100% (state senate)
- [TX House District 53](/us/states/tx/districts/house/53.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
