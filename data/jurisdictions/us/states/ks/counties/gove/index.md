---
type: Jurisdiction
title: "Gove County, KS"
classification: county
fips: "20063"
state: "KS"
demographics:
  population: 2799
  population_under_18: 706
  population_18_64: 1454
  population_65_plus: 639
  median_household_income: 66029
  poverty_rate: 5.06
  homeownership_rate: 79.37
  unemployment_rate: 2.61
  median_home_value: 118400
  gini_index: 0.4395
  vacancy_rate: 12.25
  race_white: 2637
  race_black: 14
  race_asian: 23
  race_native: 0
  hispanic: 47
  bachelors_plus: 577
districts:
  - to: "us/states/ks/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/senate/40"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/house/118"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Gove County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2799 |
| Under 18 | 706 |
| 18–64 | 1454 |
| 65+ | 639 |
| Median household income | 66029 |
| Poverty rate | 5.06 |
| Homeownership rate | 79.37 |
| Unemployment rate | 2.61 |
| Median home value | 118400 |
| Gini index | 0.4395 |
| Vacancy rate | 12.25 |
| White | 2637 |
| Black | 14 |
| Asian | 23 |
| Native | 0 |
| Hispanic/Latino | 47 |
| Bachelor's or higher | 577 |

## Districts

- [KS-01](/us/states/ks/districts/01.md) — 100% (congressional)
- [KS Senate District 40](/us/states/ks/districts/senate/40.md) — 100% (state senate)
- [KS House District 118](/us/states/ks/districts/house/118.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
