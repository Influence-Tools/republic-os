---
type: Jurisdiction
title: "Cowley County, KS"
classification: county
fips: "20035"
state: "KS"
demographics:
  population: 34411
  population_under_18: 8111
  population_18_64: 19782
  population_65_plus: 6518
  median_household_income: 57878
  poverty_rate: 14.26
  homeownership_rate: 68.1
  unemployment_rate: 3.85
  median_home_value: 120900
  gini_index: 0.4778
  vacancy_rate: 14.63
  race_white: 27599
  race_black: 861
  race_asian: 532
  race_native: 480
  hispanic: 4184
  bachelors_plus: 7466
districts:
  - to: "us/states/ks/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/senate/32"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ks/districts/house/12"
    rel: in-district
    area_weight: 0.6649
  - to: "us/states/ks/districts/house/79"
    rel: in-district
    area_weight: 0.2707
  - to: "us/states/ks/districts/house/80"
    rel: in-district
    area_weight: 0.0644
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Cowley County, KS

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 34411 |
| Under 18 | 8111 |
| 18–64 | 19782 |
| 65+ | 6518 |
| Median household income | 57878 |
| Poverty rate | 14.26 |
| Homeownership rate | 68.1 |
| Unemployment rate | 3.85 |
| Median home value | 120900 |
| Gini index | 0.4778 |
| Vacancy rate | 14.63 |
| White | 27599 |
| Black | 861 |
| Asian | 532 |
| Native | 480 |
| Hispanic/Latino | 4184 |
| Bachelor's or higher | 7466 |

## Districts

- [KS-04](/us/states/ks/districts/04.md) — 100% (congressional)
- [KS Senate District 32](/us/states/ks/districts/senate/32.md) — 100% (state senate)
- [KS House District 12](/us/states/ks/districts/house/12.md) — 66% (state house)
- [KS House District 79](/us/states/ks/districts/house/79.md) — 27% (state house)
- [KS House District 80](/us/states/ks/districts/house/80.md) — 6% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
