---
type: Jurisdiction
title: "Sullivan County, PA"
classification: county
fips: "42113"
state: "PA"
demographics:
  population: 5888
  population_under_18: 615
  population_18_64: 3421
  population_65_plus: 1852
  median_household_income: 69764
  poverty_rate: 11.58
  homeownership_rate: 84.95
  unemployment_rate: 5.83
  median_home_value: 197100
  gini_index: 0.4393
  vacancy_rate: 54.32
  race_white: 5520
  race_black: 138
  race_asian: 5
  race_native: 18
  hispanic: 138
  bachelors_plus: 1442
districts:
  - to: "us/states/pa/districts/09"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/pa/districts/senate/23"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/pa/districts/house/84"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, pa]
timestamp: "2026-07-03"
---

# Sullivan County, PA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5888 |
| Under 18 | 615 |
| 18–64 | 3421 |
| 65+ | 1852 |
| Median household income | 69764 |
| Poverty rate | 11.58 |
| Homeownership rate | 84.95 |
| Unemployment rate | 5.83 |
| Median home value | 197100 |
| Gini index | 0.4393 |
| Vacancy rate | 54.32 |
| White | 5520 |
| Black | 138 |
| Asian | 5 |
| Native | 18 |
| Hispanic/Latino | 138 |
| Bachelor's or higher | 1442 |

## Districts

- [PA-09](/us/states/pa/districts/09.md) — 100% (congressional)
- [PA Senate District 23](/us/states/pa/districts/senate/23.md) — 100% (state senate)
- [PA House District 84](/us/states/pa/districts/house/84.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
