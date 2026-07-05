---
type: Jurisdiction
title: "Smith County, TN"
classification: county
fips: "47159"
state: "TN"
demographics:
  population: 20389
  population_under_18: 4566
  population_18_64: 12424
  population_65_plus: 3399
  median_household_income: 66293
  poverty_rate: 10.02
  homeownership_rate: 76.9
  unemployment_rate: 2.66
  median_home_value: 243800
  gini_index: 0.4199
  vacancy_rate: 9.37
  race_white: 18414
  race_black: 384
  race_asian: 91
  race_native: 44
  hispanic: 641
  bachelors_plus: 3459
districts:
  - to: "us/states/tn/districts/06"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tn/districts/senate/15"
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

# Smith County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 20389 |
| Under 18 | 4566 |
| 18–64 | 12424 |
| 65+ | 3399 |
| Median household income | 66293 |
| Poverty rate | 10.02 |
| Homeownership rate | 76.9 |
| Unemployment rate | 2.66 |
| Median home value | 243800 |
| Gini index | 0.4199 |
| Vacancy rate | 9.37 |
| White | 18414 |
| Black | 384 |
| Asian | 91 |
| Native | 44 |
| Hispanic/Latino | 641 |
| Bachelor's or higher | 3459 |

## Districts

- [TN-06](/us/states/tn/districts/06.md) — 100% (congressional)
- [TN Senate District 15](/us/states/tn/districts/senate/15.md) — 100% (state senate)
- [TN House District 40](/us/states/tn/districts/house/40.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
