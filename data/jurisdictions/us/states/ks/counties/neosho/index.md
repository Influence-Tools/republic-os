---
type: Jurisdiction
title: "Neosho County, KS"
classification: county
fips: "20133"
state: "KS"
demographics:
  population: 15656
  population_under_18: 3746
  population_18_64: 8687
  population_65_plus: 3223
  median_household_income: 56618
  poverty_rate: 13.14
  homeownership_rate: 77.18
  unemployment_rate: 3.24
  median_home_value: 111300
  gini_index: 0.4379
  vacancy_rate: 10.46
  race_white: 14450
  race_black: 245
  race_asian: 84
  race_native: 29
  hispanic: 944
  bachelors_plus: 3233
districts:
  - to: "us/states/ks/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/senate/15"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ks/districts/house/2"
    rel: in-district
    area_weight: 0.751
  - to: "us/states/ks/districts/house/7"
    rel: in-district
    area_weight: 0.2488
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Neosho County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 15656 |
| Under 18 | 3746 |
| 18–64 | 8687 |
| 65+ | 3223 |
| Median household income | 56618 |
| Poverty rate | 13.14 |
| Homeownership rate | 77.18 |
| Unemployment rate | 3.24 |
| Median home value | 111300 |
| Gini index | 0.4379 |
| Vacancy rate | 10.46 |
| White | 14450 |
| Black | 245 |
| Asian | 84 |
| Native | 29 |
| Hispanic/Latino | 944 |
| Bachelor's or higher | 3233 |

## Districts

- [KS-02](/us/states/ks/districts/02.md) — 100% (congressional)
- [KS Senate District 15](/us/states/ks/districts/senate/15.md) — 100% (state senate)
- [KS House District 2](/us/states/ks/districts/house/2.md) — 75% (state house)
- [KS House District 7](/us/states/ks/districts/house/7.md) — 25% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
