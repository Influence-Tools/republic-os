---
type: Jurisdiction
title: "Hamblen County, TN"
classification: county
fips: "47063"
state: "TN"
demographics:
  population: 65669
  population_under_18: 15706
  population_18_64: 38213
  population_65_plus: 11750
  median_household_income: 55454
  poverty_rate: 18.35
  homeownership_rate: 69.76
  unemployment_rate: 5.26
  median_home_value: 210900
  gini_index: 0.4658
  vacancy_rate: 6.94
  race_white: 52162
  race_black: 1909
  race_asian: 661
  race_native: 273
  hispanic: 9926
  bachelors_plus: 12624
districts:
  - to: "us/states/tn/districts/01"
    rel: in-district
    area_weight: 0.9925
  - to: "us/states/tn/districts/02"
    rel: in-district
    area_weight: 0.0075
  - to: "us/states/tn/districts/senate/9"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/tn/districts/house/11"
    rel: in-district
    area_weight: 0.5369
  - to: "us/states/tn/districts/house/10"
    rel: in-district
    area_weight: 0.4627
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Hamblen County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 65669 |
| Under 18 | 15706 |
| 18–64 | 38213 |
| 65+ | 11750 |
| Median household income | 55454 |
| Poverty rate | 18.35 |
| Homeownership rate | 69.76 |
| Unemployment rate | 5.26 |
| Median home value | 210900 |
| Gini index | 0.4658 |
| Vacancy rate | 6.94 |
| White | 52162 |
| Black | 1909 |
| Asian | 661 |
| Native | 273 |
| Hispanic/Latino | 9926 |
| Bachelor's or higher | 12624 |

## Districts

- [TN-01](/us/states/tn/districts/01.md) — 99% (congressional)
- [TN-02](/us/states/tn/districts/02.md) — 1% (congressional)
- [TN Senate District 9](/us/states/tn/districts/senate/9.md) — 100% (state senate)
- [TN House District 11](/us/states/tn/districts/house/11.md) — 54% (state house)
- [TN House District 10](/us/states/tn/districts/house/10.md) — 46% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
