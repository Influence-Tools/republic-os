---
type: Jurisdiction
title: "Cannon County, TN"
classification: county
fips: "47015"
state: "TN"
demographics:
  population: 14818
  population_under_18: 3610
  population_18_64: 4565
  population_65_plus: 6643
  median_household_income: 59443
  poverty_rate: 18.27
  homeownership_rate: 78.38
  unemployment_rate: 2.8
  median_home_value: 252000
  gini_index: 0.442
  vacancy_rate: 10.49
  race_white: 13832
  race_black: 337
  race_asian: 0
  race_native: 26
  hispanic: 460
  bachelors_plus: 2363
districts:
  - to: "us/states/tn/districts/06"
    rel: in-district
    area_weight: 0.9931
  - to: "us/states/tn/districts/04"
    rel: in-district
    area_weight: 0.0069
  - to: "us/states/tn/districts/senate/14"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tn/districts/house/40"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Cannon County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 14818 |
| Under 18 | 3610 |
| 18–64 | 4565 |
| 65+ | 6643 |
| Median household income | 59443 |
| Poverty rate | 18.27 |
| Homeownership rate | 78.38 |
| Unemployment rate | 2.8 |
| Median home value | 252000 |
| Gini index | 0.442 |
| Vacancy rate | 10.49 |
| White | 13832 |
| Black | 337 |
| Asian | 0 |
| Native | 26 |
| Hispanic/Latino | 460 |
| Bachelor's or higher | 2363 |

## Districts

- [TN-06](/us/states/tn/districts/06.md) — 99% (congressional)
- [TN-04](/us/states/tn/districts/04.md) — 1% (congressional)
- [TN Senate District 14](/us/states/tn/districts/senate/14.md) — 100% (state senate)
- [TN House District 40](/us/states/tn/districts/house/40.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
