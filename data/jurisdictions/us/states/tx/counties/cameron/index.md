---
type: Jurisdiction
title: "Cameron County, TX"
classification: county
fips: "48061"
state: "TX"
demographics:
  population: 426120
  population_under_18: 122156
  population_18_64: 243045
  population_65_plus: 60919
  median_household_income: 52601
  poverty_rate: 24.83
  homeownership_rate: 65.21
  unemployment_rate: 5.91
  median_home_value: 136500
  gini_index: 0.4711
  vacancy_rate: 13.31
  race_white: 150891
  race_black: 2563
  race_asian: 3463
  race_native: 2250
  hispanic: 380524
  bachelors_plus: 74818
districts:
  - to: "us/states/tx/districts/34"
    rel: in-district
    area_weight: 0.7903
  - to: "us/states/tx/districts/senate/27"
    rel: in-district
    area_weight: 0.7854
  - to: "us/states/tx/districts/house/37"
    rel: in-district
    area_weight: 0.5851
  - to: "us/states/tx/districts/house/35"
    rel: in-district
    area_weight: 0.145
  - to: "us/states/tx/districts/house/38"
    rel: in-district
    area_weight: 0.0553
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Cameron County, TX

County jurisdiction — 5 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 426120 |
| Under 18 | 122156 |
| 18–64 | 243045 |
| 65+ | 60919 |
| Median household income | 52601 |
| Poverty rate | 24.83 |
| Homeownership rate | 65.21 |
| Unemployment rate | 5.91 |
| Median home value | 136500 |
| Gini index | 0.4711 |
| Vacancy rate | 13.31 |
| White | 150891 |
| Black | 2563 |
| Asian | 3463 |
| Native | 2250 |
| Hispanic/Latino | 380524 |
| Bachelor's or higher | 74818 |

## Districts

- [TX-34](/us/states/tx/districts/34.md) — 79% (congressional)
- [TX Senate District 27](/us/states/tx/districts/senate/27.md) — 79% (state senate)
- [TX House District 37](/us/states/tx/districts/house/37.md) — 59% (state house)
- [TX House District 35](/us/states/tx/districts/house/35.md) — 14% (state house)
- [TX House District 38](/us/states/tx/districts/house/38.md) — 6% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
