---
type: Jurisdiction
title: "Pawnee County, KS"
classification: county
fips: "20145"
state: "KS"
demographics:
  population: 6144
  population_under_18: 893
  population_18_64: 3819
  population_65_plus: 1432
  median_household_income: 63517
  poverty_rate: 11.52
  homeownership_rate: 66.16
  unemployment_rate: 1.22
  median_home_value: 93000
  gini_index: 0.4663
  vacancy_rate: 21.79
  race_white: 5218
  race_black: 454
  race_asian: 0
  race_native: 91
  hispanic: 561
  bachelors_plus: 1146
districts:
  - to: "us/states/ks/districts/04"
    rel: in-district
    area_weight: 0.5354
  - to: "us/states/ks/districts/01"
    rel: in-district
    area_weight: 0.4646
  - to: "us/states/ks/districts/senate/33"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/house/113"
    rel: in-district
    area_weight: 0.5257
  - to: "us/states/ks/districts/house/122"
    rel: in-district
    area_weight: 0.4743
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Pawnee County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 6144 |
| Under 18 | 893 |
| 18–64 | 3819 |
| 65+ | 1432 |
| Median household income | 63517 |
| Poverty rate | 11.52 |
| Homeownership rate | 66.16 |
| Unemployment rate | 1.22 |
| Median home value | 93000 |
| Gini index | 0.4663 |
| Vacancy rate | 21.79 |
| White | 5218 |
| Black | 454 |
| Asian | 0 |
| Native | 91 |
| Hispanic/Latino | 561 |
| Bachelor's or higher | 1146 |

## Districts

- [KS-04](/us/states/ks/districts/04.md) — 54% (congressional)
- [KS-01](/us/states/ks/districts/01.md) — 46% (congressional)
- [KS Senate District 33](/us/states/ks/districts/senate/33.md) — 100% (state senate)
- [KS House District 113](/us/states/ks/districts/house/113.md) — 53% (state house)
- [KS House District 122](/us/states/ks/districts/house/122.md) — 47% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
