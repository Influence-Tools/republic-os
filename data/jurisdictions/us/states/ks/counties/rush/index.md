---
type: Jurisdiction
title: "Rush County, KS"
classification: county
fips: "20165"
state: "KS"
demographics:
  population: 2947
  population_under_18: 589
  population_18_64: 1626
  population_65_plus: 732
  median_household_income: 59970
  poverty_rate: 11.14
  homeownership_rate: 77.58
  unemployment_rate: 3.6
  median_home_value: 83600
  gini_index: 0.5437
  vacancy_rate: 17.39
  race_white: 2603
  race_black: 11
  race_asian: 0
  race_native: 16
  hispanic: 191
  bachelors_plus: 590
districts:
  - to: "us/states/ks/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/senate/33"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/house/113"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Rush County, KS

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2947 |
| Under 18 | 589 |
| 18–64 | 1626 |
| 65+ | 732 |
| Median household income | 59970 |
| Poverty rate | 11.14 |
| Homeownership rate | 77.58 |
| Unemployment rate | 3.6 |
| Median home value | 83600 |
| Gini index | 0.5437 |
| Vacancy rate | 17.39 |
| White | 2603 |
| Black | 11 |
| Asian | 0 |
| Native | 16 |
| Hispanic/Latino | 191 |
| Bachelor's or higher | 590 |

## Districts

- [KS-01](/us/states/ks/districts/01.md) — 100% (congressional)
- [KS Senate District 33](/us/states/ks/districts/senate/33.md) — 100% (state senate)
- [KS House District 113](/us/states/ks/districts/house/113.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
