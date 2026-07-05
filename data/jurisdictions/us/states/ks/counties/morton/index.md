---
type: Jurisdiction
title: "Morton County, KS"
classification: county
fips: "20129"
state: "KS"
demographics:
  population: 2611
  population_under_18: 636
  population_18_64: 1462
  population_65_plus: 513
  median_household_income: 66447
  poverty_rate: 14.77
  homeownership_rate: 85.39
  unemployment_rate: 1.64
  median_home_value: 96100
  gini_index: 0.4421
  vacancy_rate: 25.8
  race_white: 1971
  race_black: 31
  race_asian: 44
  race_native: 1
  hispanic: 628
  bachelors_plus: 410
districts:
  - to: "us/states/ks/districts/01"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ks/districts/senate/39"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ks/districts/house/124"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Morton County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2611 |
| Under 18 | 636 |
| 18–64 | 1462 |
| 65+ | 513 |
| Median household income | 66447 |
| Poverty rate | 14.77 |
| Homeownership rate | 85.39 |
| Unemployment rate | 1.64 |
| Median home value | 96100 |
| Gini index | 0.4421 |
| Vacancy rate | 25.8 |
| White | 1971 |
| Black | 31 |
| Asian | 44 |
| Native | 1 |
| Hispanic/Latino | 628 |
| Bachelor's or higher | 410 |

## Districts

- [KS-01](/us/states/ks/districts/01.md) — 100% (congressional)
- [KS Senate District 39](/us/states/ks/districts/senate/39.md) — 100% (state senate)
- [KS House District 124](/us/states/ks/districts/house/124.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
