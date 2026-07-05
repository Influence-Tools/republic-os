---
type: Jurisdiction
title: "Licking County, OH"
classification: county
fips: "39089"
state: "OH"
demographics:
  population: 181837
  population_under_18: 41505
  population_18_64: 108554
  population_65_plus: 31778
  median_household_income: 84426
  poverty_rate: 10.22
  homeownership_rate: 73.74
  unemployment_rate: 3.24
  median_home_value: 275200
  gini_index: 0.447
  vacancy_rate: 6.35
  race_white: 155770
  race_black: 7654
  race_asian: 6787
  race_native: 48
  hispanic: 4459
  bachelors_plus: 48678
districts:
  - to: "us/states/oh/districts/12"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/oh/districts/senate/20"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/oh/districts/house/69"
    rel: in-district
    area_weight: 0.6683
  - to: "us/states/oh/districts/house/68"
    rel: in-district
    area_weight: 0.3316
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, oh]
timestamp: "2026-07-03"
---

# Licking County, OH

County jurisdiction — 3 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 181837 |
| Under 18 | 41505 |
| 18–64 | 108554 |
| 65+ | 31778 |
| Median household income | 84426 |
| Poverty rate | 10.22 |
| Homeownership rate | 73.74 |
| Unemployment rate | 3.24 |
| Median home value | 275200 |
| Gini index | 0.447 |
| Vacancy rate | 6.35 |
| White | 155770 |
| Black | 7654 |
| Asian | 6787 |
| Native | 48 |
| Hispanic/Latino | 4459 |
| Bachelor's or higher | 48678 |

## Districts

- [OH-12](/us/states/oh/districts/12.md) — 100% (congressional)
- [OH Senate District 20](/us/states/oh/districts/senate/20.md) — 100% (state senate)
- [OH House District 69](/us/states/oh/districts/house/69.md) — 67% (state house)
- [OH House District 68](/us/states/oh/districts/house/68.md) — 33% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
