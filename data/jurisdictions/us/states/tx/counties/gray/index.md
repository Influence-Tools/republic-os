---
type: Jurisdiction
title: "Gray County, TX"
classification: county
fips: "48179"
state: "TX"
demographics:
  population: 21045
  population_under_18: 5213
  population_18_64: 12324
  population_65_plus: 3508
  median_household_income: 59614
  poverty_rate: 15.72
  homeownership_rate: 76.37
  unemployment_rate: 5.57
  median_home_value: 102900
  gini_index: 0.4892
  vacancy_rate: 19.7
  race_white: 16229
  race_black: 960
  race_asian: 225
  race_native: 300
  hispanic: 6614
  bachelors_plus: 2709
districts:
  - to: "us/states/tx/districts/13"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/senate/28"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/88"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Gray County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 21045 |
| Under 18 | 5213 |
| 18–64 | 12324 |
| 65+ | 3508 |
| Median household income | 59614 |
| Poverty rate | 15.72 |
| Homeownership rate | 76.37 |
| Unemployment rate | 5.57 |
| Median home value | 102900 |
| Gini index | 0.4892 |
| Vacancy rate | 19.7 |
| White | 16229 |
| Black | 960 |
| Asian | 225 |
| Native | 300 |
| Hispanic/Latino | 6614 |
| Bachelor's or higher | 2709 |

## Districts

- [TX-13](/us/states/tx/districts/13.md) — 100% (congressional)
- [TX Senate District 28](/us/states/tx/districts/senate/28.md) — 100% (state senate)
- [TX House District 88](/us/states/tx/districts/house/88.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
