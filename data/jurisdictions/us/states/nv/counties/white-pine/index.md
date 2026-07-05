---
type: Jurisdiction
title: "White Pine County, NV"
classification: county
fips: "32033"
state: "NV"
demographics:
  population: 8735
  population_under_18: 1704
  population_18_64: 5246
  population_65_plus: 1785
  median_household_income: 72865
  poverty_rate: 8.19
  homeownership_rate: 75.41
  unemployment_rate: 4.02
  median_home_value: 220000
  gini_index: 0.3792
  vacancy_rate: 19.25
  race_white: 6567
  race_black: 520
  race_asian: 45
  race_native: 546
  hispanic: 1442
  bachelors_plus: 996
districts:
  - to: "us/states/nv/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/nv/districts/senate/19"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/nv/districts/house/33"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nv]
timestamp: "2026-07-03"
---

# White Pine County, NV

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8735 |
| Under 18 | 1704 |
| 18–64 | 5246 |
| 65+ | 1785 |
| Median household income | 72865 |
| Poverty rate | 8.19 |
| Homeownership rate | 75.41 |
| Unemployment rate | 4.02 |
| Median home value | 220000 |
| Gini index | 0.3792 |
| Vacancy rate | 19.25 |
| White | 6567 |
| Black | 520 |
| Asian | 45 |
| Native | 546 |
| Hispanic/Latino | 1442 |
| Bachelor's or higher | 996 |

## Districts

- [NV-02](/us/states/nv/districts/02.md) — 100% (congressional)
- [NV Senate District 19](/us/states/nv/districts/senate/19.md) — 100% (state senate)
- [NV House District 33](/us/states/nv/districts/house/33.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
