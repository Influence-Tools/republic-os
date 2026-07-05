---
type: Jurisdiction
title: "Middlesex County, MA"
classification: county
fips: "25017"
state: "MA"
demographics:
  population: 1638365
  population_under_18: 318865
  population_18_64: 1052493
  population_65_plus: 267007
  median_household_income: 130847
  poverty_rate: 7.74
  homeownership_rate: 61.32
  unemployment_rate: 4.35
  median_home_value: 727800
  gini_index: 0.4747
  vacancy_rate: 4.52
  race_white: 1093628
  race_black: 80327
  race_asian: 223582
  race_native: 3246
  hispanic: 151761
  bachelors_plus: 1044737
districts:
  - to: "us/states/ma/districts/03"
    rel: in-district
    area_weight: 0.4993
  - to: "us/states/ma/districts/05"
    rel: in-district
    area_weight: 0.2518
  - to: "us/states/ma/districts/06"
    rel: in-district
    area_weight: 0.1237
  - to: "us/states/ma/districts/02"
    rel: in-district
    area_weight: 0.0708
  - to: "us/states/ma/districts/04"
    rel: in-district
    area_weight: 0.0406
  - to: "us/states/ma/districts/07"
    rel: in-district
    area_weight: 0.0137
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ma]
timestamp: "2026-07-03"
---

# Middlesex County, MA

County jurisdiction — 7 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1638365 |
| Under 18 | 318865 |
| 18–64 | 1052493 |
| 65+ | 267007 |
| Median household income | 130847 |
| Poverty rate | 7.74 |
| Homeownership rate | 61.32 |
| Unemployment rate | 4.35 |
| Median home value | 727800 |
| Gini index | 0.4747 |
| Vacancy rate | 4.52 |
| White | 1093628 |
| Black | 80327 |
| Asian | 223582 |
| Native | 3246 |
| Hispanic/Latino | 151761 |
| Bachelor's or higher | 1044737 |

## Districts

- [MA-03](/us/states/ma/districts/03.md) — 50% (congressional)
- [MA-05](/us/states/ma/districts/05.md) — 25% (congressional)
- [MA-06](/us/states/ma/districts/06.md) — 12% (congressional)
- [MA-02](/us/states/ma/districts/02.md) — 7% (congressional)
- [MA-04](/us/states/ma/districts/04.md) — 4% (congressional)
- [MA-07](/us/states/ma/districts/07.md) — 1% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
